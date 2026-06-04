from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict

# --- User Schemas ---

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[boo
<truncated 804 bytes>