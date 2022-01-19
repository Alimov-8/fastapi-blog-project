# Blog API system with FastAPI

### Overview 
Learning FastAPI with [Offical Docs](https://fastapi.tiangolo.com/tutorial/). 
Developing Blog API system to understand development process of FastAPI projects

### Topics and Development History

- Installation and Setup FastAPI
- Terminology of FastAPI (operation, path, decorator, function)
- Path and Query Parameters and Validation
- Pydantic models, schemas
- POST operation and Request body


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