import time
import platform
import datetime
import sys
import os


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
        print("Выполнение команды lc с аргументами: ", args)
        return True


class CdCommand(Command):
    def __init__(self):
        super().__init__(name="cd", description="Сменить директорию")

    def execute(self, args, vfs):
        print("Выполнение команды cd с аргументами:", args)
        return True


class ExitCommand(Command):
    def __init__(self):
        super().__init__(name="exit", description="Exit console")

    def execute(self, args, vfs):
        print("Goodbye!")
        return False


class ConfDumpCommand(Command):
    def __init__(self):
        super().__init__(name="conf-dump", description="Информация для разработчика")

    def execute(self, args, vfs):
        print("╔══════════════════════════════════════╗")
        print("║           ТЕКУЩИЕ ПАРАМЕТРЫ          ║")
        print("╠══════════════════════════════════════╣")
        print("Файловая система - ", vfs.name)
        if hasattr(vfs, "console"):
            print(f"Версия Python: {sys.version.split()[0]}")
            print(f"Платформа: {platform.platform()}")
            print(f"Текущее время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("Время работы - ", vfs.console.get_uptime())
            print("Состояние консоли - ", "Работает" if vfs.console.running else "Не работает")
            print("Количество комманд - ", len(vfs.console.commands))
            print("Количество обращений к консоли - ", vfs.console.countercom)
        print("╚══════════════════════════════════════╝")
        return True


class EchoCommand(Command):
    def __init__(self):
        super().__init__(name="echo", description="Display message")

    def execute(self, args, vfs):
        print(" ".join(args))
        return True


class TimeCommand(Command):
    def __init__(self):
        super().__init__(name="time", description="Show current time")

    def execute(self, args, vfs):
        print(f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
        return True


class HelpCommand(Command):
    def __init__(self):
        super().__init__(name="help", description="Show available commands")

    def execute(self, args, vfs):
        print("Available commands:")
        for cmd_name, cmd in vfs.console.commands.items():
            print(f"  {cmd_name:12} - {cmd.description}")
        return True


class PromptCommand(Command):
    def __init__(self):
        super().__init__(name="prompt", description="Change prompt format")

    def execute(self, args, vfs):
        if args:
            new_prompt = " ".join(args) + " "
            vfs.set_prompt(new_prompt)
            print(f"Prompt changed to: {new_prompt}")
        else:
            print("Current prompt:", vfs.get_prompt())
        return True


class RunCommand(Command):
    def __init__(self):
        super().__init__(name="run", description="Run batch script (.bat file)")

    def execute(self, args, vfs):
        if not args:
            print("Usage: run <script.bat>")
            return True

        script_file = args[0]
        if not script_file.endswith('.bat'):
            script_file += '.bat'

        # Проверяем в папке scripts
        scripts_dir = "scripts"
        script_path = os.path.join(scripts_dir, script_file)

        if not os.path.exists(script_file) and not os.path.exists(script_path):
            print(f"Script file not found: {script_file}")
            print(f"Also checked in {scripts_dir}/ directory")
            return True

        # Используем путь где нашли файл
        if os.path.exists(script_file):
            actual_script = script_file
        else:
            actual_script = script_path

        print(f"Executing batch script: {actual_script}")
        vfs.console.run_batch_script(actual_script)
        return True


# Функция для получения всех команд
def get_all_commands():
    return [
        LcCommand(), CdCommand(), ExitCommand(),
        ConfDumpCommand(), EchoCommand(), TimeCommand(),
        HelpCommand(), PromptCommand(), RunCommand()
    ]