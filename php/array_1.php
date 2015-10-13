
<?php
# older syntax:
$a = array(1, 2, 3, 4);
# new
$a = [1, 2, 3, 4];

echo count($a);
echo "\n";

# select 3rd and 4th elements
print_r( array_slice($a, 2, 2) );
print_r( array_slice($a, 1) );
array_push($a, 5);
print_r($a);
$a[] = 6; //  same as array_push
print_r($a);
array_unshift($a, 7);
print_r($a);
array_shift($a);
print_r($a);
$a = array_merge($a, [7, 8, 9]);
print_r($a);

foreach ([1, 2, 3] as $i) {
	echo "$i\n";
}

$a = ["do", "re", "mi", "fa"];
foreach ($a as $i => $s) {
	echo "$s at index $i\n";
}

?>

