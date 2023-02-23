<?php
    include("sign.php")
?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" type="text/css" href="style1.css"/>

</head>

<body>
    

    <div class="container">
        <div id="form">
            <h1 id="login-h1">Login to your account</h1>
            <form name="form" method="POST" id="form-inside" action="login.php" onsubmit="return isvalid()">
                <label class="us_pw">Username</label>
                <input type="text" id="user" name="user" class="loginInputs" size="20">
                
                <br><br>
                <label class="us_pw">Password</label>
                <input type="password" id="pass" name="pass" class="loginInputs" size="21">
                <br>
                <br>
                <br>
                <input type="submit" value="Login" name="submit" id="loginButton">
                <!-- <button class="loginButton">Login</button> -->

            </form>
        </div>

        <div class="image1">
            <img src="images/image2.avif" alt="" height=450px width=450px >
            </div>

    </div>

    <script>
        function isvalid(){



            var user = document.form.user.value;
            var pass = document.form.pass.value;

            if(user.length=="" && pass.length==""){
                alert("Username and password field is empty!");
                return false;
            }else{
                if(user.length==""){
                    alert("Username is empty!");
                    return false;
                }
                if(pass.length==""){
                    alert("Password is empty!");
                    return false;
                }
            
            }
            
        }
    </script>

    





    
</body>
</html>