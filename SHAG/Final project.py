import requests
from bs4 import BeautifulSoup
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS websites
                     (url text, content text)''')

    def insert_website(self, url, content):
        self.cursor.execute("INSERT INTO websites VALUES (?,?)", (url, content))
        self.conn.commit()

    def search(self, query):
        self.cursor.execute("SELECT url, content FROM websites")
        rows = self.cursor.fetchall()
        results = []
        for row in rows:
            if query in row[1]:
                results.append((row[0], row[1].count(query)))
        results.sort(key=lambda x: x[1], reverse=True)
        return results

class WebScraper:
    def __init__(self):
        pass

    def scrape(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()

class UserInterface:
    def __init__(self, db_manager, web_scraper):
        self.db_manager = db_manager
        self.web_scraper = web_scraper

    def add_website(self, url):
        content = self.web_scraper.scrape(url)
        self.db_manager.insert_website(url, content)

    def search(self, query):
        return self.db_manager.search(query)

def run():
    db_manager = DatabaseManager('websites.db')
    web_scraper = WebScraper()
    ui = UserInterface(db_manager, web_scraper)

    db_manager.create_table()

    while True:
        print("1. Add website")
        print("2. Search")
        choice = input("Enter your choice: ")
        if choice == '1':
            url = input("Enter the URL of the website: ")
            ui.add_website(url)
        elif choice == '2':
            query = input("Enter the search query: ")
            results = ui.search(query)
            for result in results:
                print(f"Website: {result[0]}, Frequency: {result[1]}")

if __name__ == "__main__":
    run()
