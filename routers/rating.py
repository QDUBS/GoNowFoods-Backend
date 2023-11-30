from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.rating import RatingSchema, ShowRating
from models import rating
from db.database import get_db
from utils.hashing import Hash
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/ratings",
    tags=['Ratings']
)


@router.get('/', response_model=List[ShowRating], status_code=status.HTTP_200_OK)
def get_user_ratings(user_id: str, db: Session = Depends(get_db)):
    ratings = db.query(rating.Rating).filter(rating.Rating.user_id == user_id).all()

    return ratings

@router.get('/', response_model=List[ShowRating], status_code=status.HTTP_200_OK)
def get_restaurant_ratings(restaurant_id: str, db: Session = Depends(get_db)):
    ratings = db.query(rating.Rating).filter(rating.Rating.restaurant_id == restaurant_id).all()

    return ratings

@router.get('/', response_model=List[ShowRating], status_code=status.HTTP_200_OK)
def get_dish_ratings(dish_id: str, db: Session = Depends(get_db)):
    ratings = db.query(rating.Rating).filter(rating.Rating.dish_id == dish_id).all()

    return ratings


@router.get('/{id}', response_model=ShowRating, status_code=status.HTTP_200_OK)
def get_rating(id: str, db: Session = Depends(get_db)):
    single_rating = db.query(rating.Rating).filter(rating.Rating.id == id).first()

    if not single_rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Rating with id of {id} does not exist.")

    return single_rating

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_rating(request: RatingSchema, db: Session = Depends(get_db)):
    new_rating = rating.Rating(user_id=request.user_id, restaurant_id=request.restaurant_id, dish_id=request.dish_id, rating_no=request.rating_no, 
                               comment=request.comment
                            )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)

    return new_rating
