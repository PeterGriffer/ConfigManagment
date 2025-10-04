class VFS:
    def __init__(self, name='myfirstVFS'):
        self.prompt = "C:\\VFS> "
        self.name = name
        self.console = None

    def get_prompt(self):
        return self.prompt

    def set_prompt(self, newprompt):
        self.prompt = newprompt