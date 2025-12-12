from pydantic import BaseModel, ConfigDict


class InvoiceBase(BaseModel):
    invoice_number: str
    total_amount: int
    status: str = "PENDING"


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    id: int
    owner_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
