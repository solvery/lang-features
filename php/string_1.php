
<?php
$word = "amet";

$s = <<<EOF
lorem ipsum
dolor sit $word
EOF;

$count = 3;
$item = "ball";
echo "$count ${item}s\n";

$fmt = "lorem %s %d %f";
sprintf($fmt, "ipsum", 13, 3.7);

$s = "Hello, ";
$s2 = $s . "World!";

$hbar = str_repeat("-", 80);

echo "value: " . 8 ."\n";
echo 7 + "12" ."\n";
echo 73.9 + ".037" ."\n";

?>

