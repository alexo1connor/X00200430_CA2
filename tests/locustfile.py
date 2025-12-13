from locust import HttpUser, task, between
import random


class CalculatorUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:5000"

    @task(2)
    def add(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        self.client.post("/", data={"num1": num1, "num2": num2, "type": "add"})

    @task(2)
    def subtract(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        self.client.post("/", data={"num1": num1, "num2": num2, "type": "subtract"})

    @task(2)
    def multiply(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        self.client.post("/", data={"num1": num1, "num2": num2, "type": "multiply"})

    @task(1)
    def divide(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 99) + 1
        self.client.post("/", data={"num1": num1, "num2": num2, "type": "divide"})
