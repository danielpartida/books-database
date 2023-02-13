from download_book import get_book_meta_data, download_book


if __name__ == "__main__":

    for id in range(11, 3001):
        data = get_book_meta_data(book_number=id)
        title = data['metadata']['title']
        identifier = data['metadata']['identifier']
        book_number = identifier.split('/')[4]
        download_book(book_number=book_number, title=title)
