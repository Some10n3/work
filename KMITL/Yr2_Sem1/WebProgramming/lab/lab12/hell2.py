from fastapi import FastAPI

app = FastAPI()

@app.get("/path/{param}")
async def root(param : str):
    return {"message": f"Hello {param}"}