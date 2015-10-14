<?php

class A {
	private $v1 = 1;
	public $v2 = 2;
	protected $v3 = 3;

	public function m1($n) {
		echo $n;
	}
}

class B extends A {
	public $v4 = 4;
	public function m2($n) {
	}
}

echo "\n";
?>


