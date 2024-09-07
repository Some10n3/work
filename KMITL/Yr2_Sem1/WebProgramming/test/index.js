const fs = require('fs');

let student2 = {"id": "1", "name": "John", "surname": "Doe", "age": "20"}

fs.readFile("lab8.JSON", (err, data) => {
    if (err) throw err;

    let student = JSON.parse(data);
    console.log(student);
});

fs.writeFile("write.JSON", JSON.stringify(student2), (err) => {
    if (err) throw err;
    console.log("File write successfully");
});
