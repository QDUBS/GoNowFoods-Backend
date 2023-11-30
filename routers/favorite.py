from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.favorite import FavoriteSchema, ShowFavorite
from schemas.user import UserSchema
from models import favorite
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/favorites",
    tags=['Favorites']
)


@router.get('/', response_model=List[ShowFavorite], status_code=status.HTTP_200_OK)
def get_favorites(db: Session = Depends(get_db)):
    favorites = db.query(favorite.Favorite).all()

    return favorites


@router.get('/restaurants', response_model=ShowFavorite, status_code=status.HTTP_200_OK)
def get_user_favorite_restaurants(user_id: str, db: Session = Depends(get_db)):
    favorite_restaurants = db.query(favorite.Favorite).filter(
        favorite.Favorite.user_id == user_id,
    ).all()

    if not favorite_restaurants:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Favorite restaurants for user with id of {id} not found.")

    return favorite_restaurants


@router.get('/dishes', response_model=ShowFavorite, status_code=status.HTTP_200_OK)
def get_user_favorite_dishes(user_id: str, db: Session = Depends(get_db)):
    favorite_dishes = db.query(favorite.Favorite).filter(
        favorite.Favorite.user_id == user_id,
    ).all()

    if not favorite_dishes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Favorite dishes for user with id of {id} not found.")

    return favorite_dishes


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_favorite(request: FavoriteSchema, db: Session = Depends(get_db)):
    new_favorite = favorite.Favorite(
        user_id=request.user_id, restaurant_id=request.restaurant_id, dish_id=request.dish_id, type=request.type)
    db.add(new_favorite)
    db.commit()
    db.refresh(new_favorite)

    return new_favorite


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_favorite(id: str, db: Session = Depends(get_db)):
    single_favorite = db.query(favorite.Favorite).filter(favorite.Favorite.id == id).first()

    if not single_favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Favorite with id {id} not found",
        )
    
    db.delete(single_favorite)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
