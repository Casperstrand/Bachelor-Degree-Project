from fastapi import FastAPI
import pickle


app = FastAPI()

english = pickle.load(open('Trained Models/English_Model.pkl', 'rb'))
@app.get('/Search')
def search(term : str, lang : str):
    if lang == 'English':
        return english.search(term)
    else:
        return english.translated_search(term)


@app.get('/Check Accuracy')
def check_accuracy():
    return english.check_accuracy()
