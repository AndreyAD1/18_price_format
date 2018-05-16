import unittest
from format_price import format_price


class TestFormatPriceFunction(unittest.TestCase):

    def test_real_num_string(self):
        price = '1234.567'
        self.assertEqual(format_price(price), '1 234.57')

    def test_integer_num_string(self):
        price = '1234'
        self.assertEqual(format_price(price), '1 234')

    def test_real_num(self):
        price = 1234.567
        self.assertEqual(format_price(price), '1 234.57')

    def test_integer_num(self):
        price = 1234
        self.assertEqual(format_price(price), '1 234')

    def test_zero(self):
        self.assertEqual(format_price(0), '0')

    def test_negative_number(self):
        price = -12345.678
        self.assertEqual(format_price(price), '-12 345.68')

    def test_many_fraction_zeros(self):
        price = '12345.0000001'
        self.assertEqual(format_price(price), '12 345')

    def test_few_fraction_zeros(self):
        price = '12345.00'
        self.assertEqual(format_price(price), '12 345')

    def test_not_digit_string(self):
        price = '123abcs'
        self.assertIsNone(format_price(price))

    def test_empty_string(self):
        price = ''
        self.assertIsNone(format_price(price))

    def test_list(self):
        price = [1, 2, 3]
        self.assertIsNone(format_price(price))

    def test_complex_number(self):
        price = '1+2j'
        self.assertIsNone(format_price(price))

    def test_bool(self):
        price = False
        self.assertIsNone(format_price(price))

    def test_none(self):
        self.assertIsNone(format_price(None))


if __name__ == '__main__':
    unittest.main()
