from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.restaurant import RestaurantSchema, ShowRestaurant
from models import restaurant
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/restaurants",
    tags=['Restaurants']
)


@router.get('/', response_model=List[ShowRestaurant], status_code=status.HTTP_200_OK)
def get_all_restaurants(db: Session = Depends(get_db)):
    restaurants = db.query(restaurant.Restaurant).filter(restaurant.Restaurant.isActive == True).all()
    
    return restaurants

@router.get('/{id}', response_model=ShowRestaurant, status_code=status.HTTP_200_OK)
def get_restaurant(id: str, db: Session = Depends(get_db)):
    single_restaurant = db.query(restaurant.Restaurant).filter(
        restaurant.Restaurant.id == id).first()

    if not single_restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant with id of {id} does not exist.")

    return single_restaurant


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_restaurant(request: RestaurantSchema, db: Session = Depends(get_db)):
    new_restaurant = restaurant.Restaurant(
        user_id=request.user_id, name=request.name, image=request.image, delivery_fee=request.delivery_fee, min_delivery_time=request.min_delivery_time, 
        max_delivery_time=request.max_delivery_time)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return new_restaurant

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_order(id: str, request: RestaurantSchema, db: Session = Depends(get_db)):
    single_restaurant = db.query(restaurant.RestaurantSchema).filter(restaurant.RestaurantSchema.id == id)
    if not single_restaurant.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant with id of {id} does not exist.")

    single_restaurant.update({'user_id': request.user_id, 'name': request.name, 'image': request.image, 'delivery_fee': request.delivery_fee,
                           'min_delivery_time': request.min_delivery_time, 'max_delivery_time': request.max_delivery_time, 'isActive': request.isActive
                        })
    db.commit()
    
    return "Restaurant updated"
