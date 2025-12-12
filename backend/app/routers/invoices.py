from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"],
)


@router.post("/", response_model=schemas.Invoice)
def create_invoice(
    invoice: schemas.InvoiceCreate,
    db: Session = Depends(get_db),
):
    db_invoice = models.Invoice(**invoice.model_dump())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


@router.get("/", response_model=List[schemas.Invoice])
def list_invoices(db: Session = Depends(get_db)):
    return db.query(models.Invoice).all()


@router.get("/{invoice_id}", response_model=schemas.Invoice)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

