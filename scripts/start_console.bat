@echo off
chcp 65001 >nul
cls
echo ================================
echo КОНСОЛЬ ВИРТУАЛЬНОЙ ФАЙЛОВОЙ СИСТЕМЫ
echo ================================
echo.
echo Доступные команды:
echo   python main.py --help
echo   python main.py --list-vfs
echo   python main.py --list-scripts
echo.
echo Быстрые примеры:
echo   python main.py --vfs basic.vfs.json
echo   python main.py --script demo_all.bat
echo   python main.py --vfs advanced.vfs.json --script test_vfs.bat
echo.
echo ================================

if "%1"=="" (
    echo Запуск интерактивного режима...
    echo.
    python main.py
) else (
    echo Выполнение с параметрами: %*
    echo.
    python main.py %*
)

pause