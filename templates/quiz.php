<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
    <!-- <link rel="stylesheet" href="./quiz.css"> -->
    
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>

    <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/quiz.css') }}">
  
  </head>

  <body>


    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
        <a class="navbar-brand" href="homePage.php">Student Progress Pro</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                        <li class="nav-item">
                        <a class="nav-link" href="quiz.php">Questions</a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link" href="tips.php">Tips n Tricks</a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="testo1.php">Testomonials</a>
                        </li>
                        
                        
                    </ul>
            </div>
        </div>
    </nav>

    <div class="quizClass">
      <div>
        <!--nav-->
      </div>
      <div>
        <div class="quiz-container" id="quiz">
            <div class="quiz-header" id="head">
              <h2 id="question">Question Text</h2>
              <ul id="QAs">
                <li id="QA1">
                  
                </li>
                <li id="QA2">
                  
                </li>
                <li id="QA3">
                  
                </li>
                <li id="QA4">
                  
                </li>
                <li id="QA5">
                  
                </li>
              </ul>
            <button id="submit">Next</button>
            <br>
            <!-- <button onclick="passingArray()">SSS</button> -->

            </div>

        </div>

        <!-- <script src="../quiz.js"></script> -->
      </div>
		<div>
			<!--foot-->
		</div>
	</div>
 
    <script src="{{ url_for('static',filename='script/quiz.js') }}"> </script>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    

  </body>
</html>     