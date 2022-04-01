<?php
$webRoot = $_SERVER['DOCUMENT_ROOT'];
$secretKey = file_get_contents("bí_mật_đừng_để_bị_mất.txt");

function createURLWithMac($params, $secretKey)
{
    $message = "";
    foreach ($params as $key => $value) {
        if ($key !== "mac")
            $message .= $key . $value;
    };
    $mac = md5($secretKey . $message);
    $url = "/access.php?" . http_build_query($params) . "&mac=" . $mac;
    return $url;
}

if (isset($_GET["source"])) {
    die(highlight_file("./access.php"));
}

?>

<!DOCTYPE html>
<html>
<meta charset=utf-8>
<title>SPOTTHEBUG #3</title>
<style>
    body {
        font-family: monospace;
        font-size: 20px;
    }
    table,
    th,
    td {
        border: 1px solid black;
        border-collapse: collapse;
    }

    th,
    td {
        padding: 5px;
        text-align: left;
    }
</style>

<body>

    <h2>SPOT THE BUG #3</h2>
    <p>Click the filename to access it</p>

    <table style="width:50%">
        <caption></caption>
        <tr>
            <th>Filename</th>
            <th>Allow Access</th>
        </tr>
        <tr>
            <td><?php echo "<a href='" . createURLWithMac(array("filename" => "hinh-con-meo.jpg"), $secretKey) . "'>hinh-con-meo.jpg</a>"; ?></td>
            <td>✅ Allow</td>
        </tr>
        <tr>
            <td><?php echo "<a href='" . createURLWithMac(array("filename" => "hinh-con-cho.jpg"), $secretKey) . "'>hinh-con-cho.jpg</a>"; ?></td>
            <td>✅ Allow</td>
        </tr>
        <tr>
            <td><a href='/access.php?filename=hinh-con-chim.jpg'>hinh-con-chim.jpg</a><br></td>
            <td>❌ Forbidden</td>
        </tr>
        <tr>
            <td><a href='/access.php?filename=meo-va-ban-gai.jpg'>meo-va-ban-gai.jpg</a></td>
            <td>❌ Forbidden</td>
        </tr>
    </table>
    <br>
    <p>View source code <a href="/?source=1">here</a></p>
</body>
</html>