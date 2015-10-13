<?php

$n = 0;

if ( 0 == $n ) {
	echo "no hits\n";
} elseif ( 1 == $n ) {
	echo "one hit\n";
} else {
	echo "$n hits\n";
}

switch ($n) {
	case 0:
		echo "no hits\n";
		break;
	case 1:
		echo "one hit\n";
		break;
	default:
		echo "$n hits\n";
}

while ( $i < 100 ) { $i++; }

for ($i = 1; $i <= 10; $i++) {
	echo "$i\n";
}

echo "\n";
?>


