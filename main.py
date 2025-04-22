from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Welcome"}

products = []

@app.post("/create_product")
async def create_product(product: Product):
    products.append(product)
    return {"message" : "product has been added"}

@app.get("/view_products")
async def view_products():
    return {"products": products}