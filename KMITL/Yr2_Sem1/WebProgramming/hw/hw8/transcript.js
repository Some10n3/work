
function onChange(event) {
    var reader = new FileReader();
    reader.onload = onReaderLoad;
    reader.readAsText(event.target.files[0]);
}

function onReaderLoad(event){
    console.log(event.target.result);
    var obj = JSON.parse(event.target.result);
    display_data(obj);
}

function display_data(jsonObj){
    document.getElementById('student_name').value = jsonObj.student_name;
    document.getElementById('date_of_birth').value = jsonObj.date_of_birth;
    document.getElementById('student_id').value = jsonObj.student_id;
    document.getElementById('date_of_admission').value = jsonObj.date_of_admission;
    document.getElementById('date_of_graduation').value = jsonObj.date_of_graduation;
    document.getElementById('degree').value = jsonObj.degree;
    document.getElementById('major').value = jsonObj.major;

    const tableBody = document.getElementById('content_body');

    const rows = tableBody.getElementsByTagName('tr');
    const rowsLength = rows.length;
    for (let i = 0; i < rowsLength; i++) {
        tableBody.removeChild(rows[0]);
    }

    const credit = jsonObj.credit;
    const years = Object.keys(credit);

    var gpa = 0;

    for (let i = 0; i < years.length; i++) {
        const year = years[i];
        const semesters = Object.keys(credit[year]);
        for (let j = 0; j < semesters.length; j++) {
            
            const semester = semesters[j];

            //print semester
            const row = tableBody.insertRow(-1);
            const semesterCell = row.insertCell(0);
            semesterCell.innerHTML = year + " " + semester;
            semesterCell.style.fontWeight = "bold";
            semesterCell.style.textDecoration = "underline";

            row.insertCell(1);row.insertCell(2);
            
            var gps = 0;
            var credits = 0;
            const subjects = credit[year][semester];

            for (let k = 0; k < subjects.length; k++) {
                
                const subject = subjects[k];
                const row = tableBody.insertRow(-1);

                const nameCell = row.insertCell(0);
                const creditCell = row.insertCell(1);
                const gradeCell = row.insertCell(2);

                nameCell.innerHTML = subject.subject_id + " " + subject.name;
                nameCell.setAttribute("align", "left");
                //not bold
                nameCell.style.fontWeight = "normal";
                creditCell.innerHTML = subject.credit;
                gradeCell.innerHTML = subject.grade;

                gps += mapGrade(subject.grade) * subject.credit;
                credits += parseInt(subject.credit);
            }

            gps /= credits;
            gpa += gps;
            gps = gps.toFixed(2);

            const gpaAndGpsRow = tableBody.insertRow(-1);
            const gpaAndGpsCell = gpaAndGpsRow.insertCell(0);
            gpaAndGpsCell.innerHTML = "GPA: " + (gpa / (j + 1)).toFixed(2) + " GPS: " + gps;
            gpaAndGpsCell.style.fontStyle = "italic";

            gpaAndGpsRow.insertCell(1);gpaAndGpsRow.insertCell(2);

        }
    }
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
    document.getElementById('fileInput').addEventListener('change', onChange);
}