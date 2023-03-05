var predOut = data.arr_str; //recieve predicted mark range
var passArr = testing3; //recieve behaviour array
var tipMarkRange;
var tipsArr=[];

//set ranges to predicted marks
if(predOut=="0 to 39"){
    tipMarkRange= 39;
}else if(predOut=="40 to 49"|| predOut=="50 to 59" || predOut=="60 to 69"){
    tipMarkRange=69;
}else(predOut=="70 to 79" || predOut=="80 to 89" || predOut=="90 to 100")
    tipMarkRange=100;

    
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
