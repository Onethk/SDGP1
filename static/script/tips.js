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