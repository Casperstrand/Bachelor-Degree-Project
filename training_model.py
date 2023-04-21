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
        #In the init the class does all the preprocessing automatically
        #and then trains the model
        self.df = pd.read_csv(dataset)
        self.language = language
        self.lemmatizer = lemmatizer(language)
        self.stopwords = stopwords(language)
        #It uses a SVM model, which could easily be changed if you want to try 
        #a differend model
        self.model = svm.SVC()
        #The social meida connection is then also very easily changed
        self.twitter_con = twitterConnection()
        self.text_processing()
        self.training()

    def remove_stop_words(self,text):
        text = [w for w in text if w.lower() not in self.stopwords.stopwords]
        return text

    def fix_text(self,row):
        return ' '.join(row)

    def text_processing(self):
        self.df = self.df.dropna()
        self.df['final_text'] = self.df['text'].apply(nltk.word_tokenize)
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

    #Quick funtion that returns the accuracy of the model
    def check_accuracy(self):
        return self.model.score(self.test_x_tfidf, self.test_y)

    #This is the main function that takes in a term and language as parameters
    #what these parameters is used is to limit the search from the social media connection
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
    
    #This function does the exact same thing as the one above but it translates the 
    #the posts from the social media connection
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