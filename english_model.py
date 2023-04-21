from training_model import trainingModel

class EnglishModel:

    def __init__(self):
        #The parameters that the specified models uses are sent back
        #to the training model which uses the specific language to
        #use the correct preprocessing tools for the dataset.
        self.model = trainingModel('Datasets/IMDB Dataset.csv', 'english')

    def search(self, term):
        return self.model.search_count(term, 'en')
    
    def check_accuracy(self):
        return self.model.check_accuracy()
    
    #This is only used for the English model but could easily be uses for 
    #for any specified language and just change the parameter from 'en'
    def translated_search(self, term, lang):
        return self.model.translated_search(term, lang, 'en')
        