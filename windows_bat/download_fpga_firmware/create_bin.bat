del *.mcs
del *.cfi
del *.prm

promgen -w -p bin -r header.hex -o header.bin
promgen -w -p bin -spi -s 8192 -u 010000 system_top.bit -u 400000 system_top.bit -o body.bin

type header.bin body.bin > Card45T_m.bin

del header.mcs
del body.mcs
del *.cfi
del *.prm

