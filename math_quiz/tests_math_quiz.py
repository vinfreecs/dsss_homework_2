import unittest
from math_quiz import random_integer, random_operator, calculator


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        operator=random_operator()
        self.assertIn(operator,["+","-","*"])

    def test_calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 5, '-', '3 - 5', -2),
                (3, 4, '*', '3 * 4', 12),
                (6, 5, '+', '6 + 5', 11),
                (8, 6, '-', '8 - 6', 2),
                (1, 2, '*', '1 * 2', 2)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                prob,ans = calculator(num1,num2,operator)
                self.assertEqual(prob,expected_problem)
                self.assertEqual(ans,expected_answer)

if __name__ == "__main__":
    unittest.main()
