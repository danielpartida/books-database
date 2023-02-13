from os import listdir
from os.path import isfile, join

from upload_book import upload_book

if __name__ == "__main__":

    path = "../db/"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        upload_book(file_name=file)
