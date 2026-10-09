@echo off
setlocal
cd /d "%~dp0"
title Emergency Alert Packet Integrity Simulator
color 0b

echo =====================================================================
echo    EMERGENCY ALERT PACKET INTEGRITY SIMULATOR - CYBER COMMAND
echo =====================================================================
echo.
echo [1/2] Opening Dashboard in your default web browser...
echo.

:: Immediately launch the browser with the local index.html file
start "" "%~dp0index.html"

echo [2/2] Starting local telemetry HTTP server...
echo.

:: Try to launch python server
python -u server.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [NOTE] Python server exited or is not in PATH.
    echo The dashboard is already open directly in your web browser!
    echo You can use all simulator features directly without any server.
    echo.
)

pause
