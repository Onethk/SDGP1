<?php
    $user1 = $_POST['user'];
    $pass1 = $_POST['pass'];

    $servername = "localhost"; 
    $username = "server_www"; 
    $password = "t2HoQKHjLAIGXQzt";
    $dbname = "SDGP";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);


    if($conn->connect_error){
        die('Connection Failed: '.$conn->connect_error);
    }else{
        $stmt = $conn->prepare("INSERT INTO login(username, password) VALUES (?,?)");
        $stmt->bind_param("ss",$user1,$pass1);
        $stmt->execute();
        echo "Success";
        $stmt->close();
        $conn->close();
    }


?>
