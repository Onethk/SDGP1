//get prediction h1 tag
var pretester = document.getElementById("predouter");

//get textcontent of tag
pretester = pretester.textContent;

console.log(pretester);
//get prediction string only
var pretester = pretester.substring(1, pretester.length - 1);

console.log(pretester);

var predOut = pretester;
console.log(predOut);

var behavArray = document.getElementById("behavOuter");
// console.log(behavArray.textContent);
// var passArr = behavArray.textContent;
console.log(behavArray.textContent);
var passArr = behavArray.textContent;
console.log(typeof passArr);
var passArr = passArr.substring(1, passArr.length - 1);
console.log(typeof passArr);
var base = passArr.split(",").map(function (item) {
  return parseInt(item, 10);
});

console.log("base" + base);
console.log(typeof base);
passArr = base;

var tipMarkRange;
var tipsArr = [];

//set ranges to predicted marks
if (predOut == "0 to 39") {
  tipMarkRange = 39;
} else if (
  predOut == "40 to 49" ||
  predOut == "50 to 59" ||
  predOut == "60 to 69"
) {
  tipMarkRange = 69;
} else predOut == "70 to 79" || predOut == "80 to 89" || predOut == "90 to 100";
tipMarkRange = 100;

//tips
var tip1 =
  "Should improve on majority of the subjects where the student is weak ";
var tip2 =
  "Can do better as the first classes are in boundaries . Keep on repeated learning!";
var tip3 = "Revise more on practice papers";
var tip4 = "Do not procrastinate ";
var tip5 = "Avoid distractions";
var tip6 =
  "Watch out the missed lectures recordings for a better understanding";
var tip7 =
  "Watch YouTube videos or different education platforms according to ur comfort zone";
var tip8 = "Keep the phone on do not disturb mode or put it on silent";
var tip9 = "Spend more time on studies than extra-curricular activities ";
var tip10 = "Move to a calm place like a library where you feel only to study";
var tip11 = "Seek help from online Web-sites";

//create tips array depend on behaviours
if (tipMarkRange == 39) {
  tipsArr.push(tip1);
} else if (tipMarkRange == 69) {
  tipsArr.push(tip2);
} else {
  tipsArr.push(tip3);
}

if (passArr[5] == 2) {
  tipsArr.push(tip4);
} else if (passArr[5] == 1) {
  tipsArr.push(tip5);
}

if (passArr[6] == 1 || passArr[6] == 3) {
  tipsArr.push(tip6);
}

if (passArr[7] == 1 || passArr[7] == 3) {
  tipsArr.push(tip7);
}

if (passArr[9] == 3) {
  tipsArr.push(tip8);
}

if (passArr[10] == 1) {
  tipsArr.push(tip9);
}

if (passArr[2] == 1) {
  tipsArr.push(tip10);
}

if (passArr[8] == 0) {
  tipsArr.push(tip11);
}

//
if (tipsArr.length < 5) {
  var emptys = 5 - tipsArr.length;
  for (var x = 0; x < emptys; x++) {
    tipsArr.push(" ");
  }
}

document.getElementById("tipLine1").innerHTML += tipsArr[0];
document.getElementById("tipLine2").innerHTML += tipsArr[1];
document.getElementById("tipLine3").innerHTML += tipsArr[2];
document.getElementById("tipLine4").innerHTML += tipsArr[3];
document.getElementById("tipLine5").innerHTML += tipsArr[4];

let text0 = document.getElementById("itext0");
let text1 = document.getElementById("itext1");
let text2 = document.getElementById("itext2");
let text3 = document.getElementById("itext3");
let text4 = document.getElementById("itext4");

// text4.style.display = "none";

if (tipsArr[0] == " ") {
  text4.style.display = "none";
}
if (tipsArr[1] == " ") {
  text4.style.display = "none";
}
if (tipsArr[2] == " ") {
  text4.style.display = "none";
}
if (tipsArr[3] == " ") {
  text4.style.display = "none";
}
if (tipsArr[4] == " ") {
  text4.style.display = "none";
}
