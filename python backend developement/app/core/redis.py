import redis
from app.core.config import settings

# Create a connection pool for Redis
# decode_responses=True ensures that string operations return python strings instead of bytes
redis_pool = redis.ConnectionPool(
    host=settings.REDIS_HOST,
 
<truncated 238 bytes>