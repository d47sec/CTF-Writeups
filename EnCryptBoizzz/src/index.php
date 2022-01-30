<?php

session_start();
@require_once 'config.php';

if (isset($_GET['debug'])) {
	show_source(__FILE__);
	die();
}

define('BLOCK_SIZE', 16);

function pad($string) {
	if (strlen($string) % BLOCK_SIZE === 0)
		$plaintext = $string;
	else  {
		$s = BLOCK_SIZE - strlen($string) % BLOCK_SIZE;
		$plaintext = $string.str_repeat(chr($s), $s);
	} 
	return $plaintext;
}
function encrypt($name) {
	global $auth_key, $key_for_enc; // from config.php with luv!!
	$method = 'AES-128-ECB';
	$plaintext = pad($name.$auth_key);
	return bin2hex(openssl_encrypt($plaintext, $method, $key_for_enc, OPENSSL_RAW_DATA));
}

if (isset($_GET["name"])) 
	$_SESSION["name"] = encrypt($_GET['name']);

if (isset($_GET['file'])) { // safe() in config.php, try to guess my filter =))
	if (safe($_GET['file'])) 
		@readfile($_GET['file']);
	else die("Dont hack me please =((((");
}

if (isset($_GET['auth_key'])) {
	if ($_GET['auth_key'] === $auth_key) {
		if ( isset($_GET["command"]) && strlen($_GET["command"]) <= 5)
			@system($_GET["command"]);
	}
	else echo "Wrong auth_key!!";
}
?>

<h1>Hello hacker ^>^ </h1>

<!-- 
// TODO: Remove 

<strong>To debug, use ?debug=hint </strong>
-->


<!-- 08df55ca911314204564a1c4c2f14689 ddef00dfaf0fc11ded05777122bec5c5 5fec0e7366a611d06db4ea75b91cedc3 -->

<!-- 1c775b734a214e2fe555c78082a08540 463d61e1141a49b22c448537df870c53 5fec0e7366a611d06db4ea75b91cedc3 -->