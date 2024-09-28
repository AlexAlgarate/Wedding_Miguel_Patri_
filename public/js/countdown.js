function getMadridTime(dateString) {
    return new Date(new Date(dateString).toLocaleString("en-US", { timeZone: "Europe/Madrid" }));
}
var countDownDate = getMadridTime("May 30, 2025 19:30:00").getTime();


var x = setInterval(function () {
    var daysElement = document.getElementById("days");
    var hoursElement = document.getElementById("hours");
    var minutesElement = document.getElementById("minutes");
    var secondsElement = document.getElementById("seconds");

    if (daysElement !== null && hoursElement !== null && minutesElement !== null && secondsElement !== null) {
        var now = new Date().getTime();
        var distance = countDownDate - now;

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        daysElement.innerHTML = days ;
        hoursElement.innerHTML = hours ;
        minutesElement.innerHTML = minutes ;
        secondsElement.innerHTML = seconds ;

        if (distance < 0) {
            clearInterval(x);
            daysElement.innerHTML = "¡Comienza nuestra boda!";
            hoursElement.innerHTML = "";
            minutesElement.innerHTML = "";
            secondsElement.innerHTML = "";
        }
    }
}, 1000);