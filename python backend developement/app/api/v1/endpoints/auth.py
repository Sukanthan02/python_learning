from app.worker.tasks import send_welcome_email

router = APIRouter()

@router.post("/register", response_model=schema_user.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    *,
    db: Session = Depends(get_db),
    user_
<truncated 733 bytes>