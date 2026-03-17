from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.db import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.entities import User, SessionSnippet
from app.schemas.common import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    CodeRequest,
    ExecutionRequest,
    TestRunRequest,
)
from app.services.ai_service import generate_code, explain_code
from app.services.execution_service import run_code

router = APIRouter(prefix="/api/v1")


@router.post("/auth/register", response_model=TokenResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.scalar(select(User).where(User.email == payload.email))
    if existing:
        raise HTTPException(status_code=409, detail="User already exists")
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(user)
    db.commit()
    token = create_access_token(payload.email)
    return TokenResponse(access_token=token)


@router.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == payload.email))
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenResponse(access_token=create_access_token(payload.email))


@router.post("/ai/generate")
def ai_generate(payload: CodeRequest):
    try:
        code = generate_code(payload.language, payload.prompt)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {"code": code}


@router.post("/ai/explain")
def ai_explain(payload: CodeRequest):
    return {"explanation": explain_code(payload.language, payload.code or "")}


@router.post("/execution/run")
def execution_run(payload: ExecutionRequest):
    return run_code(payload.language, payload.code, payload.stdin or "")


@router.get("/sessions")
def list_sessions(db: Session = Depends(get_db)):
    rows = db.scalars(select(SessionSnippet).limit(50)).all()
    return [{"id": row.id, "language": row.language, "prompt": row.prompt} for row in rows]


@router.post("/tests/run")
def run_tests(payload: TestRunRequest):
    return {
        "status": "queued",
        "message": f"Test execution scheduled for {payload.language} via worker queue",
    }
