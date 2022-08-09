import pandas as pd
from google.cloud import translate
from os import environ
import six

project_id = environ.get("PROJECT_ID", "")
assert project_id
parent = f"projects/{project_id}"

def translate(data,language):
    from google.cloud import translate
    from os import environ
    client = translate.TranslationServiceClient()
    target_language_code = language
    response = client.translate_text(contents=[data],target_language_code=target_language_code,parent=parent,)
    #translated_data.append(response.translations[0].translated_text)
    return response.translations[0].translated_text

