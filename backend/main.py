from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

# Configurer CORS pour autoriser les requêtes provenant de http://localhost:4200
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Autoriser les requêtes de cette origine
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

client = MongoClient("mongodb://admin:password@mongo:27017/")
db = client.todolist
collection = db.todos

class TodoItem(BaseModel):
    content: str

@app.post("/todos/")
def create_todo_item(item: TodoItem):
    result = collection.insert_one(item.dict())
    return {"_id": str(result.inserted_id), "content": item.content}

@app.get("/todos/")
def get_todo_items():
    todos = []
    for item in collection.find():
        item['_id'] = str(item['_id'])
        todos.append(item)
    return todos

@app.delete("/todos/{item_id}")
def delete_todo_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

