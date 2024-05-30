import boto3
import gzip
import io
import settings

"""
not working
"""

# Initialize AWS S3 session with credentials from settings
session = boto3.Session(
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY  # Corrected key name
)
s3 = session.client('s3')

def download_s3_object_to_memory(bucket, key):
    """Download an object from S3 to memory and return its contents."""
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].read()

def main():
    bucket_name = 'commoncrawl'
    initial_key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'

    # Download and decompress .gz file from S3
    compressed_data = download_s3_object_to_memory(bucket_name, initial_key)
    with gzip.GzipFile(fileobj=io.BytesIO(compressed_data), mode='rb') as gzipfile:
        first_line = gzipfile.readline().decode('utf-8').strip()

    # Download the file specified in the first line of the decompressed data
    final_key = first_line  # Assuming this is the correct key
    final_file_data = download_s3_callback_to_memory(bucket_name, final_key)

    # Read and print the contents of the final file
    with gzip.GzipFile(fileobj=io.BytesIO(final_file_data), mode='rb') as file_content:
        for line in io.TextIOWrapper(file_content, encoding='utf-8'):
            print(line.strip())

if __name__ == "__main__":
    main()
