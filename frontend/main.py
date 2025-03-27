from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import requests

app = FastAPI()

# Serve HTML template
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get")
async def get_document():
    
    try:
        response = requests.get("http://backend:9567/get")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.post("/insert")
async def insert_document(text: str = Form(...)):
    
    try:
        response = requests.post("http://backend:9567/insert", json={"text": text})
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    
# Run the server on port 9567 and make it public
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9567, reload=True)
