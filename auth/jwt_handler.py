import time
from datetime import datetime
from jose import jwt, JWTError
from fastapi import HTTPException, status
from database.connection import Settings


settings = Settings()


# function to create jwt token
def create_access_token(user: str) -> str:
    payload = {
        "user": user,
        "expires": time.time() + 3600  # token will expire after 60 mins of creation
    }

    token = jwt.encode(payload, key=settings.SECRET_KEY, algorithm='HS256')

    return token


# verifies jwt token and returns invalid response
def verify_access_token(token: str) -> dict:
    try:
        # decoding jwt
        data = jwt.decode(token=token, key=settings.SECRET_KEY,
                          algorithms=["HS256"])

        # get token expiry time
        expiry_time = data.get("expires")

        if expiry_time is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="access token missing"
            )

        # checking if token is expired
        if expiry_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired"
            )

        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid access token"
        )
