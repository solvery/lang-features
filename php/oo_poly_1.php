<?php

class A{}
class B extends A{}

$ob = new B();

if ($ob instanceof A) {
	echo "A\n";
}

if ($ob instanceof B) {
	echo "B\n";
}

echo "\n";
?>


