
function createCalendar(month, year){

    var div = document.getElementById("calendar");
    div.innerHTML = "";

    var daysInMonth = new Date(year, month+1, 0).getDate();

    var tbl = document.createElement("table");
    var tblBody = document.createElement("tbody");

    var row = document.createElement("tr");

    //button1
    var cell = document.createElement("td");
    var button = document.createElement("button");
    var cellText = document.createTextNode("<");
    button.appendChild(cellText);
    if (month != 0){
        button.setAttribute("onclick", "createCalendar(" + (month - 1) + "," + year + ")");
    }
    cell.appendChild(button);
    row.appendChild(cell);

    //month and year

    var cell = document.createElement("td");
    var cellText = document.createTextNode((month + 1) + "/" + year);
    cell.appendChild(cellText);
    cell.setAttribute("colspan", "5");
    row.appendChild(cell);
    tblBody.appendChild(row);

    //button2
    var cell = document.createElement("td");
    var button = document.createElement("button");
    var cellText = document.createTextNode(">");
    button.appendChild(cellText);
    if (month != 11){
        button.setAttribute("onclick", "createCalendar(" + (month + 1) + "," + year + ")");

    }
    cell.appendChild(button);
    row.appendChild(cell);

    var row = document.createElement("tr");

    var days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

    for (var i = 0; i < 7; i++) {
        var cell = document.createElement("td");
        var cellText = document.createTextNode(days[i]);
        cell.appendChild(cellText);
        row.appendChild(cell);
    }
    tblBody.appendChild(row);

    var count = 1;
    var day1 = new Date(year, month, 1).getDay();
    day1 = (day1 + 6) % 7;

    for (var i = 0; i < 5; i++) {
        var row = document.createElement("tr");
        for (var j = 0; j < 7; j++) {
            if (i == 0 && j < day1) {
                var cell = document.createElement("td");
                var cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            else if (count > daysInMonth) {
                var cell = document.createElement("td");
                var cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            else {
                var cell = document.createElement("td");
                var cellText = document.createTextNode(count);
                cell.appendChild(cellText);
                row.appendChild(cell);
                count++;
            }
        }
        tblBody.appendChild(row);
    }
    if (count <= daysInMonth) {
        var row = document.createElement("tr");
        for (var j = 0; j < 7; j++) {
            if (count > daysInMonth) {
                var cell = document.createElement("td");
                var cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            else {
                var cell = document.createElement("td");
                var cellText = document.createTextNode(count);
                cell.appendChild(cellText);
                row.appendChild(cell);
                count++;
            }
        }
        tblBody.appendChild(row);
    }

    tbl.appendChild(tblBody);
    // tbl.setAttribute("border", "2");
    div.appendChild(tbl);
}

//on load execute createCalendar function with January
window.onload = function(){
    createCalendar(0, 2023);
}