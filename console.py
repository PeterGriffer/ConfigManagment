from commands import *
from parser_1 import Parser
from vfs import VFS
import sys
import time
#
class Console:
    def __init__(self):
        self.vfs = VFS()
        self.parser = Parser()
        self.commands = self._register_commands()
        self.running = False
        self.vfs.console=self
        self.countercom=0
        self.start_time=time.time()
    
    def get_uptime(self):
        """Возвращает время работы в формате 'Xh Ym'"""
        uptime_seconds = time.time() - self.start_time
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        
        return f"{hours}hour {minutes}min {int(uptime_seconds)}sec"
    
    def _register_commands(self):
        commands = {}                  #словарь с командами
        commands["lc"] = LcCommand()
        commands["cd"] = CdCommand()
        commands["exit"] = ExitCommand()
        commands["conf-dump"] = ConfDumpCommand()
        return commands
    
    def execute_command(self, command_name, args):
        self.countercom+=1
        if command_name in self.commands:
            return self.commands[command_name].execute(args, self.vfs)
        else:
            print(f"Неизвестная команда: {command_name}")
            return True
    
    def run(self):
        self.running = True
        print("Welcome to VFS Console! Type 'exit' to quit.")
        
        while self.running:
            try:
            
                if sys.stdin.isatty():
                    user_input = input(self.vfs.get_prompt()).strip()
                else:
                    line=sys.stdin.readline()
                    if not line:
                        user_input="exit"
                    else:
                        user_input=line.strip()
                    print(f"{self.vfs.get_prompt()}{user_input}")
                if not user_input:
                    
                    continue
                
                command_name, args = self.parser.parse(user_input)
                self.running = self.execute_command(command_name, args)
                
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit")
            except Exception as e:
                print(f"Error: {e}")


