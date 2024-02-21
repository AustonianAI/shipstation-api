from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

from models.shipstation.weight import Weight


class OrderItem(BaseModel):
    orderItemId: Optional[int] = None
    lineItemKey: Optional[str] = None
    sku: Optional[str] = None
    name: str  # As per your description, this cannot be null
    imageUrl: Optional[HttpUrl] = None  # Using HttpUrl for URL validation
    weight: Optional[Weight] = None
    quantity: Optional[int] = None
    unitPrice: Optional[float] = None
    taxAmount: Optional[float] = None
    shippingAmount: Optional[float] = None
    warehouseLocation: Optional[str] = None
    options: List[str] = []
    productId: Optional[int] = None
    fulfillmentSku: Optional[str] = None
    adjustment: Optional[bool] = None
    upc: Optional[str] = None
    createDate: Optional[datetime] = None
    modifyDate: Optional[datetime] = None

    class Config:
        anystr_strip_whitespace = True
        use_enum_values = True
        orm_mode = True
