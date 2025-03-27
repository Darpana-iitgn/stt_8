from fastapi import FastAPI, HTTPException
from elasticsearch import Elasticsearch
import uvicorn

app = FastAPI()
es = Elasticsearch(["http://elasticsearch:9200"])

@app.get("/health")
def health_check():
    return {"status": "OK", "es_status": es.ping()}

@app.post("/insert")
async def insert_document(text: str):
    try:
        doc = {"text": text}
        res = es.index(index="india", document=doc)
        return {"id": res["_id"], "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search")
async def search_documents(query: str):
    try:
        res = es.search(
            index="india",
            body={"query": {"match": {"text": query}}}
        )
        return {
            "results": [hit["_source"] for hit in res["hits"]["hits"]],
            "count": res["hits"]["total"]["value"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9567)
