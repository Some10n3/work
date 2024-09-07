from fastapi import FastAPI

app = FastAPI()

students = {
    29 : {
        "ID" : 29,
        "Name" : "John",
        "Lastname" : "Doe",
    },
    30 : {
        "ID" : 30,
        "Name" : "Jane",
        "Lastname" : "Doe",
    }
}

@app.get("/students/all")
async def func():
    return students

@app.get("/students/{student_id}")
async def func(student_id : int):
    if student_id not in students:
        return {"Error" : "Student not found"}
    return students[student_id]

#body parameters
@app.post("/students/new/")
async def func(student : dict):
    if student["ID"] in students:
        return {"Error" : "Student already exists"}
    students[student["ID"]] = student
    return students[ID]

#path parameters
@app.post("/students/new/{Name}/{Lastname}/{ID}")
async def func(Name : str, Lastname : str, ID : int):
    if ID in students:
        return {"Error" : "Student already exists"}
    students[ID] = {"ID" : ID, "Name" : Name, "Lastname" : Lastname}
    return students[ID]

#query parameters
@app.post("/students/newForm")
async def func(Name : str, Lastname : str, ID : int):
    if ID in students:
        return {"Error" : "Student already exists"}
    students[ID] = {"ID" : ID, "Name" : Name, "Lastname" : Lastname}
    return students[ID]

# {"ID" : 86, "Name" : "ada", "Lastname" : "asdfaf"}