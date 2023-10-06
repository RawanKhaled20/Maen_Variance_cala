import unittest
import mean_var_std

# the test case
class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': {
                'row': [3.6666666666666665, 5.0, 3.0],
                'column': [3.3333333333333335, 4.0, 4.333333333333333],
                'element': 3.888888888888889
            },
            'variance': {
                'row': [9.555555555555557, 0.6666666666666666, 8.666666666666666],
                'column': [3.555555555555556, 10.666666666666666, 6.222222222222221],
                'element': 6.987654320987654
            },
            'standard deviation': {
                'row': [3.091206165165235, 0.816496580927726, 2.943920288775949],
                'column': [1.8856180831641267, 3.265986323710904, 2.494438257849294],
                'element': 2.6434171674156266
            },
            'max': {
                'row': [8, 6, 7],
                'column': [6, 8, 7],
                'element': 8
            },
            'min': {
                'row': [1, 4, 0],
                'column': [2, 0, 1],
                'element': 0
            },
            'sum': {
                'row': [11, 15, 9],
                'column': [10, 12, 13],
                'element': 35
            }
        }
        assert actual == expected, "Dictionaries are not equal"

    def test_calculate2(self):
        actual = mean_var_std.calculate([9, 1, 5, 3, 3, 3, 2, 9, 0])
        expected = {
            'mean': {
                'row': [4.666666666666667, 4.333333333333333, 2.6666666666666665],
                'column': [5.0, 3.0, 3.6666666666666665],
                'element': 3.888888888888889
            },
            'variance': {
                'row': [9.555555555555555, 11.555555555555557, 4.222222222222222],
                'column': [10.666666666666666, 0.0, 14.888888888888891],
                'element': 9.209876543209875
            },
            'standard deviation': {
                'row': [3.0912061651652345, 3.39934634239519, 2.0548046676563256],
                'column': [3.265986323710904, 0.0, 3.8586123009300755],
                'element': 3.0347778408328137
            },
            'max': {
                'row': [9, 9, 5],
                'column': [9, 3, 9],
                'element': 9
            },
            'min': {
                'row': [2, 1, 0],
                'column': [1, 3, 0],
                'element': 0
            },
            'sum': {
                'row': [14, 13, 8],
                'column': [15, 9, 11],
                'element': 35
            }
        }
        print(actual)
        assert actual == expected, "Dictionaries are not equal"
    
    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(ValueError, "Input list must contain exactly 9 digits.", mean_var_std.calculate, [2, 6, 2, 8, 4, 0, 1,])

if __name__ == "__main__":
    unittest.main()