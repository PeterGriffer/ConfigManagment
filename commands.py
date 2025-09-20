class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def execute(self, args, vfs):
        pass

class LcCommand(Command):
    def __init__(self):
        super().__init__(name="lc", description="List contents")
    
    def execute(self, args, vfs):
        print("Executing lc command with args:", args)
        return True
    

class CdCommand(Command):
    def __init__(self):
        super().__init__(name="cd", description="Change directory")
    
    def execute(self, args, vfs):
        print("Executing cd command with args:", args)
        
        return True
    

class ExitCommand(Command):
    def __init__(self):
        super().__init__(name="exit", description="Exit console")
    
    def execute(self, args, vfs):
        print("Goodbye!")
        return False
