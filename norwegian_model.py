from training_model import trainingModel

class NorwegianModel:

    def __init__(self):
        self.model = trainingModel('norwegian_train.csv', 'norwegian')

    def search(self, term):
        return self.model.search_count(term, 'no')
    
    def check_accuracy(self):
        return self.model.check_accuracy()