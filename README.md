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
- Generating JWT tokens
- [OAuth2 and JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- Environmental variables and secret keys
- Route behind authentication
- Allow authenticated users
- Delete and Update only own blogs (403 Forbidden)
- [FastAPI Layered Architecture](https://github.com/teamhide/fastapi-layered-architecture)
- Docs and AWS EC2 deployment images
- Deployment with FastAPI docs
- Dockerfile added [Blog Image](https://hub.docker.com/r/alimov8/blogimage)


###### Future Learnings
- AWS services and Docker
- Deployment FastAPI with Docker to AWS 
- Databases PostgreSQL, MongoDB, Redis
- Continue Learning



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


### Run FastAPI app with Docker
    # Start docker compose 
    $ docker-compose -f docker-compose.yaml up
    
    # Stop docker compose
    $ docker-compose -f docker-compose.yaml down

    -----------------------------------------

    $ docker pull alimov8/blogimage
    $ docker run -d --name blogcontainer -p 80:80 alimov8/blogimage
    # Check 127.0.0.1/docs from browser

    ------------------------------------------
    
    # Creating Dockerfile and Building Image
    $ cd app
    $ touch Dockerfile
    $ docker build -t myimage .
    $ docker images
    
    
    # Commands to run, stop and check containers 
    $ docker ps
    $ docker stop blogcontainer
    $ docker start blogcontainer



### Docs
<img src="sources/image_2022-01-24_19-00-50.png" alt="" style="float: left; margin-top: 5px; margin: 10px;" />
.


### Running FastAPI app with AWS EC2
    // Prepare the EC2 with Python and Apache server
    $ sudo apt upgrade
    $ sudo apt install apache2  # /var/www/html/index.html
    $ sudo service apache2 start
    $ sudo apt install python3-pip
    $ sudo apt install python3-venv
    
    // Cloning Project and Install Dependencies
    $ git clone [project link] && cd [project]
    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    
    // Runing app
    $ uvicorn main:app --reload  # Run from main.py folder
    
<img src="sources/photo_2022-01-20_21-55-40.jpg" alt="" style="float: left; margin-top: 5px; margin: 10px;" />
<img src="sources/photo_2022-01-20_22-11-31.jpg" alt="" style="float: left; margin-top: 5px; margin: 10px;" />