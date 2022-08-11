import requests,os

class Client:
    server_path= ""
    def __init__(self,url):
        self.server_path = url

    def file_writer(self, file_pointer):
        for chunk in requests.Response.iter_content(chunk_size=8192):
            file_pointer.write(chunk)
        file_pointer.close()

    def upload(self, file_path,file_name):
        files = {'file': open(file_path,'rb')}
        headers = {'file_name': f"{file_name}"}
        requests.Response = requests.post(self.server_path+"/translate",files=files, headers=headers)
        print("Response = ", requests.Response.status_code)


    def translate_and_download_uploaded_csv(self, file_name, language):
        headers = {'file_name': file_name,'language':language}
        requests.Response = requests.post(self.server_path+"/download-translated-csv", headers=headers)
        print(requests.Response.status_code)
        self.file_writer(open(f"./{language}_{file_name}", "wb"))


    def download_translated_csv(self,file_name,language):
        values = {'file_name': file_name,'language':language}
        requests.Response = requests.post( self.url+"/download-previously-translated-csv", headers=values)
        print(requests.Response.status_code)
        self.file_writer(open(f"./{language}_{file_name}", "wb"))


def previously_downloaded_csv(client_obj):
    choice_2 = input("Do you want to download a previously translated file? (y/n)")
    if choice_2 == 'y':
        file_name = input("Enter file name for translation:")
        language = input("Enter language for translation:")
        client_obj.download_translated_csv(file_name, language)
    if choice_2 == 'n':
        print("Thank you for using CSV Translator")
        print('---'*50)
        exit(0)

def main():
    #Signup and login functionality
    print("Welcome to CSV Translation Tool(Client)")
    print("---"*50)
    url = input("Enter the url of the server in the format http://localhost:5000: ")
    client_obj  = Client(url)
    file_path   = input("Enter CSV file path for upload:")
    if(os.path.exists(file_path) == False):
        print("File not found")
        exit(0)
    header_file_name = input("Enter file name/path for headers:")
    client_obj.upload(file_path,header_file_name)
    print("Do you want to translate a previously upload file? (y/n)")
    choice_1 = input()

    if choice_1 == 'y':
        file_name = input("Enter file name for translation:")
        if(os.path.exists(file_path) == False):
            print("File not found")
            exit(0)
        language = input("Enter language code for translation(refer labnol.org/code/19899-google-translate-languages for language codes):")
        client_obj.translate_and_download_uploaded_csv(file_name,language)
        previously_downloaded_csv(client_obj)

    if choice_1 == 'n':
        previously_downloaded_csv(client_obj)

if __name__ =="__main__":
    main()