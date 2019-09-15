import os
import unittest

import models
from app import app, db

TEST_DB = 'test.db'


class HttpImageProxyTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a count equals to 0 database before each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, TEST_DB)}'
        self.app = app.test_client()
        db.create_all()
        new_entry = models.APICounter('proxy', 0)
        db.session.add(new_entry)

        # commit the changes
        db.session.commit()

    def tearDown(self):
        """Destroy database after each test"""
        db.drop_all()

    def test_page_not_found(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 404)
        self.assertIn('404 Not Found', str(rv.data))

    def test_count_equals_to_zero(self):
        rv = self.app.get('/admin')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json.get('query_count'), [0])

    def test_api_count(self):
        rv = self.app.get('/proxy')
        self.assertEqual(rv.status_code, 200)
        self.assertIn('Empty', str(rv.data))

        rv = self.app.get('/admin')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json.get('query_count'), [1])

    def test_invalid_url(self):
        rv = self.app.get('/proxy?url=123')
        self.assertEqual(rv.status_code, 200)
        self.assertIn('Empty', str(rv.data))


if __name__ == '__main__':
    unittest.main()
