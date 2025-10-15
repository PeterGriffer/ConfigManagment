import time
import os
import sys
from commands import get_all_commands
from parser import Parser
from vfs import VFS

class Console:
    def __init__(self):
        self.running = False
        self.start_time = time.time()
        self.commands = {}
        self.countercom = 0
        self.vfs = VFS()
        self.vfs.console = self
        self.debug_mode = False
        self._register_commands()
    
    def _register_commands(self):
        commands = get_all_commands()
        for cmd in commands:
            self.commands[cmd.name] = cmd
    
    def get_uptime(self):
        uptime = time.time() - self.start_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def load_vfs_file(self, vfs_file):
        """Загрузка VFS файла (для использования из main.py)"""
        return self.vfs.load_vfs(vfs_file)
    
    def run_script_file(self, script_file):
        """Запуск скрипта (для использования из main.py)"""
        if not os.path.exists(script_file):
            # Проверяем в папке scripts
            scripts_dir = "scripts"
            script_path = os.path.join(scripts_dir, script_file)
            if os.path.exists(script_path):
                script_file = script_path
            else:
                print(f"Файл скрипта не найден: {script_file}")
                return False
        
        self.run_batch_script(script_file)
        return True
    
    def run_batch_script(self, script_file):
        """Выполнение bat скрипта"""
        if not os.path.exists(script_file):
            print(f"Batch-файл не найден: {script_file}")
            return
        
        if self.debug_mode:
            print(f"[ОТЛАДКА] Выполнение batch-скрипта: {script_file}")
        
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                
                if self.debug_mode:
                    print(f"[ОТЛАДКА] Строка {line_num}: '{line}'")
                
                # Пропускаем пустые строки и комментарии
                if not line:
                    continue
                    
                if (line.startswith('@') or 
                    line.startswith('rem ') or 
                    line.startswith('REM ') or
                    line.startswith('::')):
                    # Это комментарий - просто выводим его (без @)
                    if line.startswith('@'):
                        content = line[1:].strip()
                    elif line.startswith('rem '):
                        content = line[4:]
                    elif line.startswith('REM '):
                        content = line[4:]
                    else:
                        content = line[2:]
                    
                    if content:
                        print(content)
                    continue
                
                # Обрабатываем команды bat файла
                processed_line = self._process_bat_line(line)
                if processed_line:
                    print(f"{self.vfs.get_prompt()}{processed_line}")
                    self.process_command(processed_line)
                        
        except Exception as e:
            print(f"Ошибка выполнения batch-скрипта: {e}")
    
    def _process_bat_line(self, line):
        """Обработка строки BAT-файла и преобразование в команду VFS"""
        line_lower = line.lower()
        
        # Обработка echo
        if line_lower.startswith('echo '):
            content = line[5:].strip()
            if content.lower() == 'off':
                return None  # Пропускаем echo off
            elif content.lower() == 'on':
                return None  # Пропускаем echo on
            else:
                return f"echo {content}"
        
        elif line_lower.startswith('echo.'):
            print()  # Пустая строка
            return None
        
        # Обработка pause
        elif line_lower == 'pause':
            input("Нажмите Enter для продолжения...")
            return None
        
        # Обработка timeout
        elif line_lower.startswith('timeout'):
            try:
                parts = line.split()
                if len(parts) > 1:
                    seconds = int(parts[1])
                    print(f"Ожидание {seconds} секунд...")
                    time.sleep(seconds)
                else:
                    time.sleep(2)
            except:
                time.sleep(2)
            return None
        
        # Обработка cls/clear
        elif line_lower in ['cls', 'clear']:
            os.system('cls')
            return None
        
        # Обработка cd (может конфликтовать с нашей командой cd)
        elif line_lower.startswith('cd '):
            path = line[3:].strip()
            return f"cd {path}"
        
        # Все остальное считаем текстом для вывода или командой VFS
        else:
            # Если строка похожа на команду VFS, выполняем как есть
            parser = Parser()
            cmd_name, args = parser.parse(line)
            if cmd_name and cmd_name in self.commands:
                return line
            else:
                # Если это не команда VFS, выводим как текст
                print(line)
                return None
    
    def process_command(self, input_line):
        if self.debug_mode:
            print(f"[ОТЛАДКА] Обработка команды: '{input_line}'")
        
        parser = Parser()
        cmd_name, args = parser.parse(input_line)
        
        if cmd_name is None:
            return True
        
        self.countercom += 1
        
        if cmd_name in self.commands:
            return self.commands[cmd_name].execute(args, self.vfs)
        else:
            print(f"Команда не найдена: {cmd_name}")
            print("Введите 'help' для просмотра доступных команд")
            return True
    
    def run(self):
        self.running = True
        
        if not self.vfs.vfs_loaded:
            print("VFS не загружена. Используйте 'load-vfs <файл.json>' для загрузки виртуальной файловой системы.")
            print("Введите 'help' для просмотра доступных команд")
        
        while self.running:
            try:
                user_input = input(self.vfs.get_prompt()).strip()
                
                if not self.process_command(user_input):
                    self.running = False
                    
            except KeyboardInterrupt:
                print("\nИспользуйте 'exit' для выхода")
            except EOFError:
                print("\nИспользуйте 'exit' для выхода")
            except Exception as e:
                print(f"Ошибка: {e}")