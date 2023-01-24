import nltk
import lemmatization
import stopwords
import pandas as pd


class trainingModel:

    def __init__(self, dataset, language):
        self.df = pd.read_csv(dataset)
        self.language = language
        if self.language.lower == 'en':
            self.lemmetizer = nltk.WordNetLemmatizer()
            self.stopwords = nltk.corpus.stopwords.words('english')
        else:
            self.lemmetizer = lemmatization.lemmatizer(self.language)
            self.stopwords = stopwords(self.language)

    def set_language(self, language):
        lang_list = []
        if language in lang_list:
            self.language = language
        else:
            print('This model does not support that language!')
    
    def get_language(self):
        return self.language

    language = property(fget=set_language, fset=set_language)