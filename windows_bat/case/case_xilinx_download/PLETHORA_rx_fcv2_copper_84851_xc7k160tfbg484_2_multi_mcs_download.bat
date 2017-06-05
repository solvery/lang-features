@echo off

set mcs_name=PLETHORA_rx_fcv2_copper_84851_xc7k160tfbg484_2_multi

set cmd_file=%mcs_name%_mcs_download.cmd
set mcs_file=%mcs_name%.mcs
	
echo setMode -bs  > %cmd_file%
echo setMode -bs >> %cmd_file%
echo setMode -bs >> %cmd_file%
echo setMode -bs >> %cmd_file%
echo setCable -port auto >> %cmd_file%
echo Identify -inferir  >> %cmd_file%
echo identifyMPM  >> %cmd_file%
echo setCable -port usb21 -baud 12000000 >> %cmd_file%
echo attachflash -position 1 -spi "W25Q128FV" >> %cmd_file%
echo assignfiletoattachedflash -position 1 -file "%mcs_file%" >> %cmd_file%
echo Program -p 1 -dataWidth 1 -spionly -e -v -loadfpga  >> %cmd_file%
echo quit >> %cmd_file%

D:\Xilinx\14.7\ISE_DS\settings64.bat d:\Xilinx\14.7\ISE_DS\ISE\bin\nt64\impact.exe -batch %cmd_file%

pause
