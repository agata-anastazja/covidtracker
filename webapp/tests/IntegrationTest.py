from flask import template_rendered
from contextlib import contextmanager
from flask_testing import TestCase
import unittest
from webapp.covidtracker import create_app
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
            expected_dictionary = [{'date': 20200504, 'death_count': 2254},
                                   {'date': 20200503, 'death_count': 2215},
                                   {'date': 20200502, 'death_count': 2171},
                                   {'date': 20200501, 'death_count': 2073},
                                   {'date': 20200430, 'death_count': 1982},
                                   {'date': 20200304, 'death_count': 0}]
            self.assertEqual(context['data'], expected_dictionary)


if __name__ == '__main__':
    unittest.main()