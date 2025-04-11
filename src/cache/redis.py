from redis.asyncio import Redis as AsyncRedis

redis_cache: AsyncRedis | None = None


async def get_redis() -> AsyncRedis:
    return redis_cache
