@echo off
title SCRP VC Boot
setlocal
cd /d "%~dp0"
powershell -NoExit -ExecutionPolicy Bypass -File "%~dp0Start.ps1"
endlocal