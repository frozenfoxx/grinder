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
  
  def cloneformula(self, name, url, branch):
    targetdir = self.statesdir + "/" + name
    g = git.cmd.Git()
    g.clone(url, targetdir, branch=branch, depth=1)
    # mv the cloned target/reponame -> self.statesdir
    # shutil.rmtree(reponame)
