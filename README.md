# FastAPI Postman Demo

This is a simple FastAPI application designed to demonstrate REST API concepts using Postman.  
It includes basic CRUD operations, query parameters, and data persistence via a local JSON file.

---

## Features

- **GET**: Retrieve all students or filter using query parameters  
- **GET (by ID)**: Retrieve a single student by ID  
- **POST**: Add a new student  
- **PUT**: Replace an existing student record  
- **PATCH**: Partially update a student record  
- **DELETE**: Remove a student  
- **Health check** endpoint (`/health`)  

---

## Installation

### Clone or download the repository
```bash
git clone https://github.com/ramfam101/postman-demo.git
cd fastapi-postman-demo 
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
uvicorn main:app --reload
```
or
```bash
python -m uvicorn main:app --reload
```

### View docs
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

### Postman demo

Steps:

1. Open Postman

2. In collections, click Import → Upload Files

3. Choose the JSON collection file: **postman-json-collection.json**

5. The base_url variable should be set to http://127.0.0.1:8000, verify this

6. Demonstrate sending each request (GET, POST, PUT, PATCH, DELETE)

