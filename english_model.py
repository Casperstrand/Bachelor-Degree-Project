from training_model import trainingModel

class EnglishModel:

    def __init__(self):
        self.model = trainingModel('IMDB Dataset.csv', 'english')

    def search(self, term):
        return self.model.search_count(term, 'en')
    
    def check_accuracy(self):
        return self.model.check_accuracy()
    
    def translated_search(self, term):
        return self.model.translated_search(term, 'en', 'en')
        