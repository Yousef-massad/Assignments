function show(element) {
    alert("showing weather for " + element.innerText)
}

function hide() {
    var foot = document.querySelector("footer")
    foot.remove();
}

var current="c"

function changeTemp(){
    var sel= document.getElementById("room2")
    var red=document.querySelectorAll(".red")
    var blue=document.querySelectorAll(".blue")

    console.log("hello")
    if(sel.value !== current){

        if(sel.value === "f"){
       
            for(var i=0; i<red.length; i++){
                var rep=Number(red[i].textContent.replace("°",""))
                var fah=rep*9/5+32
                red[i].innerText=fah + "°"

                var rep=Number(blue[i].textContent.replace("°",""))
                var fah=rep*9/5+32
                blue[i].innerText=fah + "°"
            }

            current="f"
        }

        else{
            for(var i=0; i<red.length; i++){
                var rep=Number(red[i].textContent.replace("°",""))
                var cel=Math.round((rep - 32) * 5 / 9 * 10) / 10
                red[i].innerText=cel + "°"

                var rep=Number(blue[i].textContent.replace("°",""))
                var cel=Math.round((rep - 32) * 5 / 9 * 10) / 10
                blue[i].innerText=cel + "°"
            }

            current="c"
        }
    }
}