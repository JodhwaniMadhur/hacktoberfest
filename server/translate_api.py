
from os import environ
environ["GOOGLE_APPLICATION_CREDENTIALS"]="./translate-api-wadhwani-ai-84be3e3cd255.json"
from google.cloud import translate
   

#Always set project id in the same terminal before running this program
project_id = environ.get("PROJECT_ID", "")
parent = f"projects/{project_id}"
print("-"*100)
print(project_id)
print("-"*100)
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()

response = client.get_supported_languages(parent=parent, display_language_code="en")
languages = response.languages

print(f" Languages: {len(languages)} ".center(60, "-"))
for language in languages:
    print(f"{language.language_code}\t{language.display_name}")

