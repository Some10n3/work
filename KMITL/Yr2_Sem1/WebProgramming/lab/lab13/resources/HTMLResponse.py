from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/html/", response_class=HTMLResponse)
#the link should be http://localhost:8000/html/?name=yourname
async def get_html():
    html_content = """
    <html>
        <head>
            <title>Some HTML Response 1</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <p>This is a paragraph</p>
        </body>
    </html> """
    return html_content








    