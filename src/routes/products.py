from beanie import WriteRules
from fastapi import APIRouter

from src.schemas.products import *
from src.models.models import Product

product_route = APIRouter(prefix="/product")


@product_route.post("/", tags=["Products"])
async def create_product(args: CreateProductIn):
    record = Product(**args.model_dump(mode="json"))
    await record.insert(link_rule=WriteRules.WRITE)
    record_dict = record.dict()
    record_dict.pop("id")
    return ResponseOut(result=record_dict,
                       timeGenerated=datetime.now(),
                       message="Product added successfully"
                       )
