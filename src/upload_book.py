import os
import boto3
from dotenv import load_dotenv


if __name__ == "__main__":

    # Upload files to AWS using boto3
    # https://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto
    path = "../db/"
    file_name = "11_the-precipice.epub"
    bucket_name = "s3-book-database"

    # Read environment variables
    load_dotenv()
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    # Create AWS access key and secret access key
    # https://stackoverflow.com/questions/33297172/boto3-error-botocore-exceptions-nocredentialserror-unable-to-locate-credential
    # https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html
    s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.Bucket(bucket_name).upload_file(path+file_name, "db/{0}".format(file_name))
