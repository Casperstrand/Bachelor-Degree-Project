import nltk
from lemmatization import lemmatizer
from stopwords import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, svm
from sklearn.metrics import accuracy_score


class trainingModel:

    def __init__(self, dataset, language):
        self.df = pd.read_csv(dataset)
        self.language = language
        self.lemmatizer = lemmatizer(language)
        self.stopwords = stopwords(language)
        self.model = svm.SVC()
        self.text_processing()
        self.training()

    def remove_stop_words(self,text):
        text = [w for w in text if w.lower() not in self.stopwords.stopwords]
        return text

    def remove_special_characters(self,text):
        text = [w for w in text if w.isalnum()]
        return text

    def fix_text(self,row):
        return ' '.join(row)

    def text_processing(self):
        self.df = self.df.dropna()
        self.df['final_text'] = self.df['text'].apply(nltk.word_tokenize)
        self.df['final_text'] = self.df['final_text'].apply(self.remove_special_characters)
        self.df['final_text'] = self.df['final_text'].apply(self.remove_stop_words)
        self.df['final_text'] = self.df['final_text'].apply(self.lemmatizer.lemmetize_words)
        self.df['final_text'] = self.df['final_text'].apply(self.fix_text)

    def training(self):
        self.train_x, self.test_x, self.train_y, self.test_y = model_selection.train_test_split(self.df['final_text'], self.df['sentiment'], test_size=0.2)
        tfidvect = TfidfVectorizer(max_features=5000)
        tfidvect.fit(self.df['final_text'])
        self.train_x_tfidf = tfidvect.transform(self.train_x)
        self.test_x_tfidf = tfidvect.transform(self.test_x)
        self.model.fit(self.train_x_tfidf, self.train_y)

    def check_accuracy(self):
        pred = self.model.predict(self.test_x_tfidf)
        return accuracy_score(pred, self.test_y)