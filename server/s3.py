
class AWSS3:
    import boto3
    from boto3.s3.transfer import TransferConfig

    def __init__(self, aws_access_key_id ,aws_secret_access_key,region_name):
        '''
        Author: Madhur Jodhwani
        Date of creation: 09/08/2022
        Date of last modification: 09/08/2022
        Function name: Init function/constructor
        Description: Initializes the class with the credentials and region name
        Input: aws_access_key_id - access key id of the user
            aws_secret_access_key - secret access key of the user
            region_name - region name of the user
        Output: None
        '''
        self.s3 = self.boto3.resource('s3',
               aws_access_key_id = aws_access_key_id,
               aws_secret_access_key= aws_secret_access_key,
               region_name = region_name)


    def push_data_to_s3_bucket(self , bucket_name ,data , file_name, file_size , content_type ):
        '''
        Author: Madhur Jodhwani
        Date of creation: 09/08/2022
        Date of last modification: 09/08/2022
        Function name: push_data_to_s3_bucket
        Description: Pushes/Uploads the data to the s3 bucket
        Input: bucket_name - name of the bucket to upload the data to
            data - data to be uploaded
            file_name - name of the file to be uploaded
            file_size - size of the file to be uploaded
            content_type - content type of the file to be uploaded
        Output: None
        '''
        config = self.TransferConfig( multipart_threshold=1024 * 25, #limit above which multiparts activate
                                max_concurrency=10, #threads
                                multipart_chunksize=1024 * 25, #size of data in each thread
                                use_threads=True) #enabling threads
   
        self.s3.Object(bucket_name, file_name).upload_fileobj(data,
                                                ExtraArgs={'ContentType': content_type},
                                                Config=config,
                                                Callback= self.ProgressPercentage(file_name,file_size),
                                                )
    
    def show_contents_s3_bucket(self,bucket_name):
        '''
        Function name: show_contents_s3_bucket
        Description: Lists the contents of the s3 bucket
        Input: bucket_name - name of the bucket to list the contents of
        Output: None
        '''
        bucket = self.s3.Bucket(bucket_name)
        print()
        print(f"Bucket : {bucket_name}")
        for obj in bucket.objects.all():
            print(f'filename : {obj.key} ')
        return bucket.objects.all()

    def check_if_file_exists(self, bucket_name, file_name):
        '''
        Author: Madhur Jodhwani
        Date of creation: 10/08/2022
        Date of last modification: 10/08/2022
        Function name: check_if_file_exists
        Description: Checks if the file exists in the s3 bucket
        Input: bucket_name - name of the bucket to check the file in
            file_name - name of the file to check in the bucket
        Output: True if the file exists, False otherwise
        '''
        bucket = self.s3.Bucket(bucket_name)
        for obj in bucket.objects.all():
            if(file_name == obj.key):return True
        return False
    
    def download_file_from_s3_bucket(self,bucket_name,file_name):
        '''
         Author: Madhur Jodhwani
        Date of creation: 10/08/2022
        Date of last modification: 10/08/2022
        Function name: ownload_file_from_s3_bucket
        Description: downloads the s3 bucket
        Input: bucket_name - name of the bucket to check the file in
            file_name - name of the file to check in the bucket
        Output: True if file is downloaded else False
        '''
        
        self.s3.Bucket(bucket_name).download_file(file_name, file_name)
        return True
        

    def delete_contents_s3_bucket(self,bucket_name,file_name ):
        '''
        Author: Madhur Jodhwani
        Date of creation: 09/08/2022
        Date of last modification: 09/08/2022
        Function name: delete_contents_s3_bucket
        Description: Deletes the contents of the s3 bucket
        Input: bucket_name - name of the bucket to delete the contents of
            file_name - name of the file to delete from the bucket
        Output: None
        '''
        self.s3.Object(bucket_name, file_name).delete()
        self.show_contents_s3_bucket(bucket_name)

    def empty_bucket(self, bucket_name):
        ''' 
        Author: Madhur Jodhwani
        Date of creation: 09/08/2022
        Date of last modification: 09/08/2022

        Function name: empty_bucket
        Description: Empties the S3 bucket
        Input: bucket_name - name of the bucket to empty
        Output: None
        '''

        self.s3.Bucket(bucket_name).objects.all().delete()


    class ProgressPercentage(object):
            import threading,sys
            def __init__(self, filename, size):
                '''
                Author: Madhur Jodhwani
                Date of creation: 09/08/2022
                Date of last modification: 09/08/2022
                Function name: __init__
                Description: Initializes the class
                Input: filename - name of the file
                    size - size of the file
                Output: None
                '''
                self._filename = filename
                self._size = float(size)
                self._seen_so_far = 0
                self._lock = self.threading.Lock()

            def __call__(self, bytes_amount):
                '''
                Author: Madhur Jodhwani
                Date of creation: 09/08/2022
                Date of last modification: 09/08/2022

                Function name: __call__
                Description: Prints the progress of the upload
                Input: bytes_amount - amount of bytes uploaded
                Output: None
                '''
                with self._lock:
                    self._seen_so_far += bytes_amount
                    percentage = (self._seen_so_far / self._size) * 100
                    self.sys.stdout.write(
                        "\r%s  %s / %s  (%.2f%%)" % (
                            self._filename, self._seen_so_far, self._size,
                            percentage))
                    self.sys.stdout.flush()
