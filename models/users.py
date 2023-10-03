from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .events import Event


# # user sign up mode
# class UserSignUp(BaseModel):
#     email : EmailStr
#     password : str


#     class Config:
#         json_schema_extra = {
#             "examples" : {
#                 "email" : "test@email.com",
#                 "password" : "YouOweMe!!!"
#             }
#         }



# user model
class User(BaseModel):
    email : EmailStr
    password : str
    # events : Optional[List[Event]]


    # sample schema for doc
    class Config:
        json_schema_extra = {
            "example" : {
                "email" : "user@email.com",
                "password" : "@Hello,There!",
            }
        }


# user sign in model
class UserSignIn(BaseModel):
    email : EmailStr
    password : str


    class Config:
        json_schema_extra = {
            "example" : {
                "email" : "user@email.com",
                "password" : "@Hello,There!"
            }
        }