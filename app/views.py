from fastapi import APIRouter, Form, HTTPException, status
from typing import Annotated
from db.core import get_connection
from schemas import Currency

router = APIRouter()

@router.get("/currencies")
def get_all_currencies():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            return cursor.execute("SELECT * FROM Currencies").fetchall() # выводит [[], []] а надо [{}, {}]
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/currency/{currency_code}")
def get_currency(currency_code: str):
    try:
        with get_connection() as connection:
            print(connection.row_factory)
            cursor = connection.cursor()
            return cursor.execute(f"SELECT * FROM Currencies WHERE Code = '{currency_code}'").fetchall()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.post("/currencies", status_code=status.HTTP_201_CREATED)
def add_currency(currency: Annotated[Currency, Form()]) -> dict:
    return {
        "name": currency.name,
        "code": currency.code,
        "sign": currency.sign
    }

    