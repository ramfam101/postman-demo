from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import os
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    major: Optional[str] = None


app = FastAPI(title = "Postman API Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"students": []}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.get("/")
@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/students")
def get_students(major: Optional[str] = None, min_age: Optional[int] = None, max_age: Optional[int] = None):
    """
    GET all students — supports optional filtering:
    - /students?major=Computer%20Science
    - /students?min_age=20
    - /students?major=Math&max_age=21
    """
    data = load_data()
    students = data["students"]

    # Apply filters if present
    if major:
        students = [s for s in students if s["major"].lower() == major.lower()]
    if min_age:
        students = [s for s in students if s["age"] >= min_age]
    if max_age:
        students = [s for s in students if s["age"] <= max_age]

    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    """GET one student by ID"""
    data = load_data()
    for student in data["students"]:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students")
def add_student(student: Student):
    """POST a new student (add to list)"""
    data = load_data()
    new_student = student.dict()
    new_student["id"] = len(data["students"]) + 1
    data["students"].append(new_student)
    save_data(data)
    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):
    """PUT = full update (replace student record)"""
    data = load_data()
    for i, s in enumerate(data["students"]):
        if s["id"] == student_id:
            new_data = updated.dict()
            new_data["id"] = student_id
            data["students"][i] = new_data
            save_data(data)
            return new_data
    raise HTTPException(status_code=404, detail="Student not found")


@app.patch("/students/{student_id}")
def patch_student(student_id: int, partial: Student):
    """PATCH = partial update"""
    data = load_data()
    for s in data["students"]:
        if s["id"] == student_id:
            s.update(partial)
            save_data(data)
            return s
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """DELETE a student"""
    data = load_data()
    new_students = [s for s in data["students"] if s["id"] != student_id]
    if len(new_students) == len(data["students"]):
        raise HTTPException(status_code=404, detail="Student not found")
    data["students"] = new_students
    save_data(data)
    return {"message": "Student deleted successfully"} 
