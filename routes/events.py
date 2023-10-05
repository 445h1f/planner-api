from fastapi import APIRouter, HTTPException, status
from models.events import Event, EventUpdate
from typing import List
from beanie import PydanticObjectId
from models.events import Event
from database.connection import Database

event_router = APIRouter(tags=["Events"])

event_database = Database(Event)



# endpoint to returns all events
@event_router.get('/', response_model=List[Event])
async def get_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events


#get event by id
@event_router.get('/{event_id}', response_model=Event)
async def get_single_event(event_id:int) -> Event:
    event = await event_database.get(event_id)

    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no event found with supplied id."
        )

    return event


# endpoint to add event
@event_router.post('/new')
async def create_event(event_data:Event) -> dict:
    await event_database.save(event_data)

    return {
        "message" : "event added successfully."
    }


# endpoint to update event
@event_router.put('/edit/{event_id}')
async def update_event(event_id:PydanticObjectId, new_event_data:EventUpdate) -> Event:
    updated_event = event_database.update(event_id, new_event_data)

    if not update_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no event found with supplied id."
        )

    return updated_event


# endpoint to delete event by id
@event_router.delete('/delete/{event_id}')
async def delete_single_event(event_id : PydanticObjectId) -> dict:

    deleted = await event_database.delete(event_id)

    if not deleted:
        # when even not found, raising not found exception
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no event found with supplied id."
        )

    return {
        "message" : "event deleted successfully"
    }