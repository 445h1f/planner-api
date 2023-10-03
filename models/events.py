from pydantic import BaseModel
from typing import List, Optional


# event model
class Event(BaseModel):
    id : Optional[int] = None
    title : str
    image : str
    description : str
    tags : List[str]
    location : str


    # example scheme for documentation
    class Config:
        json_schema_extra = {
            "example" : {
                "title" : "Sky Walking",
                "image" : "https://examplesite.com/image.png",
                "description" : "aka Sky Diving, we'll be meeting to walk in Sky.\
                                Make sure to join us for having adventure.",
                "tags" : ["sky", "diving", "parachuting", "adventure", "nature"],
                "location" : "Earth Surface"
            }
        }