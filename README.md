📘 HTTP Methods in FastAPI: GET, POST, PUT, and DELETE

FastAPI allows you to create endpoints that respond to different HTTP methods. Here's a summary of the most common ones:

🔹 GET  
Used to retrieve data.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Example item"}
```

🔹 POST  
Used to create a new resource.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
```

🔹 PUT  
Used to fully update an existing resource.

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}
```

🔹 DELETE  
Used to delete a resource.

```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

✅ Summary:

| Method | Action                       | Example Use                  |
|--------|------------------------------|-------------------------------|
| GET    | Retrieve data                | View a product                |
| POST   | Create a new resource        | Add a new product             |
| PUT    | Fully update a resource      | Edit an existing product      |
| DELETE | Delete a resource            | Remove a product              |
