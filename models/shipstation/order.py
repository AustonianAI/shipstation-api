from pydantic import BaseModel, EmailStr
from typing import List, Optional, Union
from datetime import datetime

from models.shipstation.address import Address
from models.shipstation.advanced_options import AdvancedOptions
from models.shipstation.insurance_options import InsuranceOptions
from models.shipstation.international_options import InternationalOptions
from models.shipstation.order_items import OrderItem
from models.shipstation.weight import Weight
from models.shipstation.dimensions import Dimensions


class Order(BaseModel):
    orderId: Optional[int] = None
    orderNumber: Optional[str] = None
    orderKey: Optional[str] = None
    orderDate: Optional[datetime] = None
    createDate: Optional[datetime] = None
    modifyDate: Optional[datetime] = None
    paymentDate: Optional[datetime] = None
    shipByDate: Optional[datetime] = None
    orderStatus: Optional[str] = None
    customerId: Optional[int] = None
    customerUsername: Optional[str] = None
    customerEmail: Optional[EmailStr] = None
    billTo: Optional[Address] = None
    shipTo: Optional[Address] = None
    items: List[OrderItem] = []
    orderTotal: Optional[float] = None
    amountPaid: Optional[float] = None
    taxAmount: Optional[float] = None
    shippingAmount: Optional[float] = None
    customerNotes: Optional[str] = None
    internalNotes: Optional[str] = None
    gift: Optional[bool] = None
    giftMessage: Optional[str] = None
    paymentMethod: Optional[str] = None
    requestedShippingService: Optional[str] = None
    carrierCode: Optional[str] = None
    serviceCode: Optional[str] = None
    packageCode: Optional[str] = None
    confirmation: Optional[str] = None
    shipDate: Optional[datetime] = None
    holdUntilDate: Optional[datetime] = None
    weight: Optional[Weight] = None
    dimensions: Optional[Dimensions] = None
    insuranceOptions: Optional[InsuranceOptions] = None
    internationalOptions: Optional[InternationalOptions] = None
    advancedOptions: Optional[AdvancedOptions] = None
    tagIds: Optional[List[int]] = None
    userId: Optional[str] = None
    externallyFulfilled: Optional[bool] = None
    externallyFulfilledBy: Optional[str] = None
