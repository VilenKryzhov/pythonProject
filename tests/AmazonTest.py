import unittest
import time
from amazon.AmazonPage import AmazonPage
from amazon.Book import Book



class TestAmazonSearch(unittest.TestCase):

    def setUp(self):
        self.amazon_books_page = AmazonPage()
        self.books_list = []
        self.filter_author_list = []
        self.url = "https://www.amazon.com/"

    def test_search_java_books(self):
        self.amazon_books_page.open_amazon_home_page(self.url)
        print("Sleep Selenium")
        time.sleep(5)
        self.amazon_books_page.open_amazon_home_page(self.url)
        self.amazon_books_page.click_filter_button()
        self.amazon_books_page.click_books_filter()
        self.amazon_books_page.type_value_in_input("Java")

        title_list = self.amazon_books_page.get_title_list()
        author_list = self.amazon_books_page.get_author_list()

        self.filter_author_list = self.amazon_books_page.get_filter_author_list(author_list)
        price_list = self.amazon_books_page.get_price_list()

        for i in range(len(title_list)):
            book = Book(title_list[i], self.filter_author_list[i], price_list[i])
            self.books_list.append(book)

        name_of_book = None

        for book in self.books_list:
            if book.title == "Head First Java, 2nd Edition":
                name_of_book = book.title
            print("Book Name:    " + book.title)
            print("Book author:  " + book.author)
            print("Book price:   $" + book.price)
            print(" ")

        self.assertEquals(name_of_book, "Head First Java, 2nd Edition")
