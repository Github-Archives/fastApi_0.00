from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    value: int

# GET
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item/")
async def root(item: str):
    return {"message": item}

@app.get("/interesting-fact/")
async def interesting_fact():
    fact = "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
    # The function then returns a dictionary with a single key-value pair,
    # where the key is "fact" and the value is the string stored in the fact variable.
    # This dictionary is automatically converted to a JSON response by FastAPI:
    return {"myKey": fact}  # Dictionary -> {"key": value} Pair
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Thus, when a client makes a GET request to /interesting-fact/,  #
# they receive a JSON response containing the interesting fact.   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# POST
@app.post("/calculate/")
async def calculate(data: CalculationRequest):
    mutated_value = data.value * 2  # Simple calculation: multiply the value by 2
    return {"mutated_value": mutated_value} ## Dictionary -> {"key": value} Pair
