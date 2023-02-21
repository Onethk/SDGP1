const quizData = [
    {
        question: "Time taken to travel to the university?",
        a: "Less than 15 minutes",
        b: "Less than 30 minutes",
        c: "Less than 1 hour",
        d: "More than 1 hour",
        e: "answer",
        
    },
    {
        question: "Do you do any part time job ?",
        a: "Yes",
        b: "No",
        c: "answer",
        d: "answer",
        e: "answer",
        
    },
    {
        question: "Are you in a relationship ?",
        a: "Yes",
        b: "No",
        c: "answer",
        d: "answer",
        e: "answer",
        
    },
    {
        question: "Father's education ?",
        a: "Primary school (grade 1 - 5)",
        b: "Secondary school (grade 6 - 12)",
        c: "Holds a degree",
        d: "answer",
        e: "answer", 
        
    },
    {
        question: "Mother's education ?",
        a: "Primary school (grade 1 - 5)",
        b: "Secondary school (grade 6 - 12)",
        c: "Holds a degree",
        d: "answer", 
        e: "answer",
      
    },
    {
        question: "Daily study hours ?",
        a: "Less than 1 hour",
        b: "Less than 2 hours",
        c: "Less than 5 hours",
        d: "More than 5 hours",
        e: "none", 
        
    },
    {
        question: "How often do you attend lectures and tutorials ?",
        a: "Always",
        b: "Sometimes",
        c: "Never",
        d: "answer", 
        e: "answer",
        
    },
    {
        question: "How often do you concentrate and listen during the lecture?",
        a: "Always",
        b: "Sometimes",
        c: "Never",
        d: "answer",
        e: "answer",
        
    },
    {
        question: "Do you have any friends who help in your studies?",
        a: "Yes",
        b: "No",
        c: "answer",
        d: "answer", 
        e: "answer",
        
    },
    {
        question: "How often do you spend time on social media?",
        a: "Less than 1 hour",
        b: "Less than 2 hours",
        c: "More than 2 hours",
        d: "None", 
        e: "answer",
        
    },
    {
        question: "Do you spend time on any extra curricular activity (sports, clubs)?",
         a: "Yes",
        b: "No",
        c: "answer",
        d: "answer",
        e: "answer",  
        
    },
    {
        question: "How far in ahead of the tests do you start studying?",
        a: "Closest date to the exam",
        b: "I study regularly",
        c: "answer",
        d: "answer",
        e: "answer", 
        
    },
];
const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const e_text = document.getElementById('e_text')
const submitBtn = document.getElementById('submit')
const outputs=[];
let currentQuiz = 0
let score = 0
loadQuiz()
function loadQuiz() {
    deselectAnswers()
    const currentQuizData = quizData[currentQuiz]
    questionEl.innerText = currentQuizData.question
    
    if (currentQuizData.a !="answer") {
    	document.getElementById("QA1").innerHTML +="<div id='ansDiv1'><input type='radio' name='answer' id='a' class='answer'><label for='a' id='a_text'>"+currentQuizData.a+"</label></div>";   	
    }else{
    	document.getElementById("QA1").innerHTML +="<div id='ansDiv1'></div>";
    }
    

    if (currentQuizData.b !="answer") {
    	document.getElementById("QA2").innerHTML +="<div id='ansDiv2'><input type='radio' name='answer' id='b' class='answer'><label for='b' id='b_text'>"+currentQuizData.b+"</label></div>";	
    }else{
    	document.getElementById("QA2").innerHTML +="<div id='ansDiv2'></div>";
    }
   

    if (currentQuizData.c !="answer") {
    	document.getElementById("QA3").innerHTML +="<div id='ansDiv3'><input type='radio' name='answer' id='c' class='answer'><label for='c' id='c_text'>"+currentQuizData.c+"</label></div>";    	
    }else{
    	document.getElementById("QA3").innerHTML +="<div id='ansDiv3'></div>";
    }
  
    if (currentQuizData.d !="answer") {
    	document.getElementById("QA4").innerHTML +="<div id='ansDiv4'><input type='radio' name='answer' id='d' class='answer'><label for='d' id='d_text'>"+currentQuizData.d+"</label></div>";    	
    }else{
    	document.getElementById("QA4").innerHTML +="<div id='ansDiv4'></div>";
    }  

    if (currentQuizData.e !="answer") {
    	document.getElementById("QA5").innerHTML +="<div id='ansDiv5'><input type='radio' name='answer' id='e' class='answer'><label for='e' id='e_text'>"+currentQuizData.e+"</label></div>";    	
    }else{
    	document.getElementById("QA5").innerHTML +="<div id='ansDiv5'></div>";
    }  
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = (answerEl.id).toString();   
                
        }
    })
    return answer
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    outputs[currentQuiz]=answer;    
    var AnsRemove1= document.getElementById('ansDiv1');
    AnsRemove1.remove();
    var AnsRemove2= document.getElementById('ansDiv2');
    AnsRemove2.remove();
    var AnsRemove3= document.getElementById('ansDiv3');
    AnsRemove3.remove();
    var AnsRemove4= document.getElementById('ansDiv4');
    AnsRemove4.remove();
    var AnsRemove5= document.getElementById('ansDiv5');
    AnsRemove5.remove();
    currentQuiz++
    if(currentQuiz < quizData.length){
           loadQuiz()
       }else{
       		var qizBRemove= document.getElementById('submit');
            qizBRemove.remove();
            var qizRemove= document.getElementById('head');
            qizRemove.remove();
            for (i = 0; i < outputs.length; i++)
                document.getElementById("quiz").innerHTML+= (i+1) + ": " + outputs[i];

       } 
    
})