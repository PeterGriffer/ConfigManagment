Эмулятор командной строки с виртуальной файловой системой в памяти. Загружает структуру файлов из JSON, поддерживает базовые UNIX-команды и выполнение скриптов.

Навигация: ls, cd, pwd
Файлы: cat, touch, uniq
Система: who, time, echo, help, conf-dump
Управление: load-vfs, run, exit

Формат VFS: JSON файлы с поддержкой base64 для бинарных данных.

Установка не требуется - чистый Python

Запуск интерактивного режима
python main.py

Запуск с VFS
python main.py --vfs basic.vfs.json

Запуск скрипта
python main.py --script demo.bat

Показать справку
python main.py --help

Список доступных VFS
python main.py --list-vfs

Пример вывода в пц интерактивном режиме
[VFS:БазоваяVFS /]$ ls
[VFS:БазоваяVFS /]$ cd /home/user
[VFS:БазоваяVFS /home/user]$ cat readme.txt
[VFS:БазоваяVFS /home/user]$ touch newfile.txt
[VFS:БазоваяVFS /home/user]$ who