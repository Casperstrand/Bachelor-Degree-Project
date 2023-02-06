from training_model import trainingModel

class EnglishModel:

    def __init__(self):
        self.model = trainingModel('IMDB Dataset.csv', 'english')
        