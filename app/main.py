"""Main FastAPI app module"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def index():
    """Redirect to the API documentation."""
    return RedirectResponse(url="/docs")
