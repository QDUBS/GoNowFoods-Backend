from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.dish import DishSchema, ShowDish
from models import dish
from db.database import get_db
from utils.hashing import Hash
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/dishes",
    tags=['Dishes']
)


@router.get('/', response_model=List[ShowDish], status_code=status.HTTP_200_OK)
def get_dishes(restaurant_id: str, db: Session = Depends(get_db)):
    dishes = db.query(dish.Dish).filter(dish.Dish.restaurant_id == restaurant_id).all()

    return dishes


@router.get('/{id}', response_model=ShowDish, status_code=status.HTTP_200_OK)
def get_dish(id: str, db: Session = Depends(get_db)):
    single_dish = db.query(dish.Dish).filter(dish.Dish.id == id).first()

    if not single_dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dish with id of {id} does not exist.")

    return single_dish

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_dish(request: DishSchema, db: Session = Depends(get_db)):
    new_dish = dish.Dish(restaurant_id=request.restaurant_id, name=request.name, image=request.image, description=request.description, price=request.price,
                         category=request.category, category_code=request.category_code,
                         )
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)

    return new_dish

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_dish(id: str, request: DishSchema, db: Session = Depends(get_db)):
    single_dish = db.query(dish.Dish).filter(dish.Dish.id == id)
    if not single_dish.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id of {id} does not exist.")

    single_dish.update({'restaurant_id': request.restaurant_id, 'name': request.name, 'image': request.image, 'description': request.description,
                           'price': request.price, 'category': request.category, 'category_code': request.category_code
                        })
    db.commit()
    
    return "Dish updated"
