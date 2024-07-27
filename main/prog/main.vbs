Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "venv\Scripts\activate.bat" & Chr(34), 0
Set WshShell = Nothing