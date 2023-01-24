import simplemma
class lemmatizer:

    def __init__(self, language):
        self.language = language

    def lemmetize_words(self, word_list):
        lemmetized = [simplemma.lemmatize(w, self.language) for w in word_list]
        return lemmetized