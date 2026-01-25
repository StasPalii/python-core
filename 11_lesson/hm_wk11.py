from enum import Enum
from typing import Union

from fastapi import FastAPI

app = FastAPI()

class Operation(str, Enum):
    add = "add"
    sub = "sub"
    mul = "mul"
    div = "div"

@app.get("/calc/{operation}")
async def shop(operation: Operation, a:  float, b: float):
    initial_date ={"operation": operation, "a": a, "b": b}
    if operation == "add":
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result =a * b
    elif operation == "div":
        if b == 0:
            result = "nooo"
        else:
            result = a / b
    else:
        result = "tu tybik"
    result = {"result": result}
    return initial_date, result

