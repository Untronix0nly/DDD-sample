from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio import Redis

from src.cache import redis
from src.config.settings import settings
from src.database.models import start_mapping
from src.dependencies.main import register_dependencies


@asynccontextmanager
async def lifespan(_: FastAPI):
    start_mapping()
    redis.redis_cache = Redis(
        host=settings.cache_host, port=settings.cache_port, decode_responses=True
    )
    yield
    await redis.redis_cache.close()


app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    version=settings.version,
    docs_url="/api/todos/openapi",
    openapi_url="/api/todos/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


register_dependencies(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=LOGGING)
