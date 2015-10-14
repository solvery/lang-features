<?php

abstract class C1 {
	abstract function fun1();
	abstract function fun2($n, $m);
}

class C2 extends C1 {
	public function fun1(){}
	public function fun2($a, $b){
		return $a . $b;
	}
}

$oc1 = new C2();

echo "\n";
?>


