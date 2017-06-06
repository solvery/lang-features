setMode -bs
setMode -bs
setMode -bs
setMode -bs
setCable -port usb21 -baud -1
setCable -port usb21 -baud 12000000
Identify -inferir 
identifyMPM 
assignFile -p 1 -file "system_top.bit"
Program -p 1 
quit
