from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.support_ticket import SupportTicketSchema, ShowSupportTicket
from schemas.user import UserSchema
from models import support_ticket
from db.database import get_db
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/support_tickets",
    tags=['Support Tickets']
)


@router.get('/', response_model=List[ShowSupportTicket], status_code=status.HTTP_200_OK)
def get_support_tickets(db: Session = Depends(get_db)):
    support_tickets = db.query(support_ticket.SupportTicket).all()

    return support_tickets


@router.get('/{id}', response_model=ShowSupportTicket, status_code=status.HTTP_200_OK)
def get_support_ticket(id: str, db: Session = Depends(get_db)):
    single_support_ticket = db.query(support_ticket.SupportTicket).filter(
        support_ticket.SupportTicket.id == id).first()

    if not single_support_ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Support ticket with id of {id} does not exist.")

    return single_support_ticket


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_support_ticket(request: SupportTicketSchema, db: Session = Depends(get_db)):
    new_support_ticket = support_ticket.SupportTicket(
        user_id=request.user_id, issue=request.issue, subject=request.subject, message=request.message)
    db.add(new_support_ticket)
    db.commit()
    db.refresh(new_support_ticket)

    return new_support_ticket
