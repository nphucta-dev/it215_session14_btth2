from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    major: Mapped[str] = mapped_column(String(255), nullable=False)
    gpa: Mapped[float] = mapped_column(Float, nullable=False)
