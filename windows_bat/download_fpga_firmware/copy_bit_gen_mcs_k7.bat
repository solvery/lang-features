set /p file="file:"
del system_top.bit
copy %file% system_top.bit
D:\Xilinx\14.7\ISE_DS\ISE\bin\nt64\promgen -s 131072 -u 0 system_top.bit -spi -w -p mcs -o k7.mcs
