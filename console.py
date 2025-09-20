from commands import *
from parser_1 import Parser
from vfs import VFS


class Console:
    def __init__(self):
        self.vfs = VFS()
        self.parser = Parser()
        self.commands = self._register_commands()
        self.running = False
    
    def _register_commands(self):
        commands = {}                  #словарь с командами
        commands["lc"] = LcCommand()
        commands["cd"] = CdCommand()
        commands["exit"] = ExitCommand()
        return commands
    
    def execute_command(self, command_name, args):
        if command_name in self.commands:
            return self.commands[command_name].execute(args, self.vfs)
        else:
            print(f"Unknown command: {command_name}")
            return True
    
    def run(self):
        self.running = True
        print("Welcome to VFS Console! Type 'exit' to quit.")
        
        while self.running:
            try:
                user_input = input(self.vfs.get_prompt()).strip()
                if not user_input:
                    continue
                
                command_name, args = self.parser.parse(user_input)
                self.running = self.execute_command(command_name, args)
                
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit")
            except Exception as e:
                print(f"Error: {e}")


