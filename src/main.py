import uvicorn
import logging

from pydantic import ValidationError
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pymongo.errors import ServerSelectionTimeoutError, PyMongoError

from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.database import connect_database
from src.routes.products import product_route

logger = logging.getLogger()

app = FastAPI(
    version=settings.VERSION,
    title=settings.SWAGGER_TITLE,
    docs_url="/docs",
    redoc_url="/redocs",
    default_response_class=ORJSONResponse
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DatabaseConnectionError(Exception):
    pass


@app.on_event("startup")
async def startup_events():
    try:
        await connect_database()
    except ServerSelectionTimeoutError as e:
        raise DatabaseConnectionError("Failed to connect to MongoDB server") from e
    except PyMongoError as e:
        raise DatabaseConnectionError("An error occurred while connecting to MongoDB") from e


@app.exception_handler(DatabaseConnectionError)
async def database_connection_error_handler(request: Request, exc: DatabaseConnectionError):
    return JSONResponse(
        status_code=500,
        content={"error": "Database connection error", "detail": str(exc)},
    )


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


app.include_router(product_route, prefix="")
if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8001)
