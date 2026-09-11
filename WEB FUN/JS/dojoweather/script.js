function show(element) {
    alert("showing weather for " + element.innerText)
}

function hide() {
    var foot = document.querySelector("footer")
    foot.remove();
}