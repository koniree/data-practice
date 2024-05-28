import requests
import os
import glob
import zipfile
from io import BytesIO
import logging
import shutil


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

DOWNLOAD_DIR = 'Downloads'
CURRENT_DIR = os.getcwd()

def create_dir():
    dir_path = os.path.join(CURRENT_DIR, DOWNLOAD_DIR)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path
    
def read_url(url, dir):
    try:    
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
    except requests.RequestException as e:
        logging.error(f"Failed to download the file from {url}: {e}")
        return

    filename = url.split('/')[-1]
    with open(filename, 'wb') as file:
        zip_file = zipfile.ZipFile(BytesIO(filename.content)) 
        unzip = zip_file.extractall(dir)
    os.remove(zip_file)

def remove_zip_files():
    # remove zip files
    for f in glob.glob("*.zip"):
        os.remove(f)

def remove_csv_files():
    # remove csv files
    try:
        shutil.rmtree('./Downloads/')
    except FileNotFoundError or OSError:
        pass

def main():
    remove_csv_files()
    remove_zip_files()
    create_dir()
    for url in download_uris:
        read_url(url, './Downloads')
    print(os.listdir('./Downloads'))


if __name__ == "__main__":
    main()
