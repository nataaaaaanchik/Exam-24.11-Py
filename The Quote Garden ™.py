from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    # Ініціалізація драйвера Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())  # Ініціалізація з webdriver-manager

    # Відкриваємо сторінку
    url = "https://www.quotegarden.com/mind.html"
    driver.get(url)

    # Очікуємо завантаження контенту
    time.sleep(3)

    # Знаходимо всі цитати за класом
    quotes = driver.find_elements(By.CLASS_NAME, "text")

    # Виводимо текст кожної цитати
    if quotes:
        for i, quote in enumerate(quotes, start=1):
            print(f"{i}. {quote.text.strip()}")
    else:
        print("Цитати не знайдено. Перевірте селектор.")

except Exception as e:
    print(f"Сталася помилка: {e}")

finally:
    # Переконуємося, що драйвер закривається навіть при помилках
    if 'driver' in locals():
        driver.quit()
