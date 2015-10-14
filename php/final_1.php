
<?php

class S {
	static $n = 1;
	public $m = 10;
	const J = 100;
	public function getj(){
		echo self::J;
	}
	static function getm(){
		echo $this->$m;
	}
	static function getn(){
		echo self::$n;
		echo self::J;
	}
}

echo S::$n;
S::getn();
$s = new S();
$s->getj();

echo "\n";
?>

