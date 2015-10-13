
<?php

$s=1999;
if (preg_match('/1999/', $s)) {
	  echo "party!\n";
}

preg_match('/lorem/i', "Lorem");

// 
$s = "do re mi mi mi";
$s = preg_replace('/mi/', "ma", $s);
echo $s;
echo "\n";

$s = "2010-06-03";
$rx = '/(\d{4})-(\d{2})-(\d{2})/';
preg_match($rx, $s, $m);
list($_, $yr, $mo, $dy) = $m;
echo $yr,$mo,$dy;
echo "\n";

?>

