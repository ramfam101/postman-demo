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
git clone https://github.com/<your-username>/fastapi-postman-demo.git
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

### View docs
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

### Postman demo

You can import the included Postman collection:

File: postman-json-collection.json

Steps:

1. Open Postman

2. Click Import → Upload Files

3. Choose the JSON collection file

4. Verify the base_url variable is to http://127.0.0.1:8000

5. Try sending each request (GET, POST, PUT, PATCH, DELETE)

