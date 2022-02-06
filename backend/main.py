from fastapi import FastAPI
from ml.model import Model
from ml.model import IrisInput

app = FastAPI()


@app.post("/")
def index(iris_input: IrisInput):
    model = Model()
    return model.predict(iris_input)