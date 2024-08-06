from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic models are used to define the request and response models for the API.
# The CalculationRequest class inherits from BaseModel, which is a core component of Pydantic.
# This inheritance allows the class to leverage Pydantic's data validation and serialization features.
# The class contains a single attribute, value, which is of type int:
# By defining this model, the FastAPI application ensures that any data sent to the POST endpoint /calculate/
# must include an integer field named value. If the incoming data does not match this structure, FastAPI will
# automatically return a validation error response. This helps maintain the integrity and reliability of the
# data processed by the application.
class CalculationRequest(BaseModel):
    value: int


# GET
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/item/")
async def root(item: str):
    return {"message": item}

# When a client makes a GET request to /interesting-fact/,
# they receive a JSON response containing the interesting fact.
@app.get("/interesting-fact/")
async def interesting_fact():
    fact = "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
    # The function then returns a dictionary with a single key-value pair,
    # where the key is "fact" and the value is the string stored in the fact variable.
    # This dictionary is automatically converted to a JSON response by FastAPI:
    return {"myKey": fact}  # Dictionary -> {"key": value} Pair


# POST
@app.post("/calculate/")
async def calculate(data: CalculationRequest):
    mutated_value = data.value * 2  # Simple calculation: multiply the value by 2
    return {"mutated_value": mutated_value}  # Dictionary -> {"key": value} Pair
