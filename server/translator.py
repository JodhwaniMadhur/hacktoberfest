import pandas as pd
from os import environ


project_id = environ["PROJECT_ID"]
assert project_id
parent = f"projects/{project_id}"


def translate_csv(file_path,language):
    '''
    Author: Madhur Jodhwani
    Date of creation: 08/08/2022
    Date of last modification: 10/08/2022
    Description: Process the CSV - Translate it's contents from one language to another - Convert to DataFrame
    Input: file_path - path of the file to be translated
        language - language to be translated to
    Output: Translated Dataframe
    '''
    from google.cloud import translate
    client = translate.TranslationServiceClient()
    target_language_code = language
    non_translated_file_data = pd.read_csv(file_path)
    column_names = list(non_translated_file_data.columns)
    non_translated_file_data = non_translated_file_data.values.tolist() #convert pandas dataframe to list
    non_translated_file_data.insert(0,column_names)                     #adding column names to the top of the list
    
    delimited_file_data, translated_data = [],[]
    for row in non_translated_file_data:
        row = "-".join(list(map(str,row)))
        delimited_file_data.append(row)
    for i in delimited_file_data:
        response = client.translate_text(contents=[i],target_language_code=target_language_code,parent=parent,)
        translated_data.append(response.translations[0].translated_text.split("-"))
    df = pd.DataFrame(translated_data, columns=translated_data.pop(0))
    for i in translated_data:
        df.append(i)
    return df

