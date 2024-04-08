from beanie import Document


class Product(Document):
    name: str
    price: float
    description: str
