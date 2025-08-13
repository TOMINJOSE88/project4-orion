from fastapi import FastAPI
from inference import router  # import your router

app = FastAPI()

# Mount the inference routes
app.include_router(router)
