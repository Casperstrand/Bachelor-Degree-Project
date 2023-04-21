from google.cloud import translate_v2 as translate
from google.oauth2 import service_account



credentials = service_account.Credentials.from_service_account_file('Credentials/cryptic-tower-376516-85193ea924d9.json')
translate_client = translate.Client(credentials=credentials)
def translate_text(text, target):
    result = translate_client.translate(text, target_language=target)
    return result["translatedText"]