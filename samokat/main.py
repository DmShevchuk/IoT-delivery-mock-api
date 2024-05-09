from typing import List
from fastapi import FastAPI, Header, Response, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI()


class Product(BaseModel):
    title: str
    price: float


product_list = []


@app.post("/samokat/api/v1/products")
async def add_products(products: List[Product],
                       login: str = Header(None),
                       password: str = Header(None)):
    check_auth(login, password)

    product_list.clear()

    for product in products:
        product_list.append(product)

    return Response(content=None, status_code=200)


@app.get("/samokat/api/v1/products")
async def get_products(login: str = Header(None),
                       password: str = Header(None)):
    check_auth(login, password)

    return product_list


@app.put("/samokat/api/v1/products")
async def find_products(product_names: List[str],
                        login: str = Header(None),
                        password: str = Header(None)):
    check_auth(login, password)

    result = []
    total_cost = 0

    for product_name in product_names:
        for product in product_list:
            if product.title.lower() == product_name.lower():
                result.append({"title": product.title, "price": product.price})
                total_cost += product.price
                break

    return {"products": result, "total_cost": total_cost}


def check_auth(login: str, password: str):
    try:
        decoded_login = base64.b64decode(login).decode('utf-8') if login else None
        decoded_password = base64.b64decode(password).decode('utf-8') if password else None
    except:
        raise HTTPException(status_code=401, detail="Invalid login or password")

    if decoded_login != "admin" or decoded_password != "qwerty$4":
        raise HTTPException(status_code=401, detail="Invalid login or password")
