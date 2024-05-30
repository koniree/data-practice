import boto3
import requests
import gzip
import settings
import io

"""
not working
"""

session = boto3.Session(
aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
aws_secret_access_key=settings.AWS_SECRET_ACCESS_API,)
s3 = session.client('s3')

def get_data(bucket, key, filename):
    zipped_file_from_bucket = s3.download_file(bucket,key,filename)

    #with open(zipped_file_from_bucket, encoding='utf-8') as zipped_file:
    #    with io.TextIOWrapper(zipped_file, encoding='utf-8') as decoder:
    #        content = decoder.read()
    #        print(content)
    with gzip.GzipFile(fileobj=io.BytesIO(zipped_file_from_bucket)) as gzipfile:
        # Read the first line to get the URI of the next file to download
        first_line = gzipfile.readline().decode('utf-8').strip()

    # Assuming the URI is a path in the S3 bucket
    final_key = first_line
    final_file_data = download_s3_object_to_memory(bucke, final_key)

    # Stream output to stdout
    with io.BytesIO(final_file_data) as final_file:
        for line in io.TextIOWrapper(final_file, encoding='utf-8'):
            print(line.strip())


    pass
def main():
    get_data("commoncrawl","crawl-data/CC-MAIN-2022-05/wet.paths.gz","wet.paths.gz")


if __name__ == "__main__":
    main()
