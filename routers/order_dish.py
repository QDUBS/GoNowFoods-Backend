from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.order_dish import OrderDishSchema, ShowOrderDish
from models import order_dish
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/order-dishes",
    tags=['Order Dishes']
)


@router.get('/', response_model=List[ShowOrderDish], status_code=status.HTTP_200_OK)
def get_order_dishes(order_id: str, db: Session = Depends(get_db)):
    order_dishes = db.query(order_dish.OrderDish).filter(order_dish.OrderDish.order_id == order_id).all()

    return order_dishes


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_order_dish(request: OrderDishSchema, db: Session = Depends(get_db)):
    new_order_dish = order_dish.OrderDish(dish_id=request.dish_id, order_id=request.order_id, quantity=request.quantity)
    db.add(new_order_dish)
    db.commit()
    db.refresh(new_order_dish)

    return new_order_dish
