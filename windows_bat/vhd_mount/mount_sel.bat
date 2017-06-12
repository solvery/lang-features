 
set /p filename="file:"
echo select vdisk file=F:\yaowu\%filename% > vhdsel
echo attach vdisk  >> vhdsel
diskpart /s vhdsel
del /f /q vhdsel
 
