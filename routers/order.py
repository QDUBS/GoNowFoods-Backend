from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.order import OrderSchema, ShowOrder
from models import order
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=['Orders']
)


@router.get('/', response_model=List[ShowOrder], status_code=status.HTTP_200_OK)
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(order.Order).filter(order.Order).all()

    return orders


@router.get('/user', response_model=List[ShowOrder], status_code=status.HTTP_200_OK)
def get_user_orders(user_id: str, db: Session = Depends(get_db)):
    orders = db.query(order.Order).filter(order.Order.user_id == user_id).all()

    return orders


@router.get('/restaurant', response_model=List[ShowOrder], status_code=status.HTTP_200_OK)
def get_restaurant_orders(restaurant_id: str, db: Session = Depends(get_db)):
    orders = db.query(order.Order).filter(order.Order.restaurant_id == restaurant_id).all()

    return orders


@router.get('/courier', response_model=List[ShowOrder], status_code=status.HTTP_200_OK)
def get_ready_orders(status: str, db: Session = Depends(get_db)):
    orders = db.query(order.Order).filter(order.Order.status == status).all()

    return orders


@router.get('/{id}', response_model=ShowOrder, status_code=status.HTTP_200_OK)
def get_order(id: str, db: Session = Depends(get_db)):
    single_order = db.query(order.Order).filter(order.Order.id == id).first()

    if not single_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id of {id} does not exist.")

    return single_order


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_order(request: OrderSchema, db: Session = Depends(get_db)):
    new_order = order.Order(user_id=request.user_id, courier_id=request.courier_id, restaurant_id=request.restaurant_id, total=request.total,
                            status=request.status)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_order(id: str, request: OrderSchema, db: Session = Depends(get_db)):
    single_order = db.query(order.Order).filter(order.Order.id == id)
    if not single_order.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id of {id} does not exist.")

    single_order.update({'user_id': request.user_id, 'courier_id': request.courier_id, 'restaurant_id': request.restaurant_id, 'total': request.total,
                           'status': request.status
                        })
    db.commit()
    
    return "Order updated"
