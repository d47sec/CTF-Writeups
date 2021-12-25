<?php
session_start();
include "flag.php";
include "secret.php";

if(isset($_SESSION["user"])){
  if($_SESSION["user"]==="santa_claus ")  echo "".$flag;
}

class secret{
    public $yoursecret;
    public $descript;
    public $filename; 
     
    function __toString(){
        global $secret;
        $secret1 ="".$secret;
        return $secret1;
    }
    function __destruct(){
        global $secret;
        echo($this->yoursecret);
        if ("".$this->yoursecret === "".$secret) {
          $filename=str_replace(".", "", $this->filename);
          $filename=str_replace("/", "", $this->filename);
          file_put_contents("/tmp/".$filename, $this->descript); // sess_PHPSESSIONID  
        }   
    }
}
if (isset($_GET['ser'])) unserialize($_GET['ser']);
// echo(unserialize('O:6:"secret":4:{s:10:"yoursecret";r:1;s:8:"descript";s:25:"user|s:12:"santa_claus ";";s:8:"filename";s:37:"sess_eabe6fc0553da759da5383b2d5d24e9d";s:4:"name";s:12:"santa_claus ";}'));

// ChristCTF{Nô-en-Zui-zẻ-nhe!,Mấy-bạn-có-gấu-chưa-chứ-tui-có-gấu-rồi-đó}
?>
