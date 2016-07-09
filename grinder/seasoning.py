#! /usr/bin/env python
import git
import shutil
import os
import yaml

class Seasoning:
  def __init__(basedir, branch):
    self.fileref = basedir + "/" + branch + "/states/seasoning.yml"
    self.statesdir = basedir + "/" + branch + "/states"
    self.config = ""

  def loadseasoning():
    self.config = yaml.safe_load(self.fileref)
  
  def cloneformula(name, url, branch):
    targetdir = self.statesdir + "/" + name
    g = git.cmd.Git()
    g.clone(url, targetdir, branch=branch, depth=1)
