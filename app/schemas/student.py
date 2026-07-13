from pydantic import BaseModel, ConfigDict, EmailStr


class StudentCreate(BaseModel):
    full_name: str
    email: EmailStr
    major: str
    gpa: float


class StudentUpdate(BaseModel):
    full_name: str
    email: EmailStr
    major: str
    gpa: float


class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: str
    major: str
    gpa: float
