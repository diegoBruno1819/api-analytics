from datetime import date
from uuid import UUID
from decimal import Decimal
from typing import Annotated
from pydantic import BaseModel, Field, field_validator, StringConstraints, computed_field, ConfigDict

# Definición de restricciones para cadenas de texto
Str100 = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
Str50 = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)]
CurrencyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=3, max_length=3, pattern=r'^[A-Za-z]{3}$')]

class Sale(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: UUID
    date: date
    product: Str100
    category: Str50
    region: Str100
    quantity: Annotated[int, Field(gt=0)]
    unit_price: Annotated[Decimal, Field(gt=0, decimal_places=2)]
    currency: CurrencyStr

    @field_validator("date")
    @classmethod
    def validate_date(cls, v: date) -> date:
        if v > date.today():
            raise ValueError("La fecha no puede ser futura")
        return v

    @field_validator("currency", mode="before")
    @classmethod
    def normalize_currency(cls, v: object) -> object:
        if isinstance(v, str):
            return v.upper()
        return v

    @computed_field
    @property
    def total_amount(self) -> Decimal:
        return (Decimal(self.quantity) * self.unit_price).quantize(Decimal("0.01"))
