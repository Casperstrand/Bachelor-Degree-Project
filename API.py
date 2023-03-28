from fastapi import FastAPI
from english_model import EnglishModel
app = FastAPI()

@app.get('/')
def search():
    return 'Hello'
