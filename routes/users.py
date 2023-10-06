from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.users import User, TokenResponse
from beanie import PydanticObjectId
from database.connection import Database
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token

# user api router
user_router = APIRouter(tags=["User"])
# user database
user_database = Database(User)

# password hashing
hash_password = HashPassword()


# user signup route
@user_router.post('/signup')
async def sign_up_user(user: User) -> dict:
    # first check if user with email exists or not
    user_exists = await User.find_one(User.email == user.email)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="email already registered."
        )

    # hashing password
    hashed_pwd = hash_password.create_hash(user.password)
    user.password = hashed_pwd

    await user_database.save(user)

    return {
        "message": "signup successful."
    }


# user sign in route
@user_router.post('/signin', response_model=TokenResponse)
async def sign_in_user(user: OAuth2PasswordRequestForm = Depends()):
    # check for email
    user_exist = await User.find_one(User.email == user.username)

    # checks if user exists or password matches
    if not user_exist or not hash_password.verify_hash(user.password, user_exist.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials"
        )
    # creating access token and returning it
    access_token = create_access_token(user_exist.email)

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
