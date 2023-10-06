from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='user/signin')


# authenticating access_token
async def authenticate(token: str = Depends(oauth2_scheme)):
    # if token is not passed
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="signin to get access"
        )

    # for invalid cases, exceptions will be raised as defined in verify function
    decoded_token = verify_access_token(token)

    # return user from decoded_token payload
    return decoded_token["user"]
