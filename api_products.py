from fastapi import FastAPI
app = FastAPI()


@app.get("/products")
def read_products():
    return [1, 2, 3]


# pip install fastapi uvicorn
# uvicorn main:app --reload
