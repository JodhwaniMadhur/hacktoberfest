from flask import Flask, jsonify, request
from translator import translate
from s3_storage import AWSS3
import os

aws_access_key_id = ""
aws_secret_access_key = ""
region_name = ""
bucket_name = ""
app = Flask(__name__)

@app.route('/translate',methods=["POST","GET"])
def api_translate():
    file_name = request.headers.get('file_name')
    #language_code = request.headers.get("language")
    data = request.files['file'].read()
    if not data:
        return jsonify({ "status" : "error" }),406
    else:
        data = data.save(f'{file_name}')
        storeInS3(file_name)
        return jsonify({ "status" : "success" }),200

@app.route('/download-translated-csv',methods=["POST","GET"])
def api_call_translate():
    data = request.headers.get("file_name")
    language = request.headers.get("language")
    if not data:
        return jsonify({ "status" : "error" })
    else:
        #read the s3 bucket file here and translate it
        translated_data = translate(data,language)
        return jsonify({"translated_data": f"{translated_data}"}),200


def storeInS3(file_name):
    aws_s3 = AWSS3()
    file_size = os.path.getsize(file_name)
    aws_s3.push_data_to_s3_bucket(bucket_name,open(file_name,'rb'),file_name,file_size,"text/csv")
    os.remove(file_name)
    return True