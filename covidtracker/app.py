from flask import Flask, render_template
from flask_cors import CORS
import urllib3
import json
import datetime

class DataProcessor:

    def process(self, list_of_days):
        result = list(map(
            lambda day: {"date": self._format_date_for_display(day["date"]), "death_count": self._get_death_key(day)},
            list_of_days))
        return result

    def _format_date_for_display(self, date_as_int):
        unformated_date = str(date_as_int)
        formated_date = datetime.datetime.strptime(unformated_date, '%Y%m%d').strftime('%m %d %Y')
        return formated_date

    def _get_death_key(self, day_dictionary):
        if "death" in day_dictionary:
            return day_dictionary["death"]
        else:
            return 0


class RealCovidApi:

    def call_api(self):
        url = 'https://covidtracking.com/api/v1/states/CA/daily.json'
        response = urllib3.PoolManager().urlopen(method='GET', url=url)
        html = response.data
        return json.loads(html)


def create_app(covid_api):
    app = Flask(__name__)

    CORS(app)

    @app.route('/')
    def index():
        data = covid_api.call_api()
        processed_data = DataProcessor().process(data)
        return render_template('index.html', data=processed_data, enumerate=enumerate, str=str)

    return app


if __name__ == '__main__':
    app = create_app(RealCovidApi())
    app.run()
