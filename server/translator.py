import pandas as pd
from os import environ
from cache import LRUCache

project_id = environ["PROJECT_ID"]
assert project_id
parent = f"projects/{project_id}"


def translate_csv(file_path,language):
    '''
    Author: Madhur Jodhwani
    Date of creation: 08/08/2022
    Date of last modification: 26/08/2024
    Description: Process the CSV - Translate it's contents from one language to another - Convert to DataFrame
    Input: file_path - path of the file to be translated
        language - language to be translated to
    Output: Translated Dataframe
    '''
    from google.cloud import translate
    
    cache = LRUCache(100)
    client = translate.TranslationServiceClient()
    target_language_code = language
    
    non_translated_file_data = pd.read_csv(file_path, encoding = 'utf-8') #Read the CSV file
    column_names = list(non_translated_file_data.columns)
    
    non_translated_file_data = non_translated_file_data.values.tolist() #convert pandas dataframe to list
    non_translated_file_data.insert(0,column_names)                     #adding column names to the top of the list
    
    translated_data = []
    
    for row in non_translated_file_data: #Iterate through whole CSV
        translated_row = []
        for cell_value in row:
            if cell_value != None:
                if cache.get(cell_value) == None: #Does not exist in LRU Cache
                    request = {
                        "parent": parent,
                        "contents": [cell_value],
                        "target_language_code": target_language_code,
                        "mime_type": "text/plain"
                    }
                    
                    response = client.translate_text(request) #Translate the Text using Google Cloud Translate API
                    
                    if not response.translations:
                        ...
                    
                    #Get the translated text
                    translated_text = response.translations[0].translated_text
                    cache.put(cell_value,translated_text)
                    
                    #Create the CSV with the translated text
                    translated_row.append(translated_text)
                else:
                    translated_row.append(cache.get(cell_value)) #Get the translated text from LRU Cache
            else:
                continue
        translated_data.append(translated_row)    

    df = pd.DataFrame(translated_data, columns=translated_data.pop(0))
    for i in translated_data:
        df.append(i)
    return df