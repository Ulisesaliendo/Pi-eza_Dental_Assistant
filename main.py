from fastapi import FastAPI
from app.db.database import engine, Base
from app.db import models

app = FastAPI(title="Dental Assistant API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "ok"}
