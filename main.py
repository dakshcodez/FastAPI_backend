from fastapi import FastAPI, HTTPException, Form, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import Product
import authentication

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

# Register a user
@app.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    if username in authentication.users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = authentication.get_password_hash(password)
    authentication.users_db[username] = {
        "username": username,
        "full_name": username,
        "email": f"{username}@example.com",
        "hashed_password": hashed_password
    }
    return {"message": "User registered successfully"}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authentication.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(authentication.oauth2_scheme)):
    user = authentication.users_db.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return user