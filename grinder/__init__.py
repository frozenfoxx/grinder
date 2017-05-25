import configparser
import git
import repository
import seasoning
import shutil
import os

# Source configuration
conf = configparser.ConfigParser()
conf.read("conf/grinder.conf")

print("Configuration loaded.")
print("Base directory for environments:  " + str(conf['environment']['environmentdir']))
print("Remote Salt States repository:  " + str(conf['environment']['statesrepo']))
print("Remote Pillar repository:  " + str(conf['environment']['pillarrepo']))

# Read repository master branches
statebranches = lsremote(conf['environment']['statesrepo'])
pillarbranches = lsremote(conf['environment']['pillarrepo'])

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
    clonestates(conf['environment']['statesrepo'], conf['environment']['environmentdir'], branch)

    # Parse the Seasoning file
    s = seasoning.Seasoning(conf['environment']['environmentdir'], branch)
    s.deploy()

print("Branches of Pillar:  ")
for key in pillarbranches:
  if key != "HEAD":
    branch = key.split('/')[-1]
    print(branch)

    # Clone branch
    clonepillar(conf['environment']['pillarrepo'], conf['environment']['environmentdir'], branch)
