# grinder
Grinder is a dynamic environment deployment tool for SaltStack inspired by the excellent [r10k](https://github.com/puppetlabs/r10k).  Using it allows for dynamic, flexible deployments of multiple environments with formulas, states, and pillars.

# Requirements
* Python 3+
* GitPython

# How to Use
* Configure the Salt master configuration file to set `top_file_merging_strategy: same`.
* List desired Salt formulas for an environment in a file `seasoning.yaml` in the base of each branch.
* Adjust the values in the `config/grinder.conf` to point to the locations of your repositories for Salt states and Pillar states.
* Run `grinder`
* To use a Minion, use the option `saltenv=<branch>`.
