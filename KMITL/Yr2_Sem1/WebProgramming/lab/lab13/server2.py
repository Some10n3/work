from fastapi import FastAPI, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

login_form = {"id": "12", "password": "1234" ,"name":"sdfg"}

@app.get("/getall/")
async def root():
    return login_form

@app.post("/login/", response_class=HTMLResponse)
async def start(id: str = Form(...), password: str = Form(...)):
    if id == login_form["id"] and password == login_form["password"]:
        redirect_url = f"/transcript/?id={id}&name={login_form['name']}"
        return RedirectResponse(url=redirect_url,status_code=302)
    else:
        error_message = "<h1 style='color:red;'>Incorrect login</h1>"
        return HTMLResponse(content=error_message)

# @app.post("/transcript/score", response_class=HTMLResponse)
# async def get_html():
#     html_content = """
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>Lab 13 - Login</title>
#     </head>
#     <body>
#         <h1 style="text-align:center">Transcript Entry Form</h1>

    
@app.get("/")
def redirect_to_another_uri():
    redirect_uri = "/loginget/"
    return RedirectResponse(url=redirect_uri)

    
@app.get("/loginget/", response_class=HTMLResponse)
async def get_html():
    html_content = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Lab 13 - Login</title>
    </head>
    <body>
        <h1>Login</h1>
        <form action="/login/" method="post">
            <label for="username">Username:</label>
            <input type="text" name="id" id="id" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password" required>
            <br>
            <input type="submit" value="Login">
        </form>
    </html>
    """
    return html_content 


# @app.post("/loginpost/")
# async def root(dict:dict):
#     if str(dict["ID"]) in login_form:
#         return "ID is already exist"
#     else:
#         login_form[dict["ID"]]=dict
#         return login_form[dict["ID"]]
    
@app.get("/redirect/transcript")
def redirect_to_another_uri():
    redirect_url = "/transcript/"
    return RedirectResponse(url=redirect_url)
    
@app.get("/transcript/",response_class=HTMLResponse)
async def get_html():
    html_content = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Lab 13 - Transcript</title>
    </head>
    <body>
        <h1 style="text-align:center">Transcript Entry Form</h1>
        <form action="/last-transcript" method="post">
    <table>
        <tr>
            <td colspan=4 >Student ID:{login_form['id']}</td>
            <td colspan=4 >Name: {login_form['name']}</td>
        </tr>
        <tr>
            <td colspan=2> Course Code </td>
            <td colspan=2> Course Name </td>
            <td colspan=2> Credit </td>
            <td colspan=2> Score </td>
        </tr>
        <tr>
            <td colspan=2><p>101</p></td>
            <td colspan=2><p>Web Programming</p></td>
            <td colspan=2><p>4</p></td>
            <td colspan=2><input type="text" name="score1" id="Web" required></td>
        </tr>
        <tr>
            <td colspan=2><p>101</p></td>
            <td colspan=2><p>Web Programming</p></td>
            <td colspan=2><p>3</p></td>
            <td colspan=2><input type="text" name="score2" id="Database" required></td>
        </tr>
        <tr>
            <td colspan=2><p>101</p></td>
            <td colspan=2><p>Web Programming</p></td>
            <td colspan=2><p>4</p></td>
            <td colspan=2><input type="text" name="score3" id="AI" required></td>
        <tr>
            <td colspan=2><p>101</p></td>
            <td colspan=2><p>Web Programming</p></td>
            <td colspan=2><p>3</p></td>
            <td colspan=2><input type="text" name="score4" id="Data" required></td>
        </tr>
        <tr>
            <td>
                <input type="submit" value="Submit">
            </td>
        </tr>
        
    </table>
    </form>
    </html>
    """
    return html_content

@app.post("/last-transcript")
async def start(score1: str = Form(...), score2: str = Form(...),score3: str = Form(...),score4: str = Form(...)):
    redirect_url = f"/last-transcript/?score1={score1}&score2={score2}&score3={score3}&score4={score4}"
    return RedirectResponse(url=redirect_url,status_code=302)

# @app.get("/last-transcript/",response_class=HTMLResponse)
#     html_content = f"""
#     <html lang="en">
#     <body>
#     <br><br>
#     <h1>{{ transcript_heading }}</h1>
#     <table class="content_table">
#         <thead>
#             <th style="width: 5%;">
#                 <p>{{ course_id_label }}</p>
#             </th>
#             <th style="width: 85%;">
#                 <p>{{ course_title_label }}</p>
#             </th>
#             <th style="width: 5%;">
#                 <p>{{ credit_label }}</p>
#             </th>
#             <th style="width: 5%;">
#                 <p>{{ score_label }}</p>
#             </th>
#         </thead>
#         <tbody id="content_body">
#             {% for course in courses %}
#             <tr>
#                 <td style="text-align: left;">{{ course.id }}</td>
#                 <td>{{ course.title }}</td>
#                 <td>{{ course.credit }}</td>
#                 <input type="text" id="score_{{ course.id }}" value="{{ course.score }}">
#             </tr>
#             {% endfor %}
#         </tbody>
#     </table>
#     </body>
#     </html>"""
#     return html_content