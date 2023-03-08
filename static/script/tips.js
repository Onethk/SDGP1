//get prediction h1 tag
var pretester= document.getElementById("predouter");
//get textcontent of tag
pretester= pretester.textContent;
console.log(pretester);
//get prediction string only
var pretester= pretester.substring(1, pretester.length-1)
console.log(pretester);

var predOut = pretester;
console.log(predOut);

var behavArray=document.getElementById("behavOuter");
console.log(behavArray.textContent);
var passArr = behavArray.textContent;
var tipMarkRange;
var tipsArr = [];

//set ranges to predicted marks
if(predOut=="0 to 39"){
    tipMarkRange= 39;
}else if(predOut=="40 to 49"|| predOut=="50 to 59" || predOut=="60 to 69"){
    tipMarkRange=69;
}else(predOut=="70 to 79" || predOut=="80 to 89" || predOut=="90 to 100")
    tipMarkRange=100;

//tips
var tip1 ="if mark range is less than 40";
var tip2 ="if mark range is less than 70";
var tip3 ="if mark range is more than 70";
var tip4 ="if study hours less than 2 hours";
var tip5 ="if study hours less than 1 hours";
var tip6 ="if attendance for lecs is poor";
var tip7 ="if concentration in lecs is poor";
var tip8 ="if spend more than 2 hours in social media";
var tip9 ="if spend too much time on extra curricular acts";
var tip10 ="if spare too much time on relationships";
var tip11 ="if no friends to get help on studies";

//create tips array depend on behaviours
if(tipMarkRange==39){
    tipsArr.push(tip1);
}else if(tipMarkRange==69){
    tipsArr.push(tip2);
}else{
    tipsArr.push(tip3);
}

if(passArr[5]==2){
    tipsArr.push(tip4);
}else if(passArr[5]==1){
    tipsArr.push(tip5);
}

if(passArr[6]==1 || passArr[6]==3){
    tipsArr.push(tip6);
}

if(passArr[7]==1 || passArr[7]==3){
    tipsArr.push(tip7);
}

if(passArr[9]==3){
    tipsArr.push(tip8);
}

if(passArr[10]==1){
    tipsArr.push(tip9);
}

if(passArr[2]==1){
    tipsArr.push(tip10);
}

if(passArr[8]==0){
    tipsArr.push(tip11);
}

//
if(tipsArr.length<5){
    var emptys=5-tipsArr.length;
    for(var x=0;x<emptys;x++){
        tipsArr.push(" ");
    }
}

document.getElementById("tipLine1").innerHTML+=tipsArr[0];
document.getElementById("tipLine2").innerHTML+=tipsArr[1];
document.getElementById("tipLine3").innerHTML+=tipsArr[2];
document.getElementById("tipLine4").innerHTML+=tipsArr[3];
document.getElementById("tipLine5").innerHTML+=tipsArr[4];

let text0 = document.getElementById("itext0");
let text1 = document.getElementById("itext1");
let text2 = document.getElementById("itext2");
let text3 = document.getElementById("itext3");
let text4 = document.getElementById("itext4");

// text4.style.display = "none";

if(tipsArr[0] == " "){
    text4.style.display = "none";
}
if(tipsArr[1] == " "){
    text4.style.display = "none";
}
if(tipsArr[2] == " "){
    text4.style.display = "none";
}
if(tipsArr[3] == " "){
    text4.style.display = "none";
}
if(tipsArr[4] == " "){
    text4.style.display = "none";
}