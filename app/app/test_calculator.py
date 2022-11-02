from django.test import SimpleTestCase
import calculator


class CalcTests(SimpleTestCase):

    def test_add(self):
        """Test addition feature"""
        res = calculator.add(1, 3)
        self.assertEqual(res, 4)
