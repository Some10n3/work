function alarm(time, text) {
    this.time = time || "";
    this.text = text || "";
}

const alarms = [
    new alarm("10:00", "Wake up!"),
    new alarm("12:00", "Lunch time!"),
    new alarm("18:00", "Dinner time!"),
    new alarm("22:00", "Go to bed!"),
];

var hour = 0;
var minute = 0;

const timeList = document.getElementById("tableAlarm");
const row = document.createElement("tr");

const time = document.createElement("td");
time.innerHTML = "Time";
time.style.fontWeight = "bold";
row.appendChild(time);
const text = document.createElement("td");
text.innerHTML = "Alert";
text.style.fontWeight = "bold";
row.appendChild(text);

timeList.appendChild(row);

for (var i = 0; i < alarms.length; i++) {
    const row = document.createElement("tr");
    
    const time = document.createElement("td");
    time.innerHTML = alarms[i].time;
    row.appendChild(time);
    
    const text = document.createElement("td");
    text.innerHTML = alarms[i].text;
    row.appendChild(text);

    timeList.appendChild(row);
}

function showAlert() {
    for (var i = 0; i < alarms.length; i++) {
        if (document.getElementById("timeNow").innerHTML == alarms[i].time) {
            alert(alarms[i].text);
            // document.getElementById("debug").innerHTML = "this happened";
        }
    }
}

function tick() {
    minute++;
    setTimeout("tick()", 10);
    if (minute == 60) {
        minute = 0;
        hour++;
    }
    if (hour == 24) {
        hour = 0;
    }
    showTime();
    showAlert();
}

function showTime() {
    if (hour < 10) {
        var hourr = "0" + hour;
    } else {    
        var hourr = hour;
    }
    if (minute < 10) {
        var minutee = "0" + minute;
    } else {
        var minutee = minute;
    }
    document.getElementById("timeNow").innerHTML = hourr + ":" + minutee;
}

Event.observe(window, 'load', tick());