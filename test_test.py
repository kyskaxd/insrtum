import unittest

def func(x):
    denom = 3*x - x*x - 3
    # Деление на ноль не происходит по математическим причинам, исключение не выбрасывается
    return 5 / denom

def find_min_y(x_start, x_end, h):
    if h <= 0:
        raise ValueError("Шаг h должен быть положительным")
    current_x = x_start
    min_x = x_start
    min_y = func(x_start)

    while current_x <= x_end:
        current_y = func(current_x)
        if current_y < min_y:
            min_y = current_y
            min_x = current_x
        current_x += h

    return float(round(min_x, 3)), float(round(min_y, 3))

class TestFuncAndMin(unittest.TestCase):
    def setUp(self):
        print(f"\nЗапускается тест: {self._testMethodName}")

    def tearDown(self):
        print(f"Тест {self._testMethodName} выполнен успешно")

    def test_step_zero_or_negative(self):
        with self.assertRaises(ValueError):
            find_min_y(0, 10, 0)
        with self.assertRaises(ValueError):
            find_min_y(0, 10, -1)
    def test_minimum_positive_step(self):
        x, y = find_min_y(0, 4, 1)
        self.assertTrue(isinstance(x, (int, float)))
        self.assertTrue(isinstance(y, (int, float)))
        self.assertLessEqual(y, func(0))
        self.assertLessEqual(y, func(1))
        self.assertLessEqual(y, func(2))
        self.assertLessEqual(y, func(3))
        self.assertLessEqual(y, func(4))

    def test_minimum_fractional_step(self):
        x, y = find_min_y(0, 3, 0.5)
        self.assertTrue(isinstance(x, (int, float)))
        self.assertTrue(isinstance(y, (int, float)))
        points = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        for pt in points:
            self.assertLessEqual(y, func(pt))
            
    def test_negative_and_zero_x_values(self):
        xs = [-2, 0, 1]
        for val in xs:
            self.assertTrue(isinstance(func(val), float))

if __name__ == "__main__":
    unittest.main()
