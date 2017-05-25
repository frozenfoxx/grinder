# grinder
Grinder is a dynamic environment deployment tool for SaltStack inspired by the excellent [r10k](https://github.com/puppetlabs/r10k).  Using it allows for dynamic, flexible deployments of multiple environments with formulas, states, and pillars.

# Requirements
* Python 3+
* GitPython
* PyYAML

# Setup
* It is recommended to use [VirtualEnv](https://virtualenv.pypa.io/en/stable/) to manage your Python environment.
 * `python3 -m venv ~/.virtualenv/grinder`
 * `source ~/.virtualenv/grinder/bin/activate`
* `pip install gitpython`
* `pip install pyyaml`

# Configuration
## Grinder
You'll need to update the environment configuration to point at your `states` repository and your `pillar` repository.  This is currently located under the project directory in `<repobase>/grinder/conf/grinder/grinder.conf`.  Modify the *environment* section to point at your remote repositories.

## Repository
There are several steps to be taken to prepare your repositories for dynamic deployment.
* The `top.sls` file must be configured as if it is the *only* one being deployed.  It can be completely unique between branches.
* The *pillar* and *states* repositories at this time __must__ have the same branches as they will be deployed together.  This may be altered in the future.  Just remember that when you make a new feature branch in your *states* repository you're going to have to make a corresponding branch for *pillar* as well.
* Remove all external formulas from your *states* repository branches.  In each branch place them into a `seasoning.yml` file located in the base of the *states* respository.  There is an example YAML file specifying the format located in this repository.

## Salt
* Configure the Salt master configuration file to set `top_file_merging_strategy: same`.

# Usage
This workflow assumes that you have a `base` branch and wish to create, test, and then integrate a new feature into the codebase.  The normal workflow goes like this:
* Have Pillar and States repos.
* In each repo, check out a new branch called, `featurebranch`.
* In each `top.sls`, either use `{{ saltenv }}` at the top or add a `featurebranch` section with targets.
* Modify code in repos until satisfied with changes.
* Push each repo to origin.
* On salt *master*, run grinder.
* Update `master.conf` to point at new `file_roots` and `pillar_roots` directories. [to be eventually handled by Grinder]
* Kick *saltmaster* service. [to be eventually handled by Grinder]
* Either from salt *master* or from *minion*, run `salt state.apply --saltenv=featurebranch`.
* Iterate on code, pushing back to master and redeploying with Grinder until desired behavior is achieved.
* In both repos remove the `featurebranch` section or leave in `{{ saltenv }}`.
* `git checkout base && git merge featurebranch`.
* On salt *master* run grinder, update `master.conf` to remove references to `featurebranch`, kick salt *master*.

# Future
At the moment Grinder does not automatically update the Salt `master.conf` file.  It also does not automatically kick the *saltmaster* service to reload and re-initialize values.  Eventually there should also be an option not to touch the Pillar data in any way as alternatives may be desired.  Finally Grinder should eventually handle more than just Git.
