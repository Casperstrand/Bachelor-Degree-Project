import simplemma
class lemmatizer:

    def __init__(self, language):
        if language == 'english':
            self.language = 'en'
        elif language == 'norwegian':
            self.language = 'no'

    def lemmetize_words(self, word_list):
        lemmetized = [simplemma.lemmatize(w, self.language) for w in word_list]
        return lemmetized