# grinder
Grinder is a dynamic environment deployment tool for SaltStack inspired by the excellent [r10k](https://github.com/puppetlabs/r10k).  Using it allows for dynamic, flexible deployments of multiple environments with formulas, states, and pillars.

# Requirements
* Python 3+
* GitPython

# Setup
* It is recommended to use [VirtualEnv](https://virtualenv.pypa.io/en/stable/) to manage your Python environment.
 * `mkdir ~/.virtualenv`
 * `cd ~/.virtualenv`
 * `virtualenv grinder`
 * `source ~/.virtualenv/grinder/bin/activate`
* `pip install gitpython`
* `pip install pyyaml`

# Configuration
## Grinder
You'll need to update the environment configuration to point at your `states` repository and your `pillar` repository.  This is currently located under the project directory in `<repobase>/grinder/conf/grinder/grinder.conf`.  Modify the *environment* section to point at your remote repositories.

## Repository
There are several steps to be taken to prepare your repositories for dynamic deployment.
* The `top.sls` file must be configured as if it is the *only* one being deployed.  It can be completely unique between branches.
* The *pillar* and *state* repositories at this time __must__ have the same branches as they will be deployed together.  This may be altered in the future.  Just remember that when you make a new feature branch in your *states* repository you're going to have to make a corresponding branch for *pillar* as well.
* Remove all external formulas from your *states* repository branches.  In each branch place them into a `seasoning.yml` file located in the base of the *states* respository.  There is an example YAML file specifying the format located in this repository.

## Salt
* Configure the Salt master configuration file to set `top_file_merging_strategy: same`.

# Usage
* Run `grinder`.
* Modify the Salt Master's `master` configuration to point the `file_roots` and `pillar_roots` sections at the newly created branches in the directory structure (*default:*  */srv/salt/environments/branchname*).
* Restart Salt Master.
* To use an alternate dynamic environment on a Minion, use the option `saltenv=<branch>`.
