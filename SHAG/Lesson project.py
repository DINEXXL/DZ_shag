import sqlite3
import requests
from bs4 import BeautifulSoup


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS websites
                     (id INTEGER PRIMARY KEY, url TEXT, word_count INTEGER)''')

    def insert_website(self, url, word_count):
        self.cursor.execute("INSERT INTO websites (url, word_count) VALUES (?, ?)", (url, word_count))
        self.conn.commit()

    def get_websites(self):
        self.cursor.execute("SELECT * FROM websites ORDER BY word_count DESC")
        return self.cursor.fetchall()


class WebsiteParser:
    def __init__(self, word):
        self.word = word

    def count_word_in_website(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        words = soup.get_text().split()
        return words.count(self.word)


class UserInterface:
    def __init__(self, db_manager, website_parser):
        self.db_manager = db_manager
        self.website_parser = website_parser

    def run(self):
        while True:
            print("Enter URL (or 'next' to search word, 'results' to view results):")
            url = input()
            if url.lower() == 'next':
                print("Enter word to search:")
                word = input()
                self.website_parser.word = word
            elif url.lower() == 'results':
                websites = self.db_manager.get_websites()
                for website in websites:
                    print(f"ID: {website[0]}, URL: {website[1]}, Word count: {website[2]}")
            else:
                word_count = self.website_parser.count_word_in_website(url)
                self.db_manager.insert_website(url, word_count)


if __name__ == "__main__":
    db_manager = DatabaseManager('websites.db')
    website_parser = WebsiteParser('')
    user_interface = UserInterface(db_manager, website_parser)
    user_interface.run()
