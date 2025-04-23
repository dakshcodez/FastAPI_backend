from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Welcome"}

products = []

# Create a product
@app.post("/create_product")
async def create_product(product: Product):
    products.append(product)
    return {"message" : "product has been added"}

# View all products
@app.get("/view_products")
async def view_products():
    return {"products": products}

# Search for a product by category
@app.get("/search_products/{category}")
async def search_product_by_category(category: str):
    search_res = []
    for product in products:
        if product.category == category:
            search_res.append(product)
    return {"products": search_res}
