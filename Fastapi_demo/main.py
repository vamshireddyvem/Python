from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import Database_models
from models import Product
from Database_config import session,engine

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
    )
    

products=[
    Product(id=1,name='laptop',description='high performace laptop with m5',quantity= 3, price=2999.99),
       Product(id=2,name='32 inch Monitor',description='100hz UHD Monitor',quantity= 32,price=999.99),
       Product(id=3,name='Docking station',description='muti display support up to 4k',quantity= 34,price=99.99),
       Product(id=4,name='Desk',description='10 ft standing desk',quantity= 35,price=599.99)
]
Database_models.Base.metadata.create_all(bind=engine)


def init_db():
    db=session()
    try:
        count=db.query(Database_models.Product).count()
        if count ==0:
            for product in products:
                db.add(Database_models.Product(**product.model_dump()))
            db.commit()
    finally:
        db.close()
init_db()


def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return "welcome to the application"

@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(Database_models.Product).all()

    return db_products


@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    db_product=db.query(Database_models.Product).filter(Database_models.Product.id==id).first()
    if db_product:
        return db_product
    else:
        return "product not found"

@app.post("/products")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(Database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update(id:int, product:Product,db:Session=Depends(get_db)):
    db_product=db.query(Database_models.Product).filter(Database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "product Updated"
    else:  
        return "No Product found"


@app.delete("/products/{id}")
def delete_products(id:int,db:Session=Depends(get_db)):
    db_product=db.query(Database_models.Product).filter(Database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted"
    return "No product found"