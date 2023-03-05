<?php

    include("connection.php");

    if(isset($_POST['create'])){

        $userName = $_POST['user'];
        $password = $_POST['pass'];

        $checkSQL = "SELECT username FROM login";
        $exeSQL = mysqli_query($conn, $checkSQL) or die(mysqli_error($conn));

        $noEmail = TRUE;

        while ($arrayp = mysqli_fetch_array($exeSQL)){
            if($arrayp['username'] == $userName){

                $noEmail = FALSE;

                echo  '<script>
                        window.location.href = "signup1.php";
                        alert("Email Address Already Registered! Please Login In");
                    </script>';
            }
        }
        
        if($noEmail){
            $sql = "INSERT INTO login (username, password) VALUES ('$username', '$password')";

            if (mysqli_query($conn, $sql)) {
                echo  '<script> 
                        window.location.href = "login1.php";
                        alert("Account create successfully!!!") 
                       </script>';
            } else {
                echo "Error: " . $sql . ":-" . mysqli_error($conn);
            }
            mysqli_close($conn);
        }
        
    }
?>