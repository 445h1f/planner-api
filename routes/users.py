from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn
from beanie import PydanticObjectId
from database.connection import Database

# user api router
user_router = APIRouter(tags=["User"])
# user database
user_database = Database(User)



# user signup route
@user_router.post('/signup')
async def sign_up_user(user_data:User) -> dict:
    # first check if user with email exists or not
    user_exists = await User.find_one(User.email == user_data.email)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="email already registered."
        )


    await user_database.save(user_data)

    return {
        "message" : "signup successful."
    }


# user sign in route
@user_router.post('/signin')
async def sign_in_user(user_data:UserSignIn):
    # check for email
    user_exist = await User.find_one(User.email == user_data.email)

    if not user_exist or user_exist.password != user_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials"
        )

    return {
        "message" : "sigin successful."
    }
