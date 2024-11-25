import requests
from bs4 import BeautifulSoup

url = "https://www.quotegarden.com/mind.html"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select('div.quote > q')

    if quotes:
        for i, quote in enumerate(quotes, start=1):
            print(f"{i}. {quote.get_text(strip=True)}")
    else:
        print("Цитати не знайдено. Перевірте HTML-код сторінки або селектор.")

except requests.exceptions.RequestException as e:
    print(f"Помилка при завантаженні сторінки: {e}")
except Exception as e:
    print(f"Сталася помилка: {e}")
