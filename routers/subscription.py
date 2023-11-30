from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.subscription import SubscriptionSchema, ShowSubscription
from models import subscription
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/subscriptions",
    tags=['Subscriptions']
)


@router.get('/', response_model=List[ShowSubscription], status_code=status.HTTP_200_OK)
def get_subscriptions(db: Session = Depends(get_db)):
    subscriptions = db.query(subscription.Subscription).all()

    return subscriptions


@router.get('/{id}', response_model=ShowSubscription, status_code=status.HTTP_200_OK)
def get_subscription(id: str, db: Session = Depends(get_db)):
    single_subscription = db.query(subscription.Subscription).filter(
        subscription.Subscription.id == id).first()

    if not single_subscription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Subscription with id of {id} does not exist.")

    return single_subscription


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_subscription(request: SubscriptionSchema, db: Session = Depends(get_db)):
    new_subscription = subscription.Subscription(
        restaurant_id=request.restaurant_id, name=request.name, duration=request.duration, type=request.type, cost=request.cost)
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)

    return new_subscription


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_subscription(id: str, request: SubscriptionSchema, db: Session = Depends(get_db)):
    single_subscription = db.query(subscription.Subscription).filter(subscription.Subscription.id == id)
    if not single_subscription.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Subscription with id of {id} does not exist.")

    single_subscription.update({'restaurant_id': request.restaurant_id, 'name': request.name, 'duration': request.duration, 'type': request.type,
                           'cost': request.cost})
    db.commit()
    
    return "Subscription updated"
