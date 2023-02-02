import requests


def get_book_meta_data(book_number: int = 2936) -> dict:
    base_url = "https://www.feedbooks.com/"
    book_url = base_url + "book/{0}".format(book_number)

    response = requests.get(url=book_url)
    data = response.json()

    return data


if __name__ == "__main__":

    data = get_book_meta_data()

    print(data)
