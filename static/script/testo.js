const stars = document.querySelectorAll(".star");
let currentRate = document.querySelector("#currentRate");

stars.forEach((star,i) =>{
    star.onclick = function(){
        let current_star = i + 1;
        currentRate.innerText = `${current_star} of 5`;
        document.getElementById("rating").value = current_star;
        stars.forEach((star,j) =>{
            if(current_star >= j+1)
            {
                star.innerHTML = '&#9733';
            }
            else
            {
                star.innerHTML = '&#9734'
            }
        })
    }
})