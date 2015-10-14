<?php

class A {
	private $v1 = 1;
	public $v2 = 2;
	protected $v3 = 3;

	public function m1($n) {
		echo $n; echo "\n";
	}
}

class B extends A {
	public $v4 = 4;
	public function m2($n) {
		echo $this-> v4; echo "\n";
		echo $this-> v3; echo "\n";
	}
}

$oa1 = new A();
$oa1->m1(1);

$ob1 = new B();
$ob1->m2(1);

echo "\n";
?>


