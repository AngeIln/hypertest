from pydantic import BaseModel, EmailStr


class MessageResponse(BaseModel):
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class CodeRequest(BaseModel):
    language: str
    prompt: str
    code: str | None = None


class ExecutionRequest(BaseModel):
    language: str
    code: str
    stdin: str | None = ""


class TestRunRequest(BaseModel):
    language: str
    code: str
    tests: str
