@echo off
:loop
timeout /t 1200 >null 
if powercfg /getactivescheme eq S0 goto taskkill /f /im "speedfan" >null 
timeout /t 7 >null 
if powercfg /getactivescheme eq S0 goto start C:\Program Files (x86)\SpeedFan\speedfan.exe
goto loop
