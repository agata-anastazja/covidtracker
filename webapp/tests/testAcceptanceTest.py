
import urllib3
import unittest
from datetime import datetime, timedelta
from pytz import timezone
from bs4 import BeautifulSoup
from flask_testing import LiveServerTestCase
from webapp.covidtracker.app import create_app, RealCovidApi

class MyTest(LiveServerTestCase):

    def create_app(test_config=None):
        app = create_app(RealCovidApi())
        return app

    def get_today_as_string(self):
        tz = timezone('US/Eastern')
        date = datetime.now(tz).strftime('%m %d %Y')
        return date

    def get_yesterday_as_string(self):
        tz = timezone('US/Eastern')
        yesterday = datetime.now(tz) - timedelta(days=1)
        return yesterday.strftime('%m %d %Y')

    def test_getting_historical_data_for_death_count_from_california(self):
        #Given
        url = self.get_server_url()
        http = urllib3.PoolManager()
        response = http.urlopen(method='GET', url=url).data
        parsed_html = BeautifulSoup(response, "html.parser")

        expected_header = "California"
        today_string = self.get_today_as_string()
        yesterday_string = self.get_yesterday_as_string()
        #Then
        latest_date = parsed_html.find(id='date_1').get_text()
        print(latest_date)
        latest_death_count = int(parsed_html.find(id='death_count_1').get_text())

        header = parsed_html.find(id='state').get_text()
        #Then
        self.assertIn(header, expected_header)
        self.assertIn(latest_date, [today_string, yesterday_string])
        self.assertTrue(isinstance(latest_death_count, int))

if __name__ == '__main__':
    unittest.main()