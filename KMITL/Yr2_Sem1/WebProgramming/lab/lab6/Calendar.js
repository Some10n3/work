
function createCalendar(){
    // check date
    var date = document.getElementById("date").value;
    var datePattern = /^\d{4}-\d{2}-\d{2}$/;
    if(!datePattern.test(date)){
        alert("Invalid date format");
        return;
    }
    var dateArray = date.split("-");
    var year = parseInt(dateArray[0]);
    var month = parseInt(dateArray[1]);
    var day = parseInt(dateArray[2]);
    if(month < 1 || month > 12){
        alert("Invalid month");
        return;
    }
    if(day < 1 || day > 31){
        alert("Invalid day");
        return;
    }
    // create calendar
    var calendar = document.getElementById("calendar");
    calendar.innerHTML = "";
    var table = document.createElement("table");
    var caption = document.createElement("caption");
    caption.innerHTML = date;
    table.appendChild(caption);
    var thead = document.createElement("thead");
    var tr = document.createElement("tr");
    var th = document.createElement("th");
    th.innerHTML = "Sun";
    tr.appendChild(th);
    th = document.createElement("th");
    th.innerHTML = "Mon";
    tr.appendChild(th);
    th = document.createElement("th");
    th.innerHTML = "Tue";
    tr.appendChild(th);
    th = document.createElement("th");
    th.innerHTML = "Wed";
    tr.appendChild(th);
    th = document.createElement("th");
    th.innerHTML = "Thu";
    tr.appendChild(th);
    th = document.createElement("th");
    th.innerHTML = "Fri";
    tr.appendChild(th);
    th = document.createElement("th");
    th.innerHTML = "Sat";
    tr.appendChild(th);
    thead.appendChild(tr);
    table.appendChild(thead);
    var tbody = document.createElement("tbody");
    var firstDay = new Date(year, month - 1, 1);
    var lastDay = new Date(year, month, 0);
    var firstDayOfWeek = firstDay.getDay();
    var lastDayOfWeek = lastDay.getDay();
    var firstDayOfMonth = firstDay.getDate();
    var lastDayOfMonth = lastDay.getDate();
    var tr = document.createElement("tr");
    var td;
    var dayOfMonth = 1;
    for(var i = 0; i < 7; i++){
        td = document.createElement("td");
        if(i < firstDayOfWeek){
            td.innerHTML = "";
        }else{
            td.innerHTML = dayOfMonth;
            dayOfMonth++;
        }
        tr.appendChild(td);
    }
    tbody.appendChild(tr);
    for(var i = 0; i < 5; i++){
        tr = document.createElement("tr");
        for(var j = 0; j < 7; j++){
            td = document.createElement("td");
            if(dayOfMonth > lastDayOfMonth){
                td.innerHTML = "";
            }else{
                td.innerHTML = dayOfMonth;
                dayOfMonth++;
            }
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    table.appendChild(tbody);
    calendar.appendChild(table);
}