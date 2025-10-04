@echo off
rem ========================================
rem VFS DEMONSTRATION SCRIPT
rem ========================================
echo.
echo Запуск скрипта демонстрации...

rem Выполняем команды VFS
lc /home/user/documents
cd /var/log
conf-dump
help

echo.
echo Демонстрация завершена!
pause