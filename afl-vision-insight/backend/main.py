from fastapi import FastAPI
from backend.routes import upload, inference, metrics

app = FastAPI()

app.include_router(upload.router)
app.include_router(inference.router)
app.include_router(metrics.router)