from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user_router
from routes.events import event_router
import uvicorn
from database.connection import Settings

# fastAPI app
app = FastAPI()

# adding user router to app
app.include_router(user_router, prefix='/user')

# adding event router to app
app.include_router(event_router, prefix='/event')

# adding Cross-Origin Resource Sharing (CORS)
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()


@app.on_event('startup')
async def start_db():
    await settings.initialize_database()


# running app
if __name__ == '__main__':
    uvicorn.run(app='main:app',  port=8080, reload=True)
