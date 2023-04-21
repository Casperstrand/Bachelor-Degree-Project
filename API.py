from fastapi import FastAPI
import pickle



app = FastAPI()

english = pickle.load(open('English_Model.pkl', 'rb'))
norwegian = pickle.load(open('Norwegian_Model.pkl', 'rb'))
@app.get('/Search')
def search(term : str, lang : str):
    if lang.lower() == 'en':
        return english.search(term)
    elif lang.lower() == 'no':
        return norwegian.search(term)
    else:
        return english.translated_search(term, lang)

@app.get('/Check Accuracy')
def check_accuracy(lang : str):
    if lang.lower() == 'no':
        return norwegian.check_accuracy()
    elif lang.lower() == 'en':
        return english.check_accuracy()
    else:
        print('To trained model for that language')
