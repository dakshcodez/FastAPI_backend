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
@app.get("/search_by_category/{category}")
async def search_product_by_category(category: str):
    search_res: Product = []
    for product in products:
        if product.category == category:
            search_res.append(product)
    return {"search results": search_res}

# Search for a product by keywords
@app.get("/search_by_keyword/{search_keyword}")
async def search_product_by_keyword(search_keyword: str):
    search_res: Product = []
    for product in products:
        for keyword in product.keywords:
            if search_keyword == keyword:
                search_res.append(product)
                break
    return {"search results": search_res}