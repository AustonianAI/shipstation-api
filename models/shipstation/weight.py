from pydantic import BaseModel, validator, conint
from typing import Optional


class Weight(BaseModel):
    value: Optional[float] = None
    units: Optional[str] = None
    WeightUnits: Optional[conint(ge=0)] = None  # type: ignore # Using conint for a constrained integer type

    @validator('units')
    def validate_units(cls, v):
        if v not in {"pounds", "ounces", "grams"}:
            raise ValueError("units must be 'pounds', 'ounces', or 'grams'")
        return v

    @validator('WeightUnits', always=True)
    def set_weight_units(cls, v, values):
        units_mapping = {"pounds": 1, "ounces": 2, "grams": 3}
        units = values.get('units')
        if units:
            return units_mapping.get(units, None)
        return v

    class Config:
        use_enum_values = True
