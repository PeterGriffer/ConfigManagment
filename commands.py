import time
import platform
import datetime
import sys
import os
import getpass


class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def execute(self, args, vfs):
        pass


class LsCommand(Command):
    def __init__(self):
        super().__init__(name="ls", description="Список содержимого директории")

    def execute(self, args, vfs):
        path = args[0] if args else None
        result = vfs.list_directory(path)
        print(result)
        return True


class CdCommand(Command):
    def __init__(self):
        super().__init__(name="cd", description="Сменить директорию")

    def execute(self, args, vfs):
        if not args:
            # cd без аргументов - переход в корень
            result = vfs.change_directory("/")
        else:
            result = vfs.change_directory(args[0])

        if result != True:
            print(result)
        return True


class UniqCommand(Command):
    def __init__(self):
        super().__init__(name="uniq", description="Убрать повторяющиеся строки из файла")

    def execute(self, args, vfs):
        if not args:
            print("Использование: uniq <файл>")
            return True

        content = vfs.read_file(args[0])
        if content.startswith("Файл не найден") or content.startswith("Не файл"):
            print(content)
            return True

        # Убираем повторяющиеся строки
        lines = content.split('\n')
        seen = set()
        unique_lines = []

        for line in lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

        print('\n'.join(unique_lines))
        return True


class WhoCommand(Command):
    def __init__(self):
        super().__init__(name="who", description="Показать текущего пользователя")

    def execute(self, args, vfs):
        try:
            username = getpass.getuser()
            print(f"Текущий пользователь: {username}")
            print(f"Платформа: {platform.system()}")
            print(f"Время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        except:
            print("Не удалось определить пользователя")
            print(f"Платформа: {platform.system()}")
        return True


class TouchCommand(Command):
    def __init__(self):
        super().__init__(name="touch", description="Создать пустой файл")

    def execute(self, args, vfs):
        if not args:
            print("Использование: touch <имя_файла>")
            return True

        filename = args[0]
        result = vfs.create_file(filename)
        if result == True:
            print(f"Файл создан: {filename}")
        else:
            print(result)
        return True


class CatCommand(Command):
    def __init__(self):
        super().__init__(name="cat", description="Показать содержимое файла")

    def execute(self, args, vfs):
        if not args:
            print("Использование: cat <имя_файла>")
            return True

        result = vfs.read_file(args[0])
        print(result)
        return True


class ExitCommand(Command):
    def __init__(self):
        super().__init__(name="exit", description="Выйти из консоли")

    def execute(self, args, vfs):
        print("До свидания!")
        return False


class ConfDumpCommand(Command):
    def __init__(self):
        super().__init__(name="conf-dump", description="Внутренняя информация для разработчика")

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
            print("Количество команд - ", len(vfs.console.commands))
            print("Количество обращений к консоли - ", vfs.console.countercom)
        print("╚══════════════════════════════════════╝")
        return True


class EchoCommand(Command):
    def __init__(self):
        super().__init__(name="echo", description="Вывести сообщение")

    def execute(self, args, vfs):
        print(" ".join(args))
        return True


class TimeCommand(Command):
    def __init__(self):
        super().__init__(name="time", description="Показать текущее время")

    def execute(self, args, vfs):
        print(f"Текущее время: {datetime.datetime.now().strftime('%H:%M:%S')}")
        return True


class HelpCommand(Command):
    def __init__(self):
        super().__init__(name="help", description="Показать доступные команды")

    def execute(self, args, vfs):
        print("Доступные команды:")
        for cmd_name, cmd in vfs.console.commands.items():
            print(f"  {cmd_name:12} - {cmd.description}")
        return True


class RunCommand(Command):
    def __init__(self):
        super().__init__(name="run", description="Запустить batch-скрипт")

    def execute(self, args, vfs):
        if not args:
            print("Использование: run <скрипт.bat>")
            return True

        script_file = args[0]
        if not script_file.endswith('.bat'):
            script_file += '.bat'

        scripts_dir = "scripts"
        script_path = os.path.join(scripts_dir, script_file)

        if not os.path.exists(script_file) and not os.path.exists(script_path):
            print(f"Файл скрипта не найден: {script_file}")
            print(f"Также проверено в папке {scripts_dir}/")
            return True

        if os.path.exists(script_file):
            actual_script = script_file
        else:
            actual_script = script_path

        print(f"Выполнение batch-скрипта: {actual_script}")
        vfs.console.run_batch_script(actual_script)
        return True


class LoadVFSCommand(Command):
    def __init__(self):
        super().__init__(name="load-vfs", description="Загрузить виртуальную файловую систему")

    def execute(self, args, vfs):
        if not args:
            print("Использование: load-vfs <файл_vfs.json>")
            return True

        vfs_file = args[0]
        if not vfs_file.endswith('.json'):
            vfs_file += '.json'

        vfs_dir = "vfs_files"
        vfs_path = os.path.join(vfs_dir, vfs_file)

        if not os.path.exists(vfs_file) and not os.path.exists(vfs_path):
            print(f"VFS файл не найден: {vfs_file}")
            print(f"Также проверено в папке {vfs_dir}/")
            return True

        if os.path.exists(vfs_file):
            actual_vfs = vfs_file
        else:
            actual_vfs = vfs_path

        return vfs.load_vfs(actual_vfs)


class PwdCommand(Command):
    def __init__(self):
        super().__init__(name="pwd", description="Показать текущую директорию")

    def execute(self, args, vfs):
        print(vfs.get_current_path())
        return True


def get_all_commands():
    return [
        LsCommand(), CdCommand(), UniqCommand(), WhoCommand(),  # Этап 4
        TouchCommand(),  # Этап 5
        CatCommand(), ExitCommand(), ConfDumpCommand(), EchoCommand(),
        TimeCommand(), HelpCommand(), RunCommand(), LoadVFSCommand(), PwdCommand()
    ]