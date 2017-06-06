setMode -bs
setCable -port auto
Identify -inferir 
identifyMPM 
setCable -port usb21 -baud 12000000
attachflash -position 1 -spi "W25Q128FV"
assignfiletoattachedflash -position 1 -file "k7.mcs"
Program -p 1 -dataWidth 2 -spionly -e -v -loadfpga 
quit