from s3 import AWSS3
import os

file_name="response1.txt"
file_size = os.path.getsize(file_name)

s3_obj = AWSS3(aws_access_key_id ,aws_secret_access_key,region_name)
s3_obj.push_data_to_s3_bucket(bucket_name ,open(file_name,'rb') , file_name, file_size , 'text/plain')
s3_obj.show_contents_s3_bucket(bucket_name)
file_path = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_name}"
print(file_path)
