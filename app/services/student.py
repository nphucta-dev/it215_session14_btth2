from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


def get_students(db: Session) -> list[Student]:
    return db.query(Student).all()


def get_student(db: Session, student_id: int) -> Student | None:
    return db.query(Student).filter(Student.id == student_id).first()


def create_student(db: Session, data: StudentCreate) -> Student:
    student = Student(
        full_name=data.full_name,
        email=data.email,
        major=data.major,
        gpa=data.gpa,
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def update_student(db: Session, student_id: int, data: StudentUpdate) -> Student | None:
    student = get_student(db, student_id)
    if not student:
        return None
    student.full_name = data.full_name
    student.email = data.email
    student.major = data.major
    student.gpa = data.gpa
    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: int) -> bool:
    student = get_student(db, student_id)
    if not student:
        return False
    db.delete(student)
    db.commit()
    return True
