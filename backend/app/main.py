# -*- coding: utf-8 -*-
from fastapi import FastAPI

from .database import Base, engine
from .routers import invoices

# Crée les tables au démarrage (simple pour le dev local)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BillBox Backend")

app.include_router(invoices.router)


@app.get("/")
def read_root():
    return {"message": "BillBox backend is running"}
