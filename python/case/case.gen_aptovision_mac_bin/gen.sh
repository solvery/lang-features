python gen_apto_mac_1.py 		 4 12
python gen_icron_eeprom_mac_1.py 4 12

mkdir -p apto_mac_address
mkdir -p icron_mac_address

mv icron_eeprom_?x_mac_*.bin icron_mac_address
mv apto_mac_*.bin apto_mac_address
