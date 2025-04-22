@echo off
setlocal

REM Display current directory for debugging
echo Current directory: %CD%

REM Check if testCases directory exists with full path
if not exist "%~dp0testCases" (
    echo Error: testCases directory not found!
    echo Script location: %~dp0
    echo Please create a testCases directory at: %~dp0testCases
    pause
    exit /b 1
)


REM Create Allure results directory if it doesn't exist
if not exist "%~dp0Reports\Allure_Results" mkdir "%~dp0Reports\Allure_Results"

REM Run pytest with Allure results output
python -m pytest -v -s "%~dp0testCases" --alluredir="%~dp0Reports\Allure_Results" --html="%~dp0Reports\report.html" --capture=tee-sys

if %ERRORLEVEL% NEQ 0 (
    echo Test execution failed
    pause
    exit /b 1
)

REM Generate and open Allure report
allure serve "%~dp0Reports\Allure_Results"
echo Test execution completed successfully !
exit /b 20
