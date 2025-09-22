class VFS:
    def __init__(self,name='myfurstVFS'):
        self.prompt = "[home@localhost~]# "
        self.name=name
    #
    def get_prompt(self):
        return self.prompt
    
    def set_prompt(self, newprompt):
        self.prompt = newprompt