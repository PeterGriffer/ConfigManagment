@echo off
echo ========================================
echo ТЕСТИРОВАНИЕ ЭТАП 5: ДОПОЛНИТЕЛЬНЫЕ КОМАНДЫ
echo ========================================
echo.

echo 1. Загрузка VFS...
load-vfs basic.vfs.json

echo.
echo 2. Тестирование TOUCH...
echo Текущая директория:
pwd
ls
echo Создание файлов...
touch newfile1.txt
touch newfile2.txt
echo После создания:
ls

echo.
echo 3. Создание в поддиректории...
cd /home/user
pwd
ls
touch document3.txt
echo После создания в поддиректории:
ls

echo.
echo 4. Тестирование обработки ошибок...
touch /invalid_path/file.txt
touch existing_file.txt
touch existing_file.txt

echo.
echo 5. Проверка созданных файлов...
echo Содержимое нового файла:
cat newfile1.txt
cat document3.txt

echo.
echo ========================================
echo ТЕСТИРОВАНИЕ ЭТАП 5 ЗАВЕРШЕНО
echo ========================================
pause