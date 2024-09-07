
function start () {

    const json = {};
    
    const table = document.getElementById("originalTable");    

    const rows = table.rows;

    var array = [];

    for (let i = 0; i < rows[0].cells.length; i++) {
        array.push(rows[0].cells[i].innerHTML);
    }

    json["header"] = array;

    array = [];

    for (let i = 1; i < rows.length - 1; i++) {
        const row = rows[i];
        const cells = row.cells;
        for (let j = 0; j < cells.length; j++) {
            const innerJSON = {};
            const key = rows[0].cells[j].innerHTML;
            const value = cells[j].innerHTML;
            //if colspan or rowspan is not 1, add them to the json
            innerJSON[key] = value;
            if (cells[j].colSpan != 1) {
                innerJSON["colSpan"] = cells[j].colSpan;
            }
            array.push(innerJSON);
        }
    }
    json["body"] = array;

    array = [];

    //add footer
    const footer = rows[rows.length - 1].cells;

    for (let j = 0; j < footer.length; j++) {
        const innerJSON = {};
        const key = rows[0].cells[j].innerHTML;
        const value = footer[j].innerHTML;
        //if colspan or rowspan is not 1, add them to the json
        innerJSON[key] = value;
        innerJSON["colSpan"] = footer[j].colSpan;
        array.push(innerJSON);
    }

    json["footer"] = array;

    // console.log(json);

    const jsonText = JSON.stringify(json, null, 4);
    
    const jsonTextArea = document.getElementById("jsonTextArea");
    jsonTextArea.value = jsonText;

}

function convert () {

    const div = document.getElementById("newTable");
    div.innerHTML = "";

    const table = div.appendChild(document.createElement("table"));  
    table.setAttribute("border", "1");
    table.setAttribute("align", "center");

    const jsonTextArea = document.getElementById("jsonTextArea");
    const jsonText = jsonTextArea.value;

    const json = JSON.parse(jsonText);

    const header = json["header"];
    const body = json["body"];
    const footer = json["footer"];

    const headerRow = table.insertRow(0);

    for (let i = 0; i < header.length; i++) {   
        const cell = headerRow.insertCell(i);
        cell.innerHTML = header[i];
    }

    for (let i = 0; i < body.length / 5; i++) {
        const row = table.insertRow(i + 1);
        const ii = i * 5;
        const cell = row.insertCell(0);
        cell.innerHTML = body[ii]["Number"];
        const cell2 = row.insertCell(1);
        cell2.innerHTML = body[ii + 1]["Item"];
        const cell3 = row.insertCell(2);
        cell3.innerHTML = body[ii + 2]["Quantity"];
        const cell4 = row.insertCell(3);
        cell4.innerHTML = body[ii + 3]["Price"];
        const cell5 = row.insertCell(4);
        cell5.innerHTML = body[ii + 4]["Amount"];
    }

    // console.log(body.length);

    const footerRow = table.insertRow(table.rows.length);
    
    var cumColspan = 0;

    for (let i = 0; i < footer.length; i++) {
        const cell = footerRow.insertCell(i);
        cell.colSpan = footer[i]["colSpan"];
        if (cumColspan < 5 && i == footer.length - 1) {
            cell.colSpan = 5 - cumColspan;
            // console.log(cell.colSpan);
        }
        cumColspan = cumColspan + footer[i]["colSpan"];
        if (footer[i]["Number"] != undefined){
            cell.innerHTML = footer[i]["Number"];
        }
        else if (footer[i]["Item"] != undefined){
            cell.innerHTML = footer[i]["Item"];
        }
    }

    // const cell = footerRow.insertCell(0);
    // if (footer[0]["colSpan"] != undefined) {
    //     cell.colSpan = footer[0]["colSpan"];
    // }
    // cell.innerHTML = footer[0]["Number"];

    // // console.log(footer[0]["Number"]);

    // const cell2 = footerRow.insertCell(1);
    // if (footer[1]["colSpan"] != undefined) {
    //     cell2.colSpan = footer[1]["colSpan"];
    // }
    // cell2.innerHTML = footer[1]["Item"];



}

window.addEventListener("load", start, false);