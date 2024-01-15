import unittest
import datetime
import datetimehelper

from unittest.mock import patch

"""
mock.patchを使って、関数からの返り値の値を
特定の値に変更してしまう。
そうすることで、テストの結果を一定にできる。
"""


class DateTimeHelperTest(unittest.TestCase):
    def setUp(self):
        # print("Setting up...")
        self.obj = datetimehelper.DateTimeHelper()

    def test_date(self):
        """ test for date() method """
        my_date = datetime.datetime(year=2024, month=1, day=14)
        # todayメソッドの出力をパッチによってmy_dateに置き換える
        with patch.object(self.obj, 'today', return_value=my_date):
            response = self.obj.date()
            self.assertEqual(response, '14/01/2024')

    def test_weekday(self):
        my_date = datetime.datetime(year=2024, month=1, day=14)
        # todayメソッドの出力をパッチによってmy_dateに置き換える
        with patch.object(self.obj, 'today', return_value=my_date):
            response = self.obj.weekday()
            self.assertEqual(response, 'Sunday')
        
    def test_us_india_conversion(self):
        d1 = '08/12/16'
        d2 = '07/11/2014'
        d3 = '04/29/00'
        self.assertEqual(self.obj.us_to_indian(d1), '12/08/2016')
        self.assertEqual(self.obj.us_to_indian(d2), '11/07/2014')
        self.assertEqual(self.obj.us_to_indian(d3), '29/04/2000')


if __name__ == "__main__":
    unittest.main()