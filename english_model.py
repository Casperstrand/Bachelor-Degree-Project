from training_model import trainingModel

class EnglishModel:

    def __init__(self):
        self.model = trainingModel('IMDB Dataset.csv', 'english')

    def search(self, term):
        self.model.search_count(term, 'en')
        