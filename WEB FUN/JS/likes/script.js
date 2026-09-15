var likes1 = document.querySelector("#neil");
var likes2 = document.querySelector("#nich");
var likes3 = document.querySelector("#jim");

function increase(likes) {

    let int = parseInt(likes.innerText);

    var num = int + 1;

    likes.innerText = num + " like(s)";
}