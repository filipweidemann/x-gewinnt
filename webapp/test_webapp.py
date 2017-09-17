from flask import Flask, flash, redirect, url_for, session, logging, request
from flask import render_template
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from werkzeug.utils import secure_filename
from gevent.wsgi import WSGIServer
from game import game
from webservice import app
import os
import unittest

class FlaskTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the response data
        # placeholder
        self.assert_(1 == 1)

if __name__ == '__main__':
    unittest.main()
