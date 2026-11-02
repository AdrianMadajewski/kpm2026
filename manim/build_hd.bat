@echo off
rem Renders every scene in 1080p60 and bundles prezentacja.html.
rem Run from the "manim" folder after installing (see README.md).
cd /d "%~dp0"
if exist .venv\Scripts\activate.bat call .venv\Scripts\activate.bat
python build.py --quality h
if errorlevel 1 (
    echo.
    echo Build failed - see the messages above.
    pause
    exit /b 1
)
echo.
echo Done: %~dp0prezentacja.html
pause
