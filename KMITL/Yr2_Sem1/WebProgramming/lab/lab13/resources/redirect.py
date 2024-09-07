from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/redirect")
def redirect_to_another_uri():
    redirect_uri = "/target_uri"
    return RedirectResponse(url = redirect_uri)

@app.get("/target_uri")
def target_uri():
    return {"message": "You have been redirected to this page!"}