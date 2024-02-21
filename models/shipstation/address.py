from pydantic import BaseModel, constr
from typing import Optional


class Address(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    street3: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    residential: Optional[bool] = None
    addressVerified: Optional[str] = None

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True
