import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find the book containers
books = soup.find_all('article', class_='product_pod')

# Step 3: Extract info
book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    rating = book.p['class'][1]  # e.g., "Three" for 3 stars

    book_data.append({
        'Title': title,
        'Price': price,
        'Availability': availability,
        'Rating': rating
    })

# Step 4: Save to CSV
df = pd.DataFrame(book_data)
df.to_csv('books.csv', index=False)

print('Scraping done! Saved to books.csv')
