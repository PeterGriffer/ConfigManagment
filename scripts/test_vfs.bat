@echo off
echo ========================================
echo ТЕСТИРОВАНИЕ VFS
echo ========================================
echo.

echo 1. Тестирование загрузки VFS...
load-vfs minimal.vfs.json

echo.
echo 2. Тестирование списка директорий...
ls
ls /home
ls /home/user

echo.
echo 3. Тестирование чтения файлов...
cat /home/user/readme.txt

echo.
echo 4. Тестирование навигации...
pwd
cd home
pwd
ls
cd user
pwd
ls

echo.
echo 5. Тестирование обработки ошибок...
ls /nonexistent
cat unknown_file.txt
cd /invalid/path

echo.
echo 6. Загрузка продвинутой VFS...
load-vfs advanced.vfs.json
ls
ls /users
ls /users/alice

echo.
echo ========================================
echo ТЕСТИРОВАНИЕ VFS ЗАВЕРШЕНО
echo ========================================
pause