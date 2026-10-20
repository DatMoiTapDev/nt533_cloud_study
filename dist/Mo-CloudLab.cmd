@echo off
setlocal
title CloudLab - Local Offline
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-CloudLab.ps1"
if errorlevel 1 pause
endlocal
