const myDiv = document.getElementById('myWrk');
var counter = 0;
var locate = window.location.href;

console.log(locate)

function drasl(){
    if (counter % 2 == 0){
    myDiv.style.width = "50%";
    }   
    else{
        myDiv.style.width = "100%";
    }

    counter +=1;

}

myDiv.addEventListener('click', drasl);