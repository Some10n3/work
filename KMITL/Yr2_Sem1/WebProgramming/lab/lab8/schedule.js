
var alarms = {
    0:{
        "time": "00:00",  
        "text": "New Alarm"
    },
    1:{
        "time": "01:00",
        "text": "New Alarm2"
    },
};

// console.log(alarms);

var previewTime;
var hour = 0;
var minute = 0;
var mode = "view";

function start() {
    document.getElementById("btn").addEventListener("click", buttonToggle);
    document.getElementById("btn").innerHTML = "Edit Schedule";
    // document.getElementById("save").addEventListener("click", save);
    document.getElementById("export").addEventListener("click", exportJSON);
    view();
    // tick();
}

function view() {

    const div = document.getElementById("divAlarm");
    div.innerHTML = "";
    
    const timeList = document.createElement("table");
    const body = document.createElement("tbody");
    const row = document.createElement("tr");

    const time = document.createElement("td");
    time.innerHTML = "Time";
    time.style.fontWeight = "bold";
    row.appendChild(time);
    const text = document.createElement("td");
    text.innerHTML = "Activity";
    text.style.fontWeight = "bold";
    row.appendChild(text);

    body.appendChild(row);

    for (var i = 0; i < Object.keys(alarms).length; i++) {
        const row = document.createElement("tr");
        
        const time = document.createElement("td");
        time.innerHTML = alarms[i]["time"];
        // console.log(alarms[i]["time"]);
        // console.log(time.innerHTML);
        row.appendChild(time);
        const text = document.createElement("td");
        text.innerHTML = alarms[i]["text"];
        row.appendChild(text);
        
        body.appendChild(row);
    }

    timeList.appendChild(body);
    div.appendChild(timeList);
}

function edit() {

    const div = document.getElementById("divAlarm");
    div.innerHTML = "";

    const timeList = document.createElement("table");
    const body = document.createElement("tbody");
    const row = document.createElement("tr");

    const time = document.createElement("td");
    time.innerHTML = "Time";
    time.style.fontWeight = "bold";
    row.appendChild(time);
    const text = document.createElement("td");
    text.innerHTML = "Activity";
    text.style.fontWeight = "bold";
    row.appendChild(text);

    body.appendChild(row);

    for (var i = 0; i < Object.keys(alarms).length; i++) {
        const row = document.createElement("tr");
        
        const time = document.createElement("td");
        const timeInput = document.createElement("input");
        timeInput.type = "time";
        timeInput.id = "time" + i;
        timeInput.value = alarms[i]["time"];
        time.appendChild(timeInput);
        row.appendChild(time);
        
        const text = document.createElement("td");
        const textInput = document.createElement("input");
        textInput.type = "text";
        textInput.id = "text" + i;
        textInput.value = alarms[i]["text"];
        text.appendChild(textInput);
        row.appendChild(text);

        const del = document.createElement("td");
        const delBtn = document.createElement("button");
        delBtn.innerHTML = "Delete";
        delBtn.id = i;
        delBtn.addEventListener("click", remove);
        del.appendChild(delBtn);
        row.appendChild(del);

        body.appendChild(row);
        
    }

    timeList.appendChild(body);
    div.appendChild(timeList);

    const brrr = document.createElement("br");
    div.appendChild(brrr);
    div.appendChild(brrr);

    const addBtn = document.createElement("button");
    addBtn.innerHTML = "Add";
    addBtn.addEventListener("click", add);
    //class = "outerbutton"
    addBtn.className = "outerbutton";
    div.appendChild(addBtn);

}

function tick() {
    minute++;
    setTimeout("tick()", 1000);
    if (minute == 60) {
        minute = 0;
        hour++;
    }
    if (hour == 24) {
        hour = 0;
    }
    showTime();
    showAlert();
    // document.getElementById("debug").innerHTML = "this happened" + hour + ":" + minute;
}

function showAlert() {
    for (var i = 0; i < alarms.length; i++) {
        if (previewTime == alarms[i].time) {
            alert(alarms[i].text);
            // document.getElementById("debug").innerHTML = "this happened";
        }
    }
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
    previewTime = hourr + ":" + minutee;
    document.getElementById("timeNow").innerHTML = previewTime;
}

function buttonToggle(){
    if (mode == "view") {
        mode = "edit";
        document.getElementById("btn").innerHTML = "done";
        edit();        
    } else if (mode == "edit") {
        mode = "view";
        document.getElementById("btn").innerHTML = "edit schedule";
        for(var i = 0; i < Object.keys(alarms).length; i++) {
            alarms[i]["time"] = document.getElementById("time" + i).value;
            alarms[i]["text"] = document.getElementById("text" + i).value;
        }
        view();
    }
}

function remove() {
    alarms.splice(this.id, 1);
    edit();
}

function add() {
    const newAlarm = {};
    newAlarm["time"] = "00:00";
    newAlarm["text"] = "New Alarm";
    alarms[Object.keys(alarms).length] = newAlarm;
    edit();
}

function exportJSON() {
    const json = {};
    json["alarms"] = alarms;
    const jsonText = JSON.stringify(json, null, 4);
    //export as json file
    const blob = new Blob([jsonText], {type: "application/json"});
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    
    a.download = "schedule.json";

}

const dateInput = document.getElementById('file');

dateInput.addEventListener('change', function() {
 
    const selectedDate = dateInput.value;
    console.log('Selected date:', selectedDate);

    //read json file and add to alarms
    const file = this.files[0];
    const reader = new FileReader();
    reader.addEventListener('load', (event) => {
        const result = JSON.parse(event.target.result);
        // console.log(result);
        alarms = result;
        console.log(alarms);
    });
    reader.readAsText(file);
    view();
});

window.addEventListener("load", start());