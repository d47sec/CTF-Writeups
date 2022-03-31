<?php
    /* access.php source code */

    $secretKey = file_get_contents("bí_mật_đừng_để_bị_mất.txt");
    $message = "";
    foreach ($_GET as $key => $value) {
        if ($key !== "mac")
            $message .= $key . $value;
    };

    if ($_GET["mac"] === md5($secretKey . $message)) {
        $fileContent = file_get_contents(
            "cbjs-static/" . $_GET["filename"]
        );
        echo "<img src='data:image/jpeg;base64," . base64_encode($fileContent) . "'>";
    } else {
        echo "403 Forbidden!";
    }
?>


1