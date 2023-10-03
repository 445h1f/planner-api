from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
import uvicorn

#fastAPI app
app = FastAPI()

# adding user router to app
app.include_router(user_router,prefix='/user')

# adding event router to app
app.include_router(event_router, prefix='/event')


# running app
if __name__ == '__main__':
    uvicorn.run(app='main:app', port=8000, reload=True)