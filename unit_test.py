import urllib3
import unittest
from datetime import datetime, timedelta
from pytz import timezone
from bs4 import BeautifulSoup
from flask_testing import LiveServerTestCase
from covidtracker.__init__ import create_app

class MyTest(LiveServerTestCase):

    def create_app(test_config=None):
        app = create_app()
        return app

    def get_today_as_string(self):
        tz = timezone('US/Eastern')
        date = datetime.now(tz).strftime('%Y%m%d')
        return date

    def get_yesterday_as_string(self):
        tz = timezone('US/Eastern')
        yesterday = datetime.now(tz) - timedelta(days=1)
        return yesterday.strftime('%Y%m%d')

    def test_server_retrieves_californian_historical_data_for_death_count_including_today_or_yesterday(self):
        #Given
        # 'http://localhost:5000'
        url = self.get_server_url()

        http = urllib3.PoolManager()
        # response = http.request('GET', url)
        response = http.request(url=url, method='GET')
        html = response.data
        print(html)
        parsed_html = BeautifulSoup(html)
        expected_header = "California"
        today_string = self.get_today_as_string()
        yesterday_string = self.get_yesterday_as_string()
        #Then
        latest_date = parsed_html.find(id='row1_date')
        latest_death_count = parsed_html.find(id='row1_death_count')
        header = parsed_html.find(id='state')
        #Then
        self.assertEqual(expected_header, header)
        self.assertIn(latest_date, [today_string, yesterday_string])
        self.assertTrue(isinstance(latest_death_count, int))

if __name__ == '__main__':
    unittest.main()