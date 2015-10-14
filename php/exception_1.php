<?php

class Bam extends Exception
{
	function __construct()
	{
		parent::__construct("bam!");
	}
}

try {
	throw new Bam;
} catch (Bam $e) {
	echo $e->getMessage(), "\n";
}

echo "\n";
?>



