@echo off
echo [ABYSSAL TERMINAL v666]
echo Initializing dark server...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERR] Python not found. Install Python 3.8+ and retry.
    pause
    exit /b 1
)

REM Check if dependencies exist, install if not
python -c "import fastapi, uvicorn" >nul 2>&1
if errorlevel 1 (
    echo [INIT] Installing dependencies...
    pip install fastapi uvicorn
)

echo [OK] Dependencies satisfied.
echo [INIT] Binding to 127.0.0.1:6666...
echo.
echo Open browser: http://127.0.0.1:6666
echo Press Ctrl+C to terminate.
echo.

python main.py
