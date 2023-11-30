from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.courier import CourierSchema, ShowCourier
from models import order
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/couriers",
    tags=['Couriers']
)


@router.get('/', response_model=List[ShowCourier], status_code=status.HTTP_200_OK)
def get_all_couriers(db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    couriers = db.query(order.Courier).filter(order.Courier).all()

    return couriers


@router.get('/{id}', response_model=ShowCourier, status_code=status.HTTP_200_OK)
def get_courier(id: str, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    single_courier = db.query(order.Courier).filter(order.Courier.id == id).first()

    if not single_courier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Courier with id of {id} does not exist.")

    return single_courier


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_courier(request: CourierSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    new_courier = order.Courier(user_id=request.user_id, first_name=request.first_name, last_name=request.last_name, mobile_number=request.mobile_number,
                            photo=request.photo, transportation_mode=request.transportation_mode, rating=request.rating)
    db.add(new_courier)
    db.commit()
    db.refresh(new_courier)

    return new_courier
