import random
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = ""  # Replace with the website you want to scrape

#Pseudo random, not weighted by chapter
library = {
    "1-ne": 22,
    "2-ne": 33,
    "jacob": 7,
    "enos": 1,
    "jarom": 1,
    "omni": 1,
    "w-of-m": 1,
    "mosiah": 29,
    "alma": 63,
    "hel": 16,
    "3-ne": 30,
    "4-ne": 1,
    "morm": 9,
}

def main():
    random_url = generate_random_verse()
    scrape(random_url)
    parse()

def generate_random_verse():
    book_names = list(library.keys())
    chapter_counts = list(library.values())

    random_book = random.choices(book_names, weights=chapter_counts, k=1)[0]
    random_chapter = random.randint(1, library[random_book])
    url = f'https://www.churchofjesuschrist.org/study/scriptures/bofm/{random_book}/{random_chapter}?lang=eng'
    return url, random_book, random_chapter

def scrape(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        with open('output.html', 'w', encoding='utf-8') as file:
            file.write(str(soup)) 

        #print("HTML content has been saved to 'output.html'")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def parse():
    file_path = 'output.html'  

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    verses = soup.find_all(class_='verse')
    verse_count = len(verses)

    random_verse = random.randint(1, verse_count)
    result = (verses[random_verse-1].get_text(strip=False))

    return result

if __name__ == '__main__':
    main()