from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles #added this to support the fasrtapi(anish)
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend") # added this to support fast api(anish)
app.include_router(items_router, prefix="/items")
app.include_router(analytics_router, prefix="/analytics")# added prefixes (anish)
app.include_router(quiz_router, prefix="/quiz") #added prefixes(anish)


# why the hell did I write this function?
@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}