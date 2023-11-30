from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import database
from models import user, profile, address, basket, basket_dish, dish, order_dish, order, restaurant, advert, favorite, promotion, subscription, support_ticket, user_promotion_association
from routers import user as user_router, authentication as authentication_router, address as address_router, basket_dish as basket_dish_router, basket as basket_router, courier as courier_router, dish as dish_router, order_dish as order_dish_router, order as order_router, profile as profile_router, restaurant as restaurant_router, advert as advert_router, favorite as favorite_router, promotion as promotion_router, subscription as subscription_router, support_ticket as support_ticket_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
user.Base.metadata.create_all(bind=database.engine)
profile.Base.metadata.create_all(bind=database.engine)
address.Base.metadata.create_all(bind=database.engine)
order.Base.metadata.create_all(bind=database.engine)
basket.Base.metadata.create_all(bind=database.engine)
basket_dish.Base.metadata.create_all(bind=database.engine)
order.Base.metadata.create_all(bind=database.engine)
dish.Base.metadata.create_all(bind=database.engine)
order_dish.Base.metadata.create_all(bind=database.engine)
order.Base.metadata.create_all(bind=database.engine)
order.Base.metadata.create_all(bind=database.engine)
restaurant.Base.metadata.create_all(bind=database.engine)
advert.Base.metadata.create_all(bind=database.engine)
favorite.Base.metadata.create_all(bind=database.engine)
promotion.Base.metadata.create_all(bind=database.engine)
subscription.Base.metadata.create_all(bind=database.engine)
support_ticket.Base.metadata.create_all(bind=database.engine)
user_promotion_association.Base.metadata.create_all(bind=database.engine)

# Routers
app.include_router(user_router.router)
app.include_router(authentication_router.router)
app.include_router(address_router.router)
app.include_router(basket_dish_router.router)
app.include_router(basket_router.router)
app.include_router(dish_router.router)
app.include_router(order_dish_router.router)
app.include_router(order_router.router)
app.include_router(profile_router.router)
app.include_router(restaurant_router.router)
app.include_router(advert_router.router)
app.include_router(favorite_router.router)
app.include_router(promotion_router.router)
app.include_router(subscription_router.router)
app.include_router(support_ticket_router.router)

@app.get("/")
def index():
    return { "details": "GoNow Foods API" }
