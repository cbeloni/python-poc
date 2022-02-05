from typing import Optional
from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from uvicorn import run

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/item/{item}")
def read_item(item: int, q: Optional[str] = None):
    return {"item": item, "q": q}

@app.get("/error/{item}")
def read_item(item: int, q: Optional[str] = None):
    if item == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    if item == 2:
        raise RequestValidationError(errors=["item não pode ser 2"])
    return {"item": item, "q": q}

if __name__ == '__main__':
    run("app_fastapi:app", port=8000, reload=True, access_log=False)
    