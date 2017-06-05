import git
import shutil
import yaml

class Seasoning:
    """ grinder Repository class """

    def __init__(self, basedir, branch):
        self.statesdir = basedir + "/" + branch + "/states"
        self.fileref = self.statesdir + "/seasoning.yml"
        self.config = ""

    def loadseasoning(self):
        """ Parse the seasoning file """
        stream = open(self.fileref)
        self.config = yaml.safe_load(stream)
        stream.close()

    def deploy(self):
        """ Deploy formulas in the seasoning file """
        self.loadseasoning()
        for key in self.config:
            print("Deploying " + key + " formula...")
            self.cloneformula(key, self.config[key]['reponame'], \
            self.config[key]['url'], self.config[key]['branch'])

    def cloneformula(self, formulaname, reponame, url, branch):
        """ Clone a given formula """
        repotargetdir = self.statesdir + "/" + reponame
        clonedformuladir = repotargetdir + "/" + formulaname

        g = git.cmd.Git()
        g.clone(url, repotargetdir, branch=branch, depth=1)

        shutil.move(clonedformuladir, (self.statesdir + "/" + formulaname))
        shutil.rmtree(repotargetdir)
