from datetime import datetime

from fastapi import Query
from pydantic import BaseModel, validator
from typing import Dict, Optional, Any, List


class CommonResponse(BaseModel):
    timeGenerated: datetime
    message: str = None


class ResponseOut(CommonResponse):
    result: Dict[str, Any]


class CreateProductIn(BaseModel):
    name: str
    price: float
    description: str

    @validator('price')
    def price_must_be_positive(cls, value):
        if value < 0:
            raise ValueError('Price must be greater than or equal to zero.')
        return value


class AllResponseOut(CommonResponse):
    result: List[Dict[str, Any]]


class GetAllProductsIn(BaseModel):
    page_number: Optional[int] = Query(1, ge=1)
    page_size: Optional[int] = Query(10, ge=1)


class UpdateProductIn(BaseModel):
    name: str = None
    price: float = None
    description: str = None

    @validator('price')
    def price_must_be_positive(cls, value):
        if value < 0:
            raise ValueError('Price must be greater than or equal to zero.')
        return value
