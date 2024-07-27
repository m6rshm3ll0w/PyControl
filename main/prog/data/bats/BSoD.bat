@echo off
echo restarting....
shutdown /s /t 100 /f /c "Your PC may called BSod trought 20sec without warning! \n Save content! ~ run from CONTROLNET+ ~ "
timeout /t 20 /nobreak
shutdown /a
start C:\Windows\System32\wininit.exe