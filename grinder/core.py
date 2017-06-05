""" grinder core functionality """

import configparser
from .environment import Environment
from .repository import Repository
from .seasoning import Seasoning

def main():
    """ Main execution thread """
    # Source configuration
    conf = configparser.ConfigParser()
    conf.read("/etc/grinder/grinder.conf")

    print("Configuration loaded.")
    print("Base directory for environments:  " + str(conf['environment']['environmentdir']))
    print("Remote Salt States repository:  " + str(conf['environment']['statesrepo']))
    print("Remote Pillar repository:  " + str(conf['environment']['pillarrepo']))

    # Set environment
    environment = Environment(conf['environment']['environmentdir'])
    statesrepo = Repository(conf['environment']['statesrepo'], conf['environment']['environmentdir'], "states")
    pillarrepo = Repository(conf['environment']['pillarrepo'], conf['environment']['environmentdir'], "pillar")

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
            environment.createbranch(branch)

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
