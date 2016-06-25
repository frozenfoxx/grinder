# Directory Layout
[Grinder](https://github.com/frozenfoxx/grinder) ensures a specific directory layout to ensure uniform environment execution.  The *environmentdir* variable in the configuration file is the path to a given directory where this directory layout will be unrolled when the tool is run.  __Note:__ it is *strongly* advised not to leave anything permanent in this directory tree as it can be wiped out when deployed.  Assuming the default of */srv/salt/environments* it will resemble such:
* */srv/salt/environments/<branch>/*
* */srv/salt/environments/<branch>/states*
* */srv/salt/environments/<branch>/pillar*

The `seasoning.yaml` file placed in the base of your Salt State repo directory structure will be parsed for Salt Formulas to pull down.  These will be placed into the *states* directory above.

# FAQ
## Why aren't Formulas in their own directory structure?
Due to a limitation of how Salt parses directory trees it expects the formulas to be in directories of the same name located in the same directory as a `top.sls` file.  If these are placed in another directory tree then it, too, will require an identical `top.sls`.  The *merge* option for handling these files will attempt to merge across __all__ environments which can allow for collisions in Formulas across environments.
