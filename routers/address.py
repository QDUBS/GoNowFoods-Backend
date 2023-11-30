from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from schemas.user import UserSchema
from schemas.address import AddressSchema, ShowAddress
from models import address
from db.database import get_db
from utils.oauth2 import get_current_user
from enum import Enum

router = APIRouter(
    prefix="/addresses",
    tags=['Addresses']
)

class Type(str, Enum):
    HOME = "HOME"
    WORK = "WORK"
    REGULAR = "REGULAR"

@router.get('/{user_id}', response_model=ShowAddress, status_code=status.HTTP_200_OK)
def get_address(user_id: str, db: Session = Depends(get_db)):
    single_address = db.query(address.Address).filter(address.Address.user_id == user_id).first()

    if not single_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id of {id} does not exist.")

    return single_address


@router.get('/home/{user_id}', response_model=ShowAddress, status_code=status.HTTP_200_OK)
def get_home_address(user_id: str, db: Session = Depends(get_db)):
    single_address = db.query(address.Address).filter(
        address.Address.user_id == user_id, 
        address.Address.type == Type.HOME
    ).first()

    if not single_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id of {id} does not exist.")

    return single_address


@router.get('/work/{user_id}', response_model=ShowAddress, status_code=status.HTTP_200_OK)
def get_work_address(user_id: str, db: Session = Depends(get_db)):
    single_address = db.query(address.Address).filter(
        address.Address.user_id == user_id, 
        address.Address.type == Type.WORK
    ).first()

    if not single_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id of {id} does not exist.")

    return single_address


@router.get('/regular/{user_id}', response_model=ShowAddress, status_code=status.HTTP_200_OK)
def get_regular_address(user_id: str, db: Session = Depends(get_db)):
    single_address = db.query(address.Address).filter(
        address.Address.user_id == user_id, 
        address.Address.type == Type.REGULAR
    ).first()

    if not single_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id of {id} does not exist.")

    return single_address


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_address(request: AddressSchema, db: Session = Depends(get_db)):
    new_address = address.Address(user_id=request.user_id, house_no=request.house_no, street1=request.street1, street2=request.street2, city=request.city, state=request.state, 
                                country=request.country, postal_code=request.postal_code, latitude=request.latitude, longitude=request.longitude,
                                type=request.type)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)

    return new_address

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_address(id: str, request: AddressSchema, db: Session = Depends(get_db)):
    single_address = db.query(address.Address).filter(address.Address.id == id)
    if not single_address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id of {id} does not exist.")

    single_address.update({'user_id': request.user_id, 'house_no': request.house_no, 'street1': request.street1, 'street2': request.street2, 'city': request.city, 
                           'state': request.state, 'country': request.country, 'postal_code': request.postal_code, 'latitude': request.latitude,
                           'longitude': request.longitude, 'type': request.type
                        })
    db.commit()
    
    return "Address updated"

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_address(id: str, db: Session = Depends(get_db)):
    single_address = db.query(address.Address).filter(address.Address.id == id).first()

    if not single_address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Address with id {id} not found",
        )
    
    db.delete(single_address)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

