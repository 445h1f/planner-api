from pydantic import BaseModel, EmailStr
from beanie import Document, Link
from typing import List, Optional


# user model
class User(Document):
    email : EmailStr
    password : str
    # events : Optional[List[Link[Event]]]


    class Settings:
        name = 'users'

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