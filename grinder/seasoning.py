#! /usr/bin/env python
import git
import shutil
import os
import yaml

class Seasoning:
  def __init__(self, basedir, branch):
    self.statesdir = basedir + "/" + branch + "/states"
    self.fileref = self.statesdir + "/seasoning.yml"
    self.config = ""

  def loadseasoning(self):
    stream = open(self.fileref)
    self.config = yaml.safe_load(stream)
    stream.close()

  def deploy(self):
    self.loadseasoning()
    for key in self.config:
      print("Deploying " + key + " formula...")
      self.cloneformula(key, self.config[key]['reponame'], self.config[key]['url'], self.config[key]['branch'])
  
  def cloneformula(self, formulaname, reponame, url, branch):
    repotargetdir = self.statesdir + "/" + reponame
    clonedformuladir = repotargetdir + "/" + formulaname

    g = git.cmd.Git()
    g.clone(url, repotargetdir, branch=branch, depth=1)

    shutil.move(clonedformuladir, (self.statesdir + "/" + formulaname))
    shutil.rmtree(repotargetdir)
