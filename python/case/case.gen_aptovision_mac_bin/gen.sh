python gen_apto_mac_1.py  
python gen_icron_eeprom_mac_1.py

mkdir apto_mac_address
mkdir icron_mac_address

mv icron_eeprom_?x_mac_*.bin icron_mac_address
mv apto_mac_*.bin apto_mac_address
