from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_current_active_superuser
from app.core.database import get_db
from app.crud import user as crud_user
from app.models.user import User
from app.schemas import user as schema_user

router = APIRouter()

@router.get("/me", response_model=schema_user.UserResponse)
def get_current_user_details(
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Get details of the currently logged-in user."""
    return current_user

@router.put("/me", response_model=schema_user.UserResponse)
def update_current_user_profile(
    *,
    db: Session = Depends(get_db),
    user_in: schema_user.UserUpdate,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Update profile details of the currently logged-in user."""
    return crud_user.update_user(db, db_user=current_user, user_in=user_in)

@router.delete("/me", status_code=status.HTTP_200_OK)
def delete_current_user_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Delete the account of the currently logged-in user."""
    crud_user.delete_user(db, user_id=current_user.id)
    return {"message": "Account successfully deleted"}

# --- Superuser Admin Endpoints ---

@router.get("/", response_model=List[schema_user.UserResponse])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_superuser)
) -> Any:
    """Retrieve all users in the system (Superuser only)."""
    return db.query(User).offset(skip).limit(limit).all()

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user_by_admin(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    current_user: User = Depends(get_current_active_superuser)
) -> Any:
    """Delete any user in the system by ID (Superuser only)."""
    user = crud_user.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    crud_user.delete_user(db, user_id=user_id)
    return {"message": f"User {user_id} deleted successfully"}
