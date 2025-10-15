@echo off
echo ========================================
echo ДЕМОНСТРАЦИЯ BASE64 КОДИРОВАНИЯ В VFS
echo ========================================
echo.

echo 1. Загрузка VFS с base64 файлами...
load-vfs demo_base64.vfs.json

echo.
echo 2. Просмотр структуры...
ls
ls /text_files
ls /binary_data

echo.
echo 3. Демонстрация работы с ОБЫЧНЫМИ файлами:
echo.
cat /text_files/ordinary.txt

echo.
echo 4. Демонстрация работы с BASE64 файлами:
echo.
echo Файл: base64_encoded.txt
cat /text_files/base64_encoded.txt

echo.
echo Файл: english.bin
cat /binary_data/english.bin

echo.
echo Файл: russian.bin
cat /binary_data/russian.bin

echo.
echo 5. Проверка навигации по VFS:
echo.
cd /binary_data
pwd
ls
cd ../text_files
pwd
ls

echo.
echo ========================================
echo ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА!
echo Base64 кодирование работает корректно!
echo ========================================
pause