<?php
    include("connection.php");

    if(isset($_POST['submit'])){


        $username = $_POST['user'];
        $password = $_POST['pass']; 

        $sql = "SELECT * FROM login where username='$username' and password='$password' ";
        $result = mysqli_query($conn, $sql);
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
        $count = mysqli_num_rows($result);
        echo "hello";

        if($count==1){
            header("Location:welcome.php");

        }else{
            echo '<script>
            window.location.href = "index1.php";
            alert("Login failed. Invalid username or password !!!");
            </script>';
            

        }
    

    }

    


?>