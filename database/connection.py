from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, List, Any
from pydantic import BaseSettings, BaseModel
from models.users import User
from models.events import Event


class Settings(BaseSettings):
    DATABASE_URL : Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)

        await init_beanie(
            database=client.get_database('planner'),
            document_models=[User, Event]
        )

    class Config:
        env_file = '.env'


class Database:

    def __init__(self, model) -> None:
        self.model = model


    # CREATE
    # method to create document
    async def save(self, document) -> None:
        await document.create()
        return

    # READ
    # method to get single document by id
    async def get(self, id:PydanticObjectId) -> Any:
        doc = await self.model.get(id)

        if doc:
            return doc
        else:
            return False

    # method to get all documents
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs


    # UPDATE
    # method to update document
    async def update(self, id:PydanticObjectId, body:BaseModel) -> Any:
        # creating update query
        doc_body = {k:v for k, v in body.dict().items() if v is not None}

        update_query = {
            "$set" : {
                field:value for field, value in doc_body.items()
            }
        }

        # getting doc by id
        doc = await self.get(id)

        # if doc not found return false
        if not doc:
            return False

        # else update doc
        await doc.update(update_query)
        return doc


    # DELETE
    # delete doc by id
    async def delete(self, id:PydanticObjectId) -> bool:
        doc = await self.get(id)

        if not doc:
            return False

        await doc.delete()
        return True