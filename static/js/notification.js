const wsScheme = window.location.protocol == "https:" ? "wss" : "ws"; // check if https page, if true, use secure websockets transport
const wsURL = wsScheme + "://" + location.hostname + (location.port ? ":" + location.port : "") + "/ws/"; // web socket endpoint, same as in routing.py

var socket = new WebSocket(wsURL + "notifications/") // Creating a new Web Socket Connection

function displayNotifModalPopup(message) {
    const notificationPopup = document.querySelector(".notification-popup");
    const notifMessage = document.querySelector(".notification-popup p");
    notificationPopup.style.opacity = 1;
    notifMessage.textContent = message;
}

// Socket On receive message Functionality
socket.onmessage = function(e){
    console.log('heyo', e.data)
    const messageObj = JSON.parse(e.data)
    console.log(messageObj);

    if(messageObj.type == "Notification"){
        displayNotifModalPopup(messageObj.message);
    }
}

// Socket Connet Functionality
socket.onopen = function(e){
    console.log('open', e)
}

// Socket Error Functionality
socket.onerror = function(e){
    console.log('error', e)
}

socket.onclose = function(e){
    console.log('closed', e)
}