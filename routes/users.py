from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

# user api router
user_router = APIRouter(tags=["User"])


# dict to store users
users = {}


# user signup route
@user_router.post('/signup')
async def sign_up_user(data:User):
    print(data.model_dump())

    #if email is already registered
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user already exists with email"
        )

    # else add user in dict
    users[data.email] = data

    return {
        "message" : "signup successful."
    }


# user sign in route
@user_router.post('/signin')
async def sign_in_user(data:UserSignIn):
    # returning unauthorized response if email does not exists or password not matches
    if data.email not in users or users[data.email].password != data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials"
        )

    return {
        "message" : "sigin successful."
    }
