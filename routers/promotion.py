from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.promotion import PromotionSchema, ShowPromotion
from models import promotion, user
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/promotions",
    tags=['Promotions']
)


@router.get('/', response_model=List[ShowPromotion], status_code=status.HTTP_200_OK)
def get_promotions(db: Session = Depends(get_db)):
    promotions = db.query(promotion.Promotion).all()

    return promotions


@router.get("/user/{user_id}/promotions", response_model=List[ShowPromotion])
def get_user_promotions(user_id: str, db: Session = Depends(get_db)):
    user = db.query(user.User).filter_by(id=user_id).all()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user.promotions


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_promotion(request: PromotionSchema, db: Session = Depends(get_db)):
    new_promotion = promotion.Promotion(
        name=request.name, description=request.description, duration=request.duration, status=request.status, code=request.code,
        cost=request.cost, percentage=request.percentage, count=request.count
    )
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)

    return new_promotion
