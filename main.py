from fastapi import FastAPI
from random import choice
from random import randint
from string import printable
app = FastAPI()

@app.get("/")
def getRequest():
    return [''.join(choice(printable) for i in range(randint(3, 10))) for i in range(randint(5, 20))]

