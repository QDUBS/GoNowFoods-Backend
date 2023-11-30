from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.advert import AdvertSchema, ShowAdvert
from schemas.user import UserSchema
from models import advert
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/adverts",
    tags=['Adverts']
)


@router.get('/', response_model=List[ShowAdvert], status_code=status.HTTP_200_OK)
def get_adverts(db: Session = Depends(get_db)):
    adverts = db.query(advert.Advert).all()

    return adverts


@router.get('/{id}', response_model=ShowAdvert, status_code=status.HTTP_200_OK)
def get_advert(id: str, db: Session = Depends(get_db)):
    single_advert = db.query(advert.Advert).filter(
        advert.Advert.id == id).first()

    if not single_advert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Advert with id of {id} does not exist.")

    return single_advert


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_advert(request: AdvertSchema, db: Session = Depends(get_db)):
    new_advert = advert.Advert(
        restaurant_id=request.restaurant_id, name=request.name, image=request.image, duration=request.duration, status=request.status)
    db.add(new_advert)
    db.commit()
    db.refresh(new_advert)

    return new_advert
