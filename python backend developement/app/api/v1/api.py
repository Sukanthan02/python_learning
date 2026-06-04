from fastapi import APIRouter
from app.api.v1.endpoints import auth, user

# Create API version router
api_router = APIRouter()

# Include sub-routers with prefixes and documentation tags
api_router.include_router(auth.router, prefix="/auth", tag
<truncated 103 bytes>