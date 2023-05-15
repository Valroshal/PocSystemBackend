from django.test import TestCase

from django.test import TestCase
from django.db import connection


class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        self.assertTrue(connection.is_usable())
