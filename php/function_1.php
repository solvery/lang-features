<?php

function add3($x1, $x2, $x3)
{
	return $x1 + $x2 + $x3;
}

add3(1, 2, 3);
# function names are case insensitive:
ADD3(1, 2, 3);

function my_log($x, $base=10)
{
	return log($x) / log($base);
}

my_log(42);
my_log(42, M_E);

function first_and_last()
{

	$arg_cnt = func_num_args();

	if ($arg_cnt >= 1) {
		$n = func_get_arg(0);
		echo "first: " . $n . "\n";
	}

	if ($arg_cnt >= 2) {
		$a = func_get_args();
		$n = $a[$arg_cnt-1];
		echo "last: " . $n . "\n";
	}
}

$a = [1, 2, 3];

call_user_func_array("add3", $a);

function first_and_second(&$a)
{
	return [$a[0], $a[1]];
}

$a = [1, 2, 3];
list($x, $y) =
first_and_second($a);

$sqr = function ($x) {
	return $x * $x;
};

$sqr(2);

$func = "add";

function counter()
{
	static $i = 0;
	return ++$i;
}

echo counter();

function make_counter()
{
	$i = 0;
	return function () use (&$i) {
		return ++$i;
	};
}

$nays = make_counter();
echo $nays();

# PHP 5.5:
function make_counter2() {
	$i = 0;
	while (1) {
		yield ++$i;
	}
}

$nays = make_counter2();
# does not return a value:
$nays->next();
# runs generator if generator has not
# yet yielded:
echo $nays->current();

echo "\n";
?>


