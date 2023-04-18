from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('C:/Users/Casper/Desktop/Bachelor Project/Bachelor-Degree-Project/Credentials/cryptic-tower-376516-85193ea924d9.json')
translate_client = translate.Client(credentials=credentials)
def translate_text(target, text):
    result = translate_client.translate(text, target_language=target)

    return result["translatedText"]



