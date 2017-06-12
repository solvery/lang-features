
set elf_file="data/pcard_sw.elf"

cd ../edk
data2mem -bm "implementation/system_bd" -p xc6slx45tcsg324-2 -bt "implementation/system.bit"  -bd %elf_file% tag microblaze_0  -o b implementation/download.bit
copy /b /y implementation\download.bit ..\ise\system_top.bit

pause
