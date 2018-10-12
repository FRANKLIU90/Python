import employee_test as et
import unittest
from unittest.mock import patch
# import employee_test


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = et.Employee.from_str('frank-young-50000')

    def tearDown(self):
        pass

    def test_add(self):
        result = et.Employee.add(1, 5)
        self.assertEqual(result, 6)

    def test_email(self):
        # self.emp_1 = et.Employee.from_str('frank-young-50000')
        result = self.emp_1.email()
        self.assertEqual(result, 'frank.young@gmail.com')

    def test_fullname(self):
        # self.emp_1 = et.Employee.from_str('frank-young-50000')
        result = self.emp_1.fullname
        self.assertEqual('FRANK YOUNG', result)

    def test_set_raise_amt(self):
        et.Employee.set_raise_amt(1.10)
        self.assertEqual(self.emp_1.raise_amt, 1.10)

    def test_divide(self):
        with self.assertRaises(ValueError):
            et.Employee.divide(10, 0)
        self.assertEqual(et.Employee.divide(10, 3), 10 / 3)

    # def test_from_str(self):
    #     emp_2 = et.Employee.from_str('hello-there-60000')
    #     self.assertEqual(et.Employee('hello', 'there', 60000), emp_2)
    def test_look_up(self):
        # with patch('employee_test.requests.get') as mocked_get:
        #     # self.emp_1.test_look_up()
        #     mocked_get.return_value.ok = True
        #     # mocked_get.return_value.ok = True

        #     mocked_get.return_value.text = 'i tell you what'
        #     result = self.emp_1.look_up('may')
        #     self.assertEqual(result, 'i tell you what')
        #     mocked_get.assert_called_with('http://company.com/young/may')
        #     mocked_get.return_value.ok = False
        #     result = self.emp_1.look_up('june')
        #     self.assertEqual(result,'bad love')
        #     mocked_get.assert_called_with('http://company.com/young/june')
        # with patch('employee_test.requests.get')as mocked_get:
        #     mocked_get.return_value.ok = True
        #     mocked_get.return_value.text = 'i tell you what'
        #     result = self.emp_1.look_up('may')
        #     self.assertEqual(result, 'i tell you what')
        #     mocked_get.assert_called_with('http://company.com/young/may')
        #     mocked_get.return_value.ok = False
        #     result=self.emp_1.look_up('march')
        #     self.assertEqual(result, 'bad love')
        #     mocked_get.assert_called_with('http://company.com/young/march')
        with patch('employee_test.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'oh right'
            result = self.emp_1.look_up('may')
            self.assertEqual(result, 'oh right')
            mocked_get.assert_called_with('http://company.com/young/may')
            mocked_get.return_value.ok = False
            result = self.emp_1.look_up('june')
            self.assertEqual(result, 'bad love')


if __name__ == '__main__':
    unittest.main()

# unittest.main()
