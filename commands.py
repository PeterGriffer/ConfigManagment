import time
import platform
import datetime
import sys

class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def execute(self, args, vfs):
        pass
#
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

class ConfDumpCommand(Command):
    def __init__(self):
        super().__init__(name="conf-dump", description="inside information for developer")
    def execute(self, args, vfs):
         print("╔══════════════════════════════════════╗")
         print("║           ТЕКУЩИЕ ПАРАМЕТРЫ          ║")
         print("╠══════════════════════════════════════╣")
         print("Файловая система - ", vfs.name)
         if hasattr(vfs,"console"):
             
             print(f"Версия Python: {sys.version.split()[0]}")
             print(f"Платформа: {platform.platform()}")
             print(f"Текущее время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") 
             print("Время работы - ", vfs.console.get_uptime())
             print("Состояние консоли - ","Работает" if vfs.console.running else "Не работает")
             print("Количество комманд - ",len(vfs.console.commands))
             print("Количество обращений к консоли - ", vfs.console.countercom)
            
            

         print("╔══════════════════════════════════════╗")
         print("║                                      ║")
         print("╠══════════════════════════════════════╣")
         return True