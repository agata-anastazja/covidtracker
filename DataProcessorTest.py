import unittest
from covidtracker import app
from MockCovidApi import MockCovidApi

class TestStringMethods(unittest.TestCase):

    def test_data_processor_extracts_the_death_count_per_day_from_list_of_days(self):
        fake_data = MockCovidApi\
            .call_api(self, source="./resources/fake_CA_historical_data_where_each_day_has_death_key.json")
        expected_dictionary = [{'date': '05 04 2020', 'death_count': 2254},
                               {'date': '05 03 2020', 'death_count': 2215},
                               {'date': '05 02 2020', 'death_count': 2171},
                               {'date': '05 01 2020', 'death_count': 2073},
                               {'date': '04 30 2020', 'death_count': 1982},
                               {'date': '03 04 2020', 'death_count': 0}]
        processor = app.DataProcessor()
        result = processor.process(fake_data)
        self.assertEqual(expected_dictionary, result)

    def test_data_processor_extracts_the_death_count_per_day_from_list_of_days_when_some_days_have_no_death(self):
        fake_data = MockCovidApi .call_api(self)
        expected_dictionary = [{'date': 20200504, 'death_count': 2254},
                               {'date': 20200503, 'death_count': 2215},
                               {'date': 20200502, 'death_count': 2171},
                               {'date': 20200501, 'death_count': 2073},
                               {'date': 20200430, 'death_count': 1982},
                               {'date': 20200304, 'death_count': 0}]
        processor = app.DataProcessor()
        result = processor.process(fake_data)
        self.assertEqual(expected_dictionary, result)

if __name__ == '__main__':
    unittest.main()