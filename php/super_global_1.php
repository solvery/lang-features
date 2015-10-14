
<?php

// global
$x = 1;
$y = 2;

function addition() {
	$GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y'];
}

addition();
echo $z;
echo "\n";

// _server
echo $_SERVER['PHP_SELF']; echo "\n";
echo $_SERVER['SCRIPT_NAME']; echo "\n";

echo "\n";
?>

