from datetime import datetime

from pydantic import BaseModel, validator
from typing import Dict, Any


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
