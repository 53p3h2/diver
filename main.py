import json
import requests
from bs4 import BeautifulSoup

def main():
    url = f"https://divar.ir/s/tehran?q=iphone"
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('article', class_='unsafe-kt-post-card unsafe-kt-post-card--outlined unsafe-kt-post-card')
    for listing in listings:
        title = listing.find('h2', class_='unsafe-kt-post-card__title').get_text(strip=True)
        link = listing.find('a', class_='unsafe-kt-post-card__action')['href']
        print(f"Title: {title}\nLink: {link}\n")
    
if __name__ == "__main__":
    main()
