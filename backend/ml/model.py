import pickle
from sklearn.neural_network import MLPClassifier
from pydantic import BaseModel

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Prediction(BaseModel):
    prediction: str
    accuracy: str
    description: str

class Model:

    classes = ['setosa', 'versicolor', 'virginica']
    description = ['Iris setosa, the bristle-pointed iris, is a species of flowering plant in the genus Iris of the family Iridaceae, it belongs the subgenus Limniris and the series Tripetalae. It is a rhizomatous perennial from a wide range across the Arctic sea, including Alaska, Maine, Canada, Russia, northeastern Asia, China, Korea and southwards to Japan. The plant has tall branching stems, mid green leaves and violet, purple-blue, violet-blue, blue, to lavender flowers. There are also plants with pink and white flowers.', 'Iris versicolor is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names, and in Britain and Ireland as purple iris.', 'Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America. It is common along the coastal plain from Florida to Georgia in the Southeastern United States.']

    def __init__(self) -> None:
        with open('/code/backend/ml/model.pkl', 'rb') as model:
            self.classifier: MLPClassifier = pickle.load(model)

    def predict(self, iris_input: IrisInput):
        sepal_length = iris_input.sepal_length
        sepal_width = iris_input.sepal_width
        petal_length = iris_input.petal_width
        petal_width = iris_input.petal_width

        probabilities = self.classifier.predict_proba([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    
        highest_index = 0
        highest_probability = probabilities[0]
        for i in range(1, len(probabilities)):
            if probabilities[i] > highest_probability:
                highest_probability = probabilities[i]
                highest_index = i
        
        highest_probability = '{:.2f}'.format(highest_probability * 100)

        prediction = Prediction(prediction = self.classes[highest_index], accuracy = highest_probability, description = self.description[highest_index])

        return prediction
