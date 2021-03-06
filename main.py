from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "name": "Andys",
        "age": 27,
        "height": "11111",
        "weight": "111111",
        "hobby": "I like to watch premier league football!!!",
        "update": "update되어서 dockerhub에 push check"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}