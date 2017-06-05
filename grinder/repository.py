import git

class Repository:
    """ grinder Repository class """

    def __init__(self, url, basedir, postfix):
        self.url = url
        self.basedir = basedir
        self.postfix = postfix

    def lsremote(self):
        """ List branches in the repository """
        remote_refs = {}
        g = git.cmd.Git()
        for ref in g.ls_remote(self.url).split('\n'):
            hash_ref_list = ref.split('\t')
            remote_refs[hash_ref_list[1]] = hash_ref_list[0]
        return remote_refs

    def clone(self, branch):
        """ Clone a repository branch """
        targetdir = self.basedir + "/" + branch + "/" + self.postfix
        g = git.cmd.Git()
        g.clone(self.url, targetdir, branch=branch, depth=1)
