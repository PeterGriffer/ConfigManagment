@echo off
echo ========================================
echo ТЕСТИРОВАНИЕ ЭТАП 4: ОСНОВНЫЕ КОМАНДЫ
echo ========================================
echo.

echo 1. Загрузка VFS...
load-vfs basic.vfs.json

echo.
echo 2. Тестирование LS...
echo Текущая директория:
ls
echo.
echo Корневая директория:
ls /
echo.
echo Директория home:
ls /home

echo.
echo 3. Тестирование CD...
echo Текущий путь:
pwd
echo Переход в home...
cd home
pwd
ls
echo Переход в user...
cd user
pwd
ls
echo Переход в корень...
cd /
pwd

echo.
echo 4. Тестирование UNIQ...
echo Создание тестового файла с повторениями...
echo Создайте файл test_uniq.txt с содержимым:
echo line1
echo line2
echo line1
echo line3
echo line2
echo Тестирование uniq:
cat /home/user/documents/test_uniq.txt
echo.
echo После uniq:
uniq /home/user/documents/test_uniq.txt

echo.
echo 5. Тестирование WHO...
who

echo.
echo 6. Тестирование обработки ошибок...
ls /nonexistent
cd /invalid_directory
uniq unknown_file.txt

echo.
echo ========================================
echo ТЕСТИРОВАНИЕ ЭТАП 4 ЗАВЕРШЕНО
echo ========================================
pause