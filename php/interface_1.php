<?php

interface I {
	const N = 1;
	function fun1();
	function fun2($n, $m);
}

class A implements I {
	function fun1(){}
	function fun2($a,$b) {
	}
}

$oa = new A();

echo "\n";
?>


