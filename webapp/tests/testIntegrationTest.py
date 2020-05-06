from flask import template_rendered
from contextlib import contextmanager
from flask_testing import TestCase
import unittest
from webapp.covidtracker.app import create_app
from webapp.tests.MockCovidApi import MockCovidApi


class AppTest(TestCase):

    def create_app(test_config=None):
        app = create_app(MockCovidApi())
        return app

    @contextmanager
    def captured_templates(self, app):
        recorded = []

        def record(sender, template, context, **extra):
            recorded.append((template, context))

        template_rendered.connect(record, app)
        try:
            yield recorded
        finally:
            template_rendered.disconnect(record, app)

    def test_californian_historical_data_is_processed_and_passed(self):
        with self.captured_templates(self.app) as templates:
            rv = self.app.test_client().get('/')
            assert rv.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'index.html'
            expected_dictionary = [{'date': '05 04 2020', 'death_count': 2254},
                                   {'date': '05 03 2020', 'death_count': 2215},
                                   {'date': '05 02 2020', 'death_count': 2171},
                                   {'date': '05 01 2020', 'death_count': 2073},
                                   {'date': '04 30 2020', 'death_count': 1982},
                                   {'date': '03 04 2020', 'death_count': 0}]
            self.assertEqual(context['data'], expected_dictionary)


if __name__ == '__main__':
    unittest.main()