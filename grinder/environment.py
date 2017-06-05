import os
import shutil

class Environment:
    """ A dynamic environment """

    def __init__(self, dir):
        self.basedir = dir

    def clean(self):
        """ Cleans out the old environment layout """
        shutil.rmtree(self.basedir)
        os.makedirs(self.basedir, exist_ok=True)

    def createbranch(self, branch):
        """ Creates a directory for a branch of the repo """
        os.makedirs(self.basedir + "/" + branch, 0o755)
