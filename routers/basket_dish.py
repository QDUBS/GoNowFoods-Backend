from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.basket_dish import BasketDishSchema, ShowBasketDish
from models import basket_dish
from db.database import get_db
from utils.hashing import Hash
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/basket-dishes",
    tags=['Basket Dishes']
)


@router.get('/', response_model=List[ShowBasketDish], status_code=status.HTTP_200_OK)
def get_basket_dishes(basket_id: str, db: Session = Depends(get_db)):
    basket_dishes = db.query(basket_dish.BasketDish).filter(basket_dish.BasketDish.basket_id == basket_id).all()

    return basket_dishes

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_basket_dish(request: BasketDishSchema, db: Session = Depends(get_db)):
    new_basket_dish = basket_dish.BasketDish(basket_id=request.basket_id, dish_id=request.dish_id, quantity=request.quantity)
    db.add(new_basket_dish)
    db.commit()
    db.refresh(new_basket_dish)

    return new_basket_dish

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_basket_dish(id: str, db: Session = Depends(get_db)):
    single_basket_dish = db.query(basket_dish.BasketDish).filter(basket_dish.BasketDish.id == id).first()

    if not single_basket_dish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Basket dish with id {id} not found",
        )
    
    db.delete(single_basket_dish)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
