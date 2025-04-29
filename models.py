from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str
    keywords : tuple

class User(BaseModel):
    username: str
    full_name: str = ""
    email: str = ""
    