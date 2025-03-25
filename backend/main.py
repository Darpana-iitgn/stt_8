from fastapi import FastAPI, HTTPException, Form
from elasticsearch import Elasticsearch
import uvicorn

app = FastAPI()
es = Elasticsearch(["http://elasticsearch:9200"])

# Insert document
@app.post("/insert")
async def insert_document(text: str = Form(...)):
    try:
        # Get next ID
        search_result = es.search(index="india", body={"sort": [{"id": {"order": "desc"}}], "size": 1})
        new_id = str(int(search_result['hits']['hits'][0]['_source']['id']) + 1) if search_result['hits']['total']['value'] > 0 else "1"
        
        es.index(index="india", document={"id": new_id, "text": text})
        return {"status": "success", "inserted_id": new_id}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Search document 
@app.get("/search")
async def search_document(query: str):
    try:
        result = es.search(index="india", body={"query": {"match": {"text": query}}})
        return result['hits']['hits'][0]['_source'] if result['hits']['total']['value'] > 0 else {}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9567)