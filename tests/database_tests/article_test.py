from unittest import TestCase

from src.app import app
from src.references.article import Article

class ArticleDatabaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            from src.utils.database import reset_database
            reset_database()

    def test_article_get_all_returns_None_if_no_articles_in_database(self):
        with app.app_context():
            from src.db import article,register
            register.insert_new_user("mie","123")
            result = article.get_all(1)
        self.assertEqual(result, None)

    def test_article_insert_one_with_correct_object_is_correctly_saved_to_db(self):
        test_article = {
            "key": "key",
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "journal": "Mitä tä tarkottaa :D", 
            "volume": 3,
            "pages": "200-300",
            "category_id":1,
            "user_id":1
        }

        with app.app_context():
            from src.db import article, register, category
            register.insert_new_user('test', 'test')
            category.insert_one({"name":"test", "user_id":1})
            pre_result = article.get_all(1)
            article.insert_one(test_article)
            result = article.get_all(1)

        if result:
            self.assertEqual(pre_result, None)
            self.assertIsInstance(result[0], Article)

            self.assertEqual(result[0].key, "key")
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[0].title, "My best book")
            self.assertEqual(result[0].year, 2023)
            self.assertEqual(result[0].journal, "Mitä tä tarkottaa :D")
            self.assertEqual(result[0].volume, 3)
            self.assertEqual(result[0].pages, "200-300")
        else:
            raise AssertionError("No result from database")

    def test_article_get_all_multiple_references_returns_all(self):
        test_article = {
            "key": "key",
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "journal": "Mitä tä tarkottaa :D", 
            "volume": 3,
            "pages": "200-300",
            "category_id":1,
            "user_id":1
        }

        other_test_article = {
            "key": "otherkey",
            "author": "You",
            "title": "Your best book", 
            "year": 2020,
            "journal": "Edelleenkään en tiedä", 
            "volume": 1,
            "pages": "100-200",
            "category_id":2,
            "user_id":1
        }

        with app.app_context():
            from src.db import article, register, category
            register.insert_new_user('test', 'test')
            category.insert_one({"name":"test", "user_id":1})
            category.insert_one({"name":"test2", "user_id":1})
            article.insert_one(test_article)
            article.insert_one(other_test_article)
            result = article.get_all(1)

        if result:
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result[1].author, "You")
        else:
            raise AssertionError("No result from database")

    def test_article_different_users_get_their_own_references(self):
        test_article = {
            "key": "key",
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "journal": "Mitä tä tarkottaa :D", 
            "volume": 3,
            "pages": "200-300",
            "category_id":1,
            "user_id":1
        }

        other_test_article = {
            "key": "otherkey",
            "author": "You",
            "title": "Your best book", 
            "year": 2020,
            "journal": "Edelleenkään en tiedä", 
            "volume": 1,
            "pages": "100-200",
            "category_id":2,
            "user_id":2
        }

        with app.app_context():
            from src.db import article, register, category
            register.insert_new_user('test', 'test')
            register.insert_new_user('test2', 'test')
            category.insert_one({"name":"test", "user_id":1})
            category.insert_one({"name":"test2", "user_id":2})
            article.insert_one(test_article)
            article.insert_one(other_test_article)
            result = article.get_all(1)
            result2 = article.get_all(2)

        if result:
            self.assertEqual(len(result), 1)
            self.assertEqual(len(result2), 1)
            self.assertEqual(result[0].author, "Me")
            self.assertEqual(result2[0].author, "You")
        else:
            raise AssertionError("No result from database")

    def test_delete_one_article(self):
        test_article = {
            "key": "key",
            "author": "Me",
            "title": "My best book", 
            "year": 2023,
            "journal": "Mitä tä tarkottaa :D", 
            "volume": 3,
            "pages": "200-300",
            "category_id":1,
            "user_id":1
        }

        with app.app_context():
            from src.db import article, register, category
            register.insert_new_user('test', 'test')
            category.insert_one({"name":"test", "user_id":1})
            article.insert_one(test_article)
            result = article.get_all(1)
            article.delete_one(1,"key")
            result2 = article.get_all(1)

        if result:
            self.assertEqual(result2, None)
        else:
            raise AssertionError("No result from database")
