
set /p hour="hour:"
set /a delay=%hour%*3600

shutdown -s -t %delay%

pause
shutdown -a 

pause