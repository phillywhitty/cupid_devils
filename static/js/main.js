
// Hide django flash messages after few seconds

var messageTimer = document.getElementById('message-timer');

setTimeout(function() {
    messageTimer.style.display = 'none';
}, 3000);