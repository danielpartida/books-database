import requests


# TODO: Store fields of metadata title, language, published, author, publisher, description, subject
def get_book_meta_data(book_number: int = 2936) -> dict:
    base_url = "https://www.feedbooks.com/"
    book_url = base_url + "book/{0}".format(book_number)

    response = requests.get(url=book_url)
    data = response.json()

    return data


def download_book(book_number: int = 2936, title: str = "Romeo and Juliet"):
    title = title.replace(" ", '-').lower()
    base_url = "https://download.feedbooks.net/"
    download_url = base_url + "book/{0}.epub?filename={1}".format(book_number, title)

    response = requests.get(url=download_url)
    # Raise error in case of an HTTPError
    response.raise_for_status()
    content = response.content
    open('../db/{0}_{1}.epub'.format(book_number, title), 'wb').write(content)


if __name__ == "__main__":

    data = get_book_meta_data()
    download_book()
