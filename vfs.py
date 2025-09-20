class VFS:
    def __init__(self):
        self.prompt = "[home@localhost~]# "
    
    def get_prompt(self):
        return self.prompt
    
    def set_prompt(self, newprompt):
        self.prompt = newprompt