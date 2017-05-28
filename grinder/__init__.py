import configparser
import git
import repository
import seasoning
import shutil
import os
import yaml

# Source configuration
conf = configparser.ConfigParser()
conf.read("conf/grinder.conf")

print("Configuration loaded.")
print("Base directory for environments:  " + str(conf['environment']['environmentdir']))
print("Remote Salt States repository:  " + str(conf['environment']['statesrepo']))
print("Remote Pillar repository:  " + str(conf['environment']['pillarrepo']))

# Set repositories
statesrepo = repository.Repository(conf['environment']['statesrepo'], conf['environment']['environmentdir'], "states")
pillarrepo = repository.Repository(conf['environment']['pillarrepo'], conf['environment']['environmentdir'], "pillar")

# Read repository master branches
statebranches = statesrepo.lsremote()
pillarbranches = pillarrepo.lsremote()

# Clean up old environment
shutil.rmtree(conf['environment']['environmentdir'])

# Make directory structure for the branch
print("Branches of Salt States:  ")
for key in statebranches:
    if key != "HEAD":
        branch = key.split('/')[-1]
        print(branch)
        os.makedirs(conf['environment']['environmentdir'] + "/" + branch, 0o755)

    # Clone branch
    statesrepo.clone(branch)

    # Parse the Seasoning file
    s = seasoning.Seasoning(conf['environment']['environmentdir'], branch)
    s.deploy()

print("Branches of Pillar:  ")
for key in pillarbranches:
    if key != "HEAD":
        branch = key.split('/')[-1]
        print(branch)

        # Clone branch
        pillarrepo.clone(branch)
