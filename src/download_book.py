import re
import requests


# TODO: Store fields of metadata title, language, published, author, publisher, description, subject
def get_book_meta_data(book_number: int = 2936) -> dict:
    base_url = "https://www.feedbooks.com/"
    book_url = base_url + "book/{0}".format(book_number)

    response = requests.get(url=book_url)

    text = response.text
    match = re.search('Object not found', text)

    if not match:
        data = response.json()

    else:
        data = {}

    return data


def proces_book_title(title: str) -> str:
    title = title.replace(" ", '-').lower()
    title = title.replace(":", "")
    title = title.replace("'", "")
    title = title.replace('"', "")
    title = title.replace('?', "")
    title = title.replace('!', "")
    title = title.replace('/', "-")
    title = title.replace("*", '')

    return title


def download_book(book_number: int, title: str):
    title = proces_book_title(title=title)
    base_url = "https://download.feedbooks.net/"
    download_url = base_url + "book/{0}.epub?filename={1}".format(book_number, title)

    response = requests.get(url=download_url)
    # Raise error in case of an HTTPError
    response.raise_for_status()
    content = response.content
    open('../db/{0}_{1}.epub'.format(book_number, title), 'wb').write(content)


if __name__ == "__main__":

    for id in range(3001, 3501):
        data = get_book_meta_data(book_number=id)
        if bool(data):
            title = data['metadata']['title']
            identifier = data['metadata']['identifier']
            book_number = identifier.split('/')[4]
            download_book(book_number=book_number, title=title)
