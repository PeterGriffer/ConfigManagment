import argparse
import sys
import os
from console import Console

def main():
    parser = argparse.ArgumentParser(
        description='Консоль виртуальной файловой системы',
        epilog='Пример: python main.py --vfs basic.vfs.json --script demo.bat'
    )
    
    # Основные параметры
    parser.add_argument(
        '--vfs', '-v',
        help='Загрузить VFS из JSON файла при запуске',
        metavar='ФАЙЛ_VFS'
    )
    
    parser.add_argument(
        '--script', '-s',
        help='Выполнить batch-скрипт при запуске',
        metavar='ФАЙЛ_СКРИПТА'
    )
    
    parser.add_argument(
        '--list-vfs', '-l',
        action='store_true',
        help='Показать доступные VFS файлы и выйти'
    )
    
    parser.add_argument(
        '--list-scripts',
        action='store_true',
        help='Показать доступные batch-скрипты и выйти'
    )
    
    parser.add_argument(
        '--verbose', '-V',
        action='store_true',
        help='Включить подробный вывод'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Отключить стартовый баннер'
    )
    
    # Параметры для отладки
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Включить режим отладки'
    )
    
    # Обработка обратной совместимости со старыми вызовами
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        sys.argv.insert(1, '--script')
    
    args = parser.parse_args()
    
    # Обработка специальных флагов
    if args.list_vfs:
        list_vfs_files()
        return
    
    if args.list_scripts:
        list_script_files()
        return
    
    # Создаем и настраиваем консоль
    console = Console()
    
    # Устанавливаем режим отладки
    if args.debug:
        console.debug_mode = True
        print("РЕЖИМ ОТЛАДКИ ВКЛЮЧЕН")
    
    # Загружаем VFS если указан
    if args.vfs:
        if not console.load_vfs_file(args.vfs):
            print(f"Ошибка загрузки VFS: {args.vfs}")
            sys.exit(1)
    
    # Запускаем скрипт если указан
    if args.script:
        if not console.run_script_file(args.script):
            print(f"Ошибка выполнения скрипта: {args.script}")
            sys.exit(1)
    
    # Запускаем интерактивный режим если не было скрипта
    if not args.script:
        if not args.no_banner:
            print_banner()
        console.run()

def list_vfs_files():
    """Показать доступные VFS файлы"""
    vfs_dir = "vfs_files"
    print("Доступные VFS файлы:")
    print("-" * 40)
    
    if os.path.exists(vfs_dir):
        for file in os.listdir(vfs_dir):
            if file.endswith('.json'):
                file_path = os.path.join(vfs_dir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        import json
                        data = json.load(f)
                        name = data.get('name', 'Неизвестно')
                        desc = data.get('description', 'Нет описания')
                        print(f"  {file:20} - {name}")
                        print(f"  {'':20}   {desc}")
                except:
                    print(f"  {file:20} - [Ошибка чтения файла]")
                print()
    else:
        print("  Папка vfs_files не найдена")

def list_script_files():
    """Показать доступные скрипты"""
    scripts_dir = "scripts"
    print("Доступные batch-скрипты:")
    print("-" * 40)
    
    if os.path.exists(scripts_dir):
        for file in os.listdir(scripts_dir):
            if file.endswith('.bat'):
                print(f"  {file}")
    else:
        print("  Папка scripts не найдена")

def print_banner():
    """Показать баннер при запуске"""
    banner = """
╔══════════════════════════════════════════════╗
║                КОНСОЛЬ ВФС                   ║
║                 Версия 1.0                   ║
╚══════════════════════════════════════════════╝
"""
    print(banner)

if __name__ == "__main__":
    main()