const wsScheme = window.location.protocol == "https:" ? "wss" : "ws"; 
const wsURL = wsScheme + "://" + location.hostname + (location.port ? ":" + location.port : "") + "/ws/";

var socket = new WebSocket(wsURL + "notifications/") 

function displayNotifModalPopup(message) {
    const notificationPopup = document.querySelector(".notification-popup");
    const notifMessage = document.querySelector(".notification-popup p");
    notificationPopup.style.opacity = 1;
    notifMessage.textContent = message;
}


socket.onmessage = function(e){
    const messageObj = JSON.parse(e.data)

    if(messageObj.type == "Notification"){
        displayNotifModalPopup(messageObj.message);
    }
}

socket.onopen = function(e){
    console.log('open', e)
}

socket.onerror = function(e){
    console.log('error', e)
}

socket.onclose = function(e){
    console.log('closed', e)
}