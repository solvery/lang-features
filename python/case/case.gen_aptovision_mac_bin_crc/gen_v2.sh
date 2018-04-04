pn=6
num=10
python gen_apto_mac_1.py 		 $pn $num
python gen_icron_eeprom_mac_1.py $pn $num

mkdir -p apto_mac_address_Rx
mkdir -p apto_mac_address_Tx
mkdir -p icron_mac_address_Rx
mkdir -p icron_mac_address_Tx

mv icron_eeprom_tx_mac_*.bin icron_mac_address_Tx
mv icron_eeprom_rx_mac_*.bin icron_mac_address_Rx
mv apto_mac_fiber_tx*.bin apto_mac_address_Tx
mv apto_mac_fiber_rx*.bin apto_mac_address_Rx
cp ge_eeprom.py icron_mac_address_Tx
cp ge_eeprom.py icron_mac_address_Rx

mkdir v3p$pn\_$num
mv apto_mac_address* 	v3p$pn\_$num
mv icron_mac_address* 	v3p$pn\_$num

