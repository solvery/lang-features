@echo off

set bit_name=system_top

set cmd_file=%bit_name%_bit_download.cmd
set bit_file=%bit_name%.bit
	
echo setMode -bs  > %cmd_file%
echo setMode -bs >> %cmd_file%
echo setMode -bs >> %cmd_file%
echo setMode -bs >> %cmd_file%
echo setCable -port usb21 -baud -1 >> %cmd_file%
echo setCable -port usb21 -baud 12000000 >> %cmd_file%
echo Identify -inferir  >> %cmd_file%
echo identifyMPM  >> %cmd_file%
echo assignFile -p 1 -file  "%bit_file%" >> %cmd_file%
echo Program -p 1  >> %cmd_file%
echo quit >> %cmd_file%

D:\Xilinx\14.7\ISE_DS\settings64.bat d:\Xilinx\14.7\ISE_DS\ISE\bin\nt64\impact.exe -batch %cmd_file%

pause
