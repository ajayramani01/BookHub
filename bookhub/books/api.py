import requests

class GoogleBooksAPI:
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_books(self, query):
        params = {
            'q': query,
            'key': self.api_key,
            'maxResults': 10 ,
        }
        try:
            response = requests.get(self.BASE_URL, params=params)
            if response.status_code == 200:
                book_details = []
                data = response.json().get('items', [])
                for item in data:
                    volume_info = item.get('volumeInfo', {})
                    book = {
                        'title': volume_info.get('title'),
                        'author': ', '.join(volume_info.get('authors', [])),
                        'description': volume_info.get('description', 'N/A'),
                        'image': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                        'rating': volume_info.get('averageRating', 0)
                    }
                    book_details.append(book)
            return book_details
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None