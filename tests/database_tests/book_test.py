from unittest import TestCase

from src.app import app
from src.references.book import Book

class BookDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_boo_get_all_returns_None_if_no_books_in_database(self):
        with app.app_context():
            from src.db import book
            result = book.get_all()
        self.assertEqual(result, None)

    def test_book_insert_one_with_correct_object_is_correctly_saved_to_db(self):
        test_book = {
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "publisher": "Edelleen minä", 
            "address": "Manaattikuja 69"
        }

        with app.app_context():
            from src.db import book
            pre_result = book.get_all()
            book.insert_one(test_book)
            result = book.get_all()

        if result:
            self.assertEqual(pre_result, None)
            self.assertIsInstance(result[0], Book)

            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[0].title, "My best book")
            self.assertEqual(result[0].year, 2023)
            self.assertEqual(result[0].publisher, "Edelleen minä")
            self.assertEqual(result[0].address, "Manaattikuja 69")
        else:
            raise AssertionError("No result from database")

    def test_book_get_all_multiple_references_returns_all(self):
        test_book = {
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "publisher": "Edelleen minä", 
            "address": "Manaattikuja 69"
        }

        other_test_book = {
            "author": "You",
            "title": "Your best book", 
            "year": 2020,
            "publisher": "Edelleen sinä", 
            "address": "Manaattikatu 96"
        }

        with app.app_context():
            from src.db import book
            book.insert_one(test_book)
            book.insert_one(other_test_book)
            result = book.get_all()

        if result:
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[1].author, "You")
        else:
            raise AssertionError("No result from database")