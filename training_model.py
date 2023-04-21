import nltk
import pandas as pd
import translate
from lemmatization import lemmatizer
from stopwords import stopwords
from twitter_connection import twitterConnection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, svm


class trainingModel:

    def __init__(self, dataset, language):
        self.df = pd.read_csv(dataset)
        self.language = language
        self.lemmatizer = lemmatizer(language)
        self.stopwords = stopwords(language)
        self.model = svm.SVC()
        self.twitter_con = twitterConnection()
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
        self.tfidvect = TfidfVectorizer(max_features=5000)
        self.tfidvect.fit(self.df['final_text'])
        self.train_x_tfidf = self.tfidvect.transform(self.train_x)
        self.test_x_tfidf = self.tfidvect.transform(self.test_x)
        self.model.fit(self.train_x_tfidf, self.train_y)

    def check_accuracy(self):
        return self.model.score(self.test_x_tfidf, self.test_y)

    def search_count(self, term, lang):
        positive_count = 0
        negative_count = 0
        list = self.twitter_con.search(term, lang)
        for line in list:
            if self.model.predict(self.tfidvect.transform([line.text])) == 'negative':
                negative_count += 1
            elif self.model.predict(self.tfidvect.transform([line.text])) == 'positive':
                positive_count += 1

        return positive_count, negative_count
    
    def translated_search(self, term, lang, target_lang):
        positive_count = 0
        negative_count = 0
        list = self.twitter_con.search(term, lang)
        for line in list:
            if self.model.predict(self.tfidvect.transform([translate.translate_text(text=line.text,target=target_lang)])) == 'negative':
                negative_count += 1
            elif self.model.predict(self.tfidvect.transform([translate.translate_text(text=line.text,target=target_lang)])) == 'positive':
                positive_count += 1

        return positive_count, negative_count