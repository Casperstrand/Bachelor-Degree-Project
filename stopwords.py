import nltk
class stopwords:

    def __init__(self, language):
        self.language = language
        self.stopwords = nltk.corpus.stopwords.words(self.language)