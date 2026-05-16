from fastapi import FastAPI
from elasticsearch import Elasticsearch
import os

app = FastAPI()

# Connect to Elasticsearch running on host machine
ELASTIC_HOST = os.environ.get("ELASTIC_HOST", "http://host.docker.internal:9200")

es = Elasticsearch(ELASTIC_HOST)

@app.get("/")
def home():
    try:
        # Check Elasticsearch connection
        info = es.info()

        return {
            "message": "FastAPI + Elasticsearch Connected Successfully",
            "cluster_name": info["cluster_name"],
            "elasticsearch_version": info["version"]["number"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/create/{index_name}")
def create_index(index_name: str):
    try:
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)

        return {
            "message": f"Index '{index_name}' created successfully"
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/insert/{index_name}/{doc_id}")
def insert_document(index_name: str, doc_id: int):
    try:
        document = {
            "name": "Ganesh",
            "technology": "FastAPI + Elasticsearch"
        }

        response = es.index(
            index=index_name,
            id=doc_id,
            document=document
        )

        return {
            "message": "Document inserted",
            "response": response["result"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }
