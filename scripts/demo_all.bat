@echo off
echo ПОЛНАЯ ДЕМОНСТРАЦИЯ КОНСОЛИ VFS
echo ========================================

echo.
echo [РАЗДЕЛ 1: БАЗОВЫЕ КОМАНДЫ]
echo.
time
echo Привет из batch-скрипта!
conf-dump

echo.
echo [РАЗДЕЛ 2: ОПЕРАЦИИ С VFS]
echo.
echo Загрузка минимальной VFS...
load-vfs minimal.vfs.json
ls
cat /home/user/readme.txt

echo.
echo Загрузка базовой VFS...
load-vfs basic.vfs.json
ls
cd /home/user/documents
ls
cd project1
ls
cat main.py
pwd

echo.
echo [РАЗДЕЛ 3: ОБРАБОТКА ОШИБОК]
echo.
echo Тестирование ошибочных случаев...
load-vfs nonexistent.json
ls /invalid_path
cat unknown_file.txt
cd /bin/app.exe

echo.
echo [РАЗДЕЛ 4: ИНФОРМАЦИЯ О СИСТЕМЕ]
echo.
conf-dump

echo.
echo ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА!
pause