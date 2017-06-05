import os
import shutil

class Environment:
    """ A dynamic environment """

    def __init__(self, dir):
        self.basedir = dir

    def clean(self):
        shutil.rmtree(self.basedir)
        os.makedirs(self.basedir, exist_ok=True)
