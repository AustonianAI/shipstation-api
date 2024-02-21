from pydantic import BaseModel, validator
from typing import List, Optional

from models.shipstation.customs_item import CustomsItem


class InternationalOptions(BaseModel):
    contents: Optional[str] = None
    customsItems: Optional[List[CustomsItem]] = None
    nonDelivery: Optional[str] = None

    @validator('contents')
    def validate_contents(cls, v):
        valid_contents = {"merchandise", "documents", "gift", "returned_goods", "sample"}
        if v is not None and v not in valid_contents:
            raise ValueError(f"Contents must be one of {valid_contents}")
        return v

    @validator('nonDelivery')
    def validate_non_delivery(cls, v):
        valid_options = {"return_to_sender", "treat_as_abandoned"}
        if v is not None and v not in valid_options:
            raise ValueError(f"NonDelivery must be one of {valid_options}")
        return v

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True
