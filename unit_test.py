from flask import template_rendered
from contextlib import contextmanager
from flask_testing import TestCase
import unittest
from covidtracker.app import create_app
import json


class FakeCovidApi:

    def call_api(self):
        file = open("./resources/fake_CA_historical_data.json", 'r')
        r = file.read()
        file.close()
        dict = json.loads(r)
        return dict

class AppTest(TestCase):

    def create_app(test_config=None):
        app = create_app(FakeCovidApi())
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

    def test_californian_historical_data_is_passed(self):
       with self.captured_templates(self.app) as templates:
            rv = self.app.test_client().get('/')
            assert rv.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'index.html'

            self.assertEqual(6, len(context['data']))


if __name__ == '__main__':
    unittest.main()