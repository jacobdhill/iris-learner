from fastapi import FastAPI
from ml.model import Model

app = FastAPI()


@app.get("/")
def index():
    model = Model()

    data = {
        'sepal_length': 5.1,
        'sepal_width': 3.5,
        'petal_length': 1.4,
        'petal_width': 0.2
    }

    return { 
        'prediction': model.predict(data)
    }