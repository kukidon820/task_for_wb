# main.py

import subprocess
import threading
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Product, Base
from database import engine, SessionLocal
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import parser

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/parse")
def trigger_parser(query: str):
    products = parser.parse_wb(query)
    return JSONResponse(content={"products": products})


@app.post("/api/save")
def save_products(db: Session = Depends(get_db)):
    products = parser.parse_wb("iphone")
    for p in products:
        product = Product(**p)
        db.add(product)
    db.commit()
    return {"status": "saved", "count": len(products)}


@app.get("/api/products/")
def get_products(min_price: int = 0, max_price: int = 100000, min_rating: float = 0, min_reviews: int = 0, db: Session = Depends(get_db)):
    filters = []
    if min_price:
        filters.append(Product.price >= min_price)
    if max_price:
        filters.append(Product.price <= max_price)
    if min_rating:
        filters.append(Product.rating >= min_rating)
    if min_reviews:
        filters.append(Product.reviews >= min_reviews)

    products = db.query(Product).filter(and_(*filters)).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "sale_price": p.sale_price,
            "rating": p.rating,
            "reviews": p.reviews
        }
        for p in products
    ]


@app.on_event("startup")
def startup_event():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise "Something went wrong with connection database"
