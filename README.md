# Blog API system with FastAPI

### Overview 
Learning FastAPI with [Offical Docs](https://fastapi.tiangolo.com/tutorial/). 
Developing Blog API system to understand development process of FastAPI projects

### Topics and Development Process
- Installation and Setup FastAPI
- Terminology of FastAPI (operation, path, decorator, function)
- Path and Query Parameters and Validation
- Pydantic models, schemas
- POST operation and Request body

---

- FastAPI Database connection
- [SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [SQL Alchemy](https://www.sqlalchemy.org/)
- Creating Database models and schemas
- Storing data to the Database
- Getting data from the Database
- Deleting data from the Database
- CRUD functionalities 

---

- Response status codes
- HttpExceptions
- Response models and pydantic schemas
- Pydantic [offical docs](https://pydantic-docs.helpmanual.io/)

---

- Creating a User model
- Hashing the password 
- Metadata and Docs URLs
- [Database Relationships](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-relationships)
- Foreign Keys and Relationship between User and Blog

---

- [Bigger Application Structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- Code restructuring
- API Routers
- Blog and User views

---
- Authentication routers
- Login and Password verify
###### Learnings
- Generating JWT tokens
- [OAuth2 and JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- Route behind authentication
- FastAPI code restructure (bigger application structure)
- AWS EC2 deployment images
- AWS services, Docker
- Deployment FastAPI with Docker to AWS 
- Databases PostgreSQL, MongoDB, Redis
---
- Continue Learning ...

### Dependencies
- python (3.6 or greater)


### Setup
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    
    # Windows OS:
    > python -m venv venv
    > venv\Scripts\activate.bat
    > pip install -r requirements.txt

### Run 
    $ uvicorn main:app --reload



### Docs

<img src="sources/photo_2022-01-20_13-09-32.jpg" alt="" style="float: left; margin-top: 5px; margin: 10px;" />