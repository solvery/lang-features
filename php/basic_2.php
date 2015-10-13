
<?php
// variable
{
	$v = NULL;
	$a = [];
	$d = [];
	$x = 1;
	list($y, $z) = [2, 3];
}
{
	list($g1, $g2) = [7, 8];

	function swap_globals() {
		global $g1, $g2;
		list($g1, $g2) = [$g2, $g1];
	}
}
{
	define("PI", 3.14);
	/// const PI = 3.14;
}
{
	list($x, $y, $z) = [1 ,2, 3];
	// 3 is discarded:
	list($x, $y) = [1, 2, 3];
	// z set to null
	/// list($x, $y, $z) = [1, 2];
}
{
	$x = 1;
	$y = ++$x;
	$z = --$y;
	$x > 0 ? $x : -$x;
}
{
	min(1, 2, 3);
	max(1, 2, 3);
	$a = [1, 2, 3];
	min($a);
	max($a);
}
?>
