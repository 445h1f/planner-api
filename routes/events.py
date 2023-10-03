from fastapi import APIRouter, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Events"])

# storing events in list
events = []


# endpoint to returns all events
@event_router.get('/', response_model=List[Event])
async def get_all_events() -> List[Event]:
    return events


#get event by id
@event_router.get('/{event_id}', response_model=Event)
async def get_single_event(event_id:int) -> Event:
    # checking if event exists with given id
    for event in events:
        if event.id == event_id:
            return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="no event found with supplied id."
    )


# endpoint to add event
@event_router.post('/new')
async def create_event(event_data:Event) -> dict:
    # adding id for new event
    new_event_id = len(events) + 1
    event_data.id = new_event_id

    # adding event
    events.append(event_data)

    return {
        "message" : "event added successfully."
    }


# endpoint to delete event by id
@event_router.delete('/delete/{event_id}')
async def delete_single_event(event_id : int) -> dict:
    # searching for event with id
    for event in events:
        if event.id == event_id:
            #event found, so deleting it
            events.remove(event)

            return {
                "message" : "event deleted successfully."
            }

    # when even not found, raising not found exception
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="no event found with supplied id."
    )


# endpoint to delete all events
@event_router.delete('/delete')
async def delete_all_events() -> dict:
    events.clear()

    return {
        "message" : "all events deleted successfully."
    }