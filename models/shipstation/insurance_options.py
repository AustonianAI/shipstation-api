from pydantic import BaseModel, validator
from typing import Optional


class InsuranceOptions(BaseModel):
    provider: Optional[str] = None
    insureShipment: Optional[bool] = None
    insuredValue: Optional[float] = None

    @validator('provider')
    def validate_provider(cls, v):
        valid_providers = {"shipsurance", "carrier", "provider", "xcover", "parcelguard"}
        if v is not None and v not in valid_providers:
            raise ValueError(f"Provider must be one of {valid_providers}")
        return v

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True
