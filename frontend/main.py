# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from elasticsearch import Elasticsearch
# import uvicorn

# app = FastAPI()

# # Connect to Elasticsearch (assuming it runs in another container)
# es = Elasticsearch(hosts=["http://elasticsearch:9200"])  # Adjust host if needed

# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>FastAPI Frontend</title>
# </head>
# <body>
#     <h1>STT_Lab8</h1>
#     <input type="text" id="inputText" placeholder="Enter text here">
#     <button onclick="insertDocument()">Insert</button>
#     <button onclick="getBestScore()">Get Best Score</button>
#     <div id="output"></div>
#     <script>
#         async function insertDocument() {
#             let text = document.getElementById("inputText").value;
#             let response = await fetch("/insert", {
#                 method: "POST",
#                 headers: {"Content-Type": "application/json"},
#                 body: JSON.stringify({"text": text})
#             });
#             let result = await response.json();
#             document.getElementById("output").innerText = "Inserted: " + JSON.stringify(result);
#         }
#         async function getBestScore() {
#             let response = await fetch("/get_best");
#             let result = await response.json();
#             document.getElementById("output").innerText = "Best Document: " + JSON.stringify(result);
#         }
#     </script>
# </body>
# </html>
# """

# @app.get("/", response_class=HTMLResponse)
# def serve_page():
#     return HTMLResponse(content=html_content)

# @app.post("/insert")
# def insert_document(data: dict):
#     document = {"text": data.get("text", ""), "score": 100}  # Simulated score
#     res = es.index(index="documents", body=document)
#     return {"result": res["result"]}

# @app.get("/get_best")
# def get_best():
#     query = {"query": {"match_all": {}}, "size": 1, "sort": [{"score": "desc"}]}
#     res = es.search(index="documents", body=query)
#     return res["hits"]["hits"][0]["_source"] if res["hits"]["hits"] else {"error": "No documents found"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9567)


from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import requests

app = FastAPI()

# Serve HTML template
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get")
async def get_document():
    """
    Trigger 'get' action to retrieve the best matching document.
    """
    try:
        response = requests.get("http://backend:9567/get")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.post("/insert")
async def insert_document(text: str = Form(...)):
    """
    Trigger 'insert' action to add a new document.
    """
    try:
        response = requests.post("http://backend:9567/insert", json={"text": text})
        return response.json()
    except Exception as e:
        return {"error": str(e)}
    
# Run the server on port 9567 and make it public
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9567, reload=True)
