import boto3
import gzip
import io
import settings
import pandas

session = boto3.Session(
aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
aws_secret_access_key=settings.AWS_SECRET_ACCESS_API,)
s3 = session.client('s3')

def download_s3_object_to_memory(bucket, key):
    """Download an object from S3 to memory."""
    s3_response_object = s3.get_object(Bucket=bucket, Key=key)
    return s3_response_object['Body'].read()

def main():
    # Constants
    bucket_name = 'commoncrawl'
    initial_key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'

    # Download .gz file from S3 and decompress it
    compressed_data = download_s3_object_to_memory(bucket_name, initial_key)

    # Decompress data
    with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as gzipfile:
        # Read the first line to get the URI of the next file to download
        first_line = gzipfile.readline().decode('utf-8').strip()

        # Assuming the URI is a path in the S3 bucket
        final_key = first_line  # If `first_line` includes the full path on S3, adjust accordingly

        # Download the final file using the URI from the first line
        final_file_data = download_s3_object_to_memory(bucket_name, final_key)

        # Stream output to stdout
        with gzip.GzipFile(fileobj=io.BytesIO(final_file_data)) as newgzipfile:
        #with io.BytesIO(final_file_data) as final_file:
            #for line in gzip.GzipFile(newfile = io.BytesIO(final_file, encoding='utf-8')) as newest:
            newdf = pandas.DataFrame(newgzipfile)
            #for line in newgzipfile:
                    #print(line.strip())
            print(newdf.head(10))

                

if __name__ == "__main__":
    main()
