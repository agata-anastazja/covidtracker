import unittest
from flask import template_rendered
from contextlib import contextmanager
from flask_testing import TestCase
from covidtracker.__init__ import create_app

class AppTest(TestCase):

    def create_app(test_config=None):
        app = create_app()
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

    def test_server_retrieves_californian_historical_data_for_death_count_including_today_or_yesterday(self):
       with self.captured_templates(self.app) as templates:
            rv = self.app.test_client().get('/')
            assert rv.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'index.html'

if __name__ == '__main__':
    unittest.main()