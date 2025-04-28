import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

book_data = []

for page in range(1, 51):  # 50 pages total
    print(f'Scraping page {page}...')
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    if not books:
        break  # No more books found

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]
        
        book_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'Rating': rating
        })

df = pd.DataFrame(book_data)
df.to_csv('all_books.csv', index=False)

print('All pages scraped!')

