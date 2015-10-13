
<?php

# older syntax:
$d = array("t" => 1, "f" => 0);
$d = ["t" => 1, "f" => 0];

print_r($d);
print $d["t"];
$d["t"] = 2;

$d1 = ["a" => 1, "b" => 2];
$d2 = ["b" => 3, "c" => 4];
$d1 = array_merge($d1, $d2);
print_r($d1);

foreach ($d as $k => $v) {
	echo $k, $v;
}

array_keys($d);
array_values($d);

asort($d);
foreach ($d as $k => $v) {
	print "$k: $v\n";
}

echo "\n";
?>


