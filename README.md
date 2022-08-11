<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://miro.medium.com/max/512/0*vRWyllNNRZ7TCWTO.png" alt="Project logo"></a>
</p>

<h3 align="center">CSV Translator using Google Translation API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](#todo)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About this repo<a name = "about"></a>

This repo contains server codebase built in Flask for translating a CSV file into the language code provided in the request from client.
The server has 3 routes and they are as follows:
- /translate
- /download-translated-csv
- /download-previously-translated-csv

### /translate
This API endpoint is used to upload a file using the form-data for body and adding a file in the body with tag ```file``` and the header should contain the name of the file as a key value pair ```"file_name":"XYZ.csv"```

### /download-translated-csv
This API endpoint takes a ```file_name``` and a ```language``` as headers in the requets it recieves. It then checks for the file in the S3 bucket, if the S3 bucket contains the file it downloads it on the server from S3 and then processes the whole CSV to convert to a list of strings(processing done to reduce API calls) and then to we again re-arrange the data to form a pandas dataframe and write it to CSV. This CSV then gets stored on to the S3 bucket with the name ```language_file_name```. 
Example:```hi_data.csv``` hi is langauge code for Hindi and data.csv is the name for CSV.
It is also stored on the server and is also returned as a repsonse to the client. The client basically recieves the whole file data as a response for just a ```Send``` call and gets a file to download if the request sent is ```Send and Download```.

### /download-previously-translated-csv
This API endpoint takes a ```file_name``` and a ```language``` as headers in the requets it recieves. Here we combine the language code and the file name recieved in the request headers and check if the file with the same name is present in the S3 bucket. If yes then we download it on the server and return it in the response. If not then we call the ```/download-translated-csv``` API which then checks for the original file and then translate it into the given language code and return it.

PS: All three APIs accept POST and GET requests. 
Currently the API is active on http://ec2-43-205-142-160.ap-south-1.compute.amazonaws.com:5000

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

Since this project is built on a Python framework which is flask you need to install Python on your local machine.
Python v3.9, pip and Git is required
Links for installing each of these
- www.python.org
- https://pip.pypa.io/en/stable/installation/
- https://www.atlassian.com/git/tutorials/install-git
```
Steps to setup the project install pre requisites:

git clone https://github.com/JodhwaniMadhur/Translator.git
cd Translator

pip3 install -r requirements.txt 
//This will install all the requirements like flask, google translate Library, boto3, etc.

```

### Installing

A step by step series of examples that tell you how to get a development env running.

After the requirements are installed we need to run a production server 
```
cd server
export GOOGLE_APPLICATION_CREDENTIALS="<Path to credentials JSON file>" && export PROJECT_ID="<GCP project name>" && export AWS_ACCESS_KEY_ID="<Access key ID for AWS and S3>" && export AWS_SECRET_ACCESS_KEY="<Secret Key for AWS access>";

//The AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are basically ID and Password for accessing AWS programmatically.

gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

//This will start the production server on http://0.0.0.0 with PORT=5000 with 4 working threads.
```


## 🔧 Running the tests <a name = "tests"></a>

Under progress

## 🎈 Usage <a name="usage"></a>

Converting a whole CSV from one language to another using Google Translation API 

## 🚀 Deployment on EC2 <a name = "deployment"></a>

For an EC2 instance you need a AWS account. The Linux AMI EC2 instance with 1GB of space is what we need select and then run it 

## ⛏️ Built Using <a name = "built_using"></a>

- [AWS S3 Storage](https://aws.amazon.com/s3/) - Database
- [Python (Flask)](https://flask.palletsprojects.com/en/2.2.x/) - Server Framework
- [AWS EC2](https://aws.amazon.com/ec2/) - Server Environment
- [Google CLoud Platform(Translation API)](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiiqtOXv775AhVODysKHSB-ANkYABABGgJzZg&ohost=www.google.com&cid=CAESbOD22wviP2AMThTtKv8peLO9hp-N0u-u5G9TqkWAnMmaWnPUTgDehB55WjqNAGP7QW_JLTYiQYMnILFiym2aThoqHVHk5SxGXhkWx4Jons7Ox79KO-mZp5cXEVpRF3XrDfytbHcMAnVXJx7AuA&sig=AOD64_05OG0bPYxCOgzH1_At9-DmaoczGw&q&adurl&ved=2ahUKEwjWysuXv775AhVm5nMBHWUuADcQ0Qx6BAgDEAE) - Translation API

## TODO <a name ="todo"></a>
- Delete the CSV file downloaded on server after the response is saved to save disk space(Possible solutions: Cron Job or Flask app.after_request)
- Logging for detailed analytics of server(Solution: Logging library addition)
- HTTPS implementation(Solution: SSL Certificate)

## ✍️ Authors <a name = "authors"></a>

- [Madhur Jodhwani](https://github.com/JodhwaniMadhur) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- References
  - https://codelabs.developers.google.com/codelabs/cloud-translation-python3#7
  - https://betterprogramming.pub/aws-s3-buckets-with-python-tutorial-uploading-deleting-and-managing-the-files-in-buckets-dd90d4fd45fe
  - https://flask.palletsprojects.com/en/2.2.x/
  - https://flask.palletsprojects.com/en/2.2.x/deploying/
  - https://stackoverflow.com
