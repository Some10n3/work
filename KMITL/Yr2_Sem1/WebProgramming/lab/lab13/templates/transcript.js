
function display_data(jsonObj){

    const tableBody = document.getElementById('content_body');

    
    
    const rows = tableBody.getElementsByTagName('tr');
    const rowsLength = rows.length;
    for (let i = 0; i < rowsLength; i++) {
        tableBody.removeChild(rows[0]);
    }

    const credit = jsonObj.credit;
    const years = Object.keys(credit);

    var gpa = 0;
}

function mapGrade(grade) {
    switch (grade) {
        case "A":
            return 4;
        case "B+":
            return 3.5;
        case "B":
            return 3;
        case "C+":
            return 2.5;
        case "C":
            return 2;
        case "D+":
            return 1.5;
        case "D":
            return 1;
        case "F":
            return 0;
        case "S":
            return 0;
        case "U":
            return 0;
        case "X":
            return 0;
        default:
            return 0;
    }
}

window.onload = function() {
    
}