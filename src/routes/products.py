from beanie import WriteRules, PydanticObjectId

from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Path, HTTPException, Body

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


@product_route.get("/", tags=["Products"], response_model=AllResponseOut)
async def get_all_products(args: GetAllProductsIn = Depends(GetAllProductsIn)):
    records = await Product.find(limit=args.page_size, skip=(args.page_size * (args.page_number - 1))).to_list()
    serialized_records = jsonable_encoder(records)

    return AllResponseOut(result=serialized_records,
                          timeGenerated=datetime.now(),
                          message="Get Products Successfully"
                          )


@product_route.get("/{product_id}/", tags=["Products"], response_model=ResponseOut)
async def get_product(product_id: PydanticObjectId = Path(...)):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return ResponseOut(
        result=product.dict(by_alias=True),
        timeGenerated=datetime.now(),
        message="Product retrieved successfully"
    )


@product_route.get("/{product_id}/", tags=["Products"], response_model=ResponseOut)
async def update_product(product_id: PydanticObjectId = Path(...)):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return ResponseOut(
        result=product.dict(by_alias=True),
        timeGenerated=datetime.now(),
        message="Product retrieved successfully"
    )


@product_route.delete("/{product_id}/", tags=["Products"], response_model=ResponseOut)
async def delete_product(product_id: PydanticObjectId = Path(...)):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await product.delete()

    return ResponseOut(
        result={},
        timeGenerated=datetime.now(),
        message="Product deleted successfully"
    )


@product_route.put("/{product_id}/", tags=["Products"], response_model=ResponseOut)
async def update_product(product_id: PydanticObjectId = Path(...),
                         args: UpdateProductIn = Body(...)
                         ):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = args.dict()
    update_query = {"$set": {field: value for field, value in update_data.items() if value is not None}}
    await product.update(update_query)

    return ResponseOut(
        result=product.dict(by_alias=True),
        timeGenerated=datetime.now(),
        message="Product updated successfully"
    )
