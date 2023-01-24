import nltk
class stopwords:

    def __init__(self, language):
        self.language = language
        self.stopwords = nltk.corpus.stopwords.words(self.language)

    def set_stopwords(self, language):
        lang_list = []
        if language in lang_list:
            self.stopwords = nltk.corpus.stopwords.words(language)