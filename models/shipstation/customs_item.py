from pydantic import BaseModel, constr
from typing import Optional


class CustomsItem(BaseModel):
    customsItemId: Optional[str] = None  # Read-only field, included for completeness
    description: str
    quantity: int
    value: float
    harmonizedTariffCode: Optional[str] = None
    countryOfOrigin: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
