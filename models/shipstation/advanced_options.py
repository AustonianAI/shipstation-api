from pydantic import BaseModel, constr
from typing import List, Optional


class AdvancedOptions(BaseModel):
    warehouseId: Optional[int] = None
    nonMachinable: Optional[bool] = None
    saturdayDelivery: Optional[bool] = None
    containsAlcohol: Optional[bool] = None
    storeId: Optional[int] = None
    customField1: Optional[str] = None
    customField2: Optional[str] = None
    customField3: Optional[str] = None
    source: Optional[str] = None
    mergedOrSplit: Optional[bool] = None  # Read-Only
    mergedIds: Optional[List[int]] = None  # Read-Only
    parentId: Optional[int] = None  # Read-Only
    billToParty: Optional[str] = None
    billToAccount: Optional[str] = None
    billToPostalCode: Optional[str] = None
    billToCountryCode: Optional[constr(regex=r'^[A-Z]{2}$')] = None  # type: ignore
    billToMyOtherAccount: Optional[str] = None

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True
