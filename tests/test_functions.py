from unittest import TestCase
from main import rectangular

class test_rectangular_function(TestCase):

    def test_passing_zero(self):
        assert rectangular(0,5) == 'pass greater than zero'
        assert rectangular(5,0) == 'pass greater than zero'
        assert rectangular(0,0) == 'pass greater than zero'
        assert rectangular(-1,5) == 'pass greater than zero'

    def test_valid_values(self):
        assert rectangular(3, 4) == 12
