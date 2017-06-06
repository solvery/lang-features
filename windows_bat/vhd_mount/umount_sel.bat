 
set /p filename="file:"
echo select vdisk file=F:\yaowu\%filename% > vhdsel
echo detach vdisk  >> vhdsel
diskpart /s vhdsel
del /f /q vhdsel
 
