function changeName() {
    let nameElement = document.getElementById("username");
    nameElement.innerText = "John Doe";
}

function acceptRequest(elementId) {
    let element = document.getElementById(elementId);
    element.remove();

    let requestCountElement = document.getElementById("request-count");
    let currentRequests = parseInt(requestCountElement.innerText);
    requestCountElement.innerText = currentRequests - 1;

    let totalConnectionsElement = document.getElementById("total-connections");
    let currentConnections = parseInt(totalConnectionsElement.innerText);
    totalConnectionsElement.innerText = currentConnections + 1;
}

function denyRequest(elementId) {
    let element = document.getElementById(elementId);
    element.remove();

    let requestCountElement = document.getElementById("request-count");
    let currentRequests = parseInt(requestCountElement.innerText);
    requestCountElement.innerText = currentRequests - 1;
}