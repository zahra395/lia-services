# lia-services

This is a RESTful API project. It was built using FastAPI and MongoDB with the help of Beanie ODM..

## Installation

To install the project, you need to Build the Docker image with following command .
```docker
docker-compose build
```
Then Start the Docker containers with following command.
```docker
docker-compose up
```

## Usage

To use the project, you can use these URLs.
- **Automatic Interactive Docs (Swagger UI)**: [Swagger UI](https://fastapi-template-project.com/docs)
- **Automatic Alternative Docs (ReDoc)**: [ReDoc](https://fastapi-template-project.com/redoc)


## Code Structure

The project's code is organized as follows:

- `src/models`: contains the models.py file, which defines the Product model class.
- `src/routes`: contains the products.py file, which defines the routes for the "Product" entity using FastAPI.
- `src/schemas`: contains the products.py file, which defines the Pydantic models used for data validation and serialization in the FastAPI application.
- `config.py`: contains the configuration settings for the application.
- `database.py`: contains the code for initializing the Beanie ORM and establishing a connection to the MongoDB database.
- `main.py`: It is the entry point of the FastAPI application. It contains the configuration and setup for the application.



