import pickle
from sklearn.neural_network import MLPClassifier

class Model:

    classes = ['setosa', 'versicolor', 'virginica']

    def __init__(self) -> None:
        with open('/code/backend/ml/model.pkl', 'rb') as model:
            self.classifier: MLPClassifier = pickle.load(model)

    def predict(self, input_data):
        sepal_length = input_data['sepal_length']
        sepal_width = input_data['sepal_width']
        petal_length = input_data['petal_width']
        petal_width = input_data['petal_width']

        class_num = self.classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        return self.classes[class_num]
