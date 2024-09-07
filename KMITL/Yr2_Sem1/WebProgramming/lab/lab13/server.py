
from fastapi import FastAPI, Request, Body
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

import ZODB, ZODB.FileStorage
import transaction
import BTrees.OOBTree

from classes import Student, Course, Enrollment

app = FastAPI()
templates = Jinja2Templates(directory="templates")

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root
root.students = BTrees.OOBTree.BTree()

#ZODB part

@app.post("/students/new/")
async def create_student(body = Body(...)):
    sid = int (body["ID"])
    root.students[sid] = body
    transaction.commit()
    return root.students[sid]

@app.post("/login")
def login(request: Request, ID: int = Body(...), Password: str = Body(...)):

    for student in root.students.values():
        if student["ID"] == ID and student["Password"] == Password:
            print("Login success")
            return RedirectResponse(url="/score-page")
    return {"message": "Username or password is incorrect", "ID": ID, "Password": Password, "students": root.students.values()}

@app.on_event("shutdown")
def shutdown_event():
    db.close() 
    storage.close()

#page part

@app.get("/")
def redirect_to_another_uri():
    redirect_uri = "/login-page"
    return RedirectResponse(url=redirect_uri)

@app.get("/login-page")
def show_html(request: Request):

    context = {
        "icon_url": "http://example.com/myicon.png",
        "page_title": "Login Page",
        "background_color": "#dbcbc0",
        "container_background_color": "white",
        "heading_color": "#212121",
        "input_border_color": "#bdc3c7",
        "button_background_color": "#9900c4",
        "button_text_color": "#fff",
        "button_hover_background_color": "#d03ee6",
        # "js_script": "login.js",
        "action_url": "/login",
        "login_heading": "Login",
        "alert_color": "rgb(255, 0, 111)",
        "username_placeholder": "Username",
        "password_placeholder": "Password",
        "login_button_text": "Login"
    }

    return templates.TemplateResponse("login.html", {"request": request, **context})

@app.get("/score-page")
def show_html(request: Request):

    context = {
        "page_title": "Unofficial Transcript",
        "transcript_heading": "( Transcript Entry Form )",
        "course_id_label": "COURSE ID",
        "course_title_label": "COURSE TITLE",
        "credit_label": "CREDIT",
        "score_label": "SCORE",
        "js_script": "transcript.js",
        "courses": [
            {"id": "101", "title": "Web prog", "credit": "4", "score": "A"},
            {"id": "102", "title": "Database", "credit": "3", "score": "B"}
            # Add more courses as needed
        ]
    }
    print("score page")

    return templates.TemplateResponse("transcript-entry-form.html", {"request": request, **context})




