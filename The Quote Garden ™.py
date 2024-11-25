import requests
from bs4 import BeautifulSoup

url = "https://www.quotegarden.com/mind.html"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify()[:1000])

    quotes = soup.find_all('q')

    for quote in quotes:
        print(quote.get_text(strip=True))

except requests.exceptions.RequestException as e:
    print(f"Помилка при завантаженні сторінки: {e}")
except Exception as e:
    print(f"Сталася помилка: {e}")
