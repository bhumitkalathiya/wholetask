from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Event, EmailSubscription
from scraper import scrape_events

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/events")
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events

@router.post("/subscribe")
def subscribe_email(email: str, event_link: str, db: Session = Depends(get_db)):
    existing_email = db.query(EmailSubscription).filter_by(email=email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already subscribed")
    
    new_subscription = EmailSubscription(email=email, event_link=event_link)
    db.add(new_subscription)
    db.commit()
    return {"message": "Subscribed successfully!"}

@router.get("/scrape")
def scrape_and_store(db: Session = Depends(get_db)):
    events = scrape_events()
    for event in events:
        db_event = Event(title=event["title"], date=event["date"], link=event["link"])
        db.add(db_event)
    db.commit()
    return {"message": "Scraped and stored events"}

