from pydantic import BaseModel, validator
from typing import Optional


class Dimensions(BaseModel):
    length: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    units: Optional[str] = None

    @validator('units')
    def validate_units(cls, v):
        if v not in {"inches", "centimeters"}:
            raise ValueError("Units must be either 'inches' or 'centimeters'")
        return v

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True
