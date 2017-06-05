""" grinder core functionality """

import configparser
import os
import shutil
from .environment import Environment
from .repository import Repository
from .seasoning import Seasoning

def main():
    # Source configuration
    conf = configparser.ConfigParser()
    conf.read("/etc/grinder/grinder.conf")

    print("Configuration loaded.")
    print("Base directory for environments:  " + str(conf['environment']['environmentdir']))
    print("Remote Salt States repository:  " + str(conf['environment']['statesrepo']))
    print("Remote Pillar repository:  " + str(conf['environment']['pillarrepo']))

    # Set environment
    statesrepo = Repository(conf['environment']['statesrepo'], conf['environment']['environmentdir'], "states")
    pillarrepo = Repository(conf['environment']['pillarrepo'], conf['environment']['environmentdir'], "pillar")
    environment = Environment(conf['environment']['environmentdir'])

    # Read repository master branches
    statebranches = statesrepo.lsremote()
    pillarbranches = pillarrepo.lsremote()

    # Clean up old environment
    environment.clean()

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
            s = Seasoning(conf['environment']['environmentdir'], branch)
            s.deploy()

    print("Branches of Pillar:  ")
    for key in pillarbranches:
        if key != "HEAD":
            branch = key.split('/')[-1]
            print(branch)

            # Clone branch
            pillarrepo.clone(branch)
