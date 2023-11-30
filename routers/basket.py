from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.basket import BasketSchema, ShowBasket
from models import basket
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/baskets",
    tags=['Baskets']
)


@router.get('/', response_model=List[ShowBasket], status_code=status.HTTP_200_OK)
def get_all_baskets(user_id: str, db: Session = Depends(get_db)):
    baskets = db.query(basket.Basket).filter(basket.Basket.user_id == user_id).all()

    return baskets


@router.get('/restaurant', status_code=status.HTTP_200_OK)
def get_user_restaurant_basket(user_id: str, restaurant_id: str, db: Session = Depends(get_db)):
    single_basket = db.query(basket.Basket).filter(
        basket.Basket.user_id == user_id,
        basket.Basket.restaurant_id == restaurant_id
    ).first()

    return single_basket


@router.get('/{id}', response_model=ShowBasket, status_code=status.HTTP_200_OK)
def get_basket(id: str, db: Session = Depends(get_db)):
    single_basket = db.query(basket.Basket).filter(basket.Basket.id == id).first()

    if not single_basket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Basket with id of {id} does not exist.")

    return single_basket


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_basket(request: BasketSchema, db: Session = Depends(get_db)):
    new_basket = basket.Basket(user_id=request.user_id, restaurant_id=request.restaurant_id)
    db.add(new_basket)
    db.commit()
    db.refresh(new_basket)

    return new_basket


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_basket(id: str, db: Session = Depends(get_db)):
    single_basket = db.query(basket.Basket).filter(basket.Basket.id == id).first()

    if not single_basket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Basket with id {id} not found",
        )
    
    db.delete(single_basket)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
