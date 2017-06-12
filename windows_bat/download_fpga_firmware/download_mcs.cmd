setMode -bs
setMode -bs
setMode -bs
setMode -bs
setCable -port auto
Identify -inferir 
identifyMPM 
setCable -port usb21 -baud 12000000
attachflash -position 1 -spi "M25P64"
assignfiletoattachedflash -position 1 -file "45t_pcard.mcs"
Program -p 1 -dataWidth 1 -spionly -e -v -loadfpga 
quit
