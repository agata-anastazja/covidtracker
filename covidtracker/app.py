from flask import Flask, render_template
from flask_cors import CORS
import urllib3
import json

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

        return render_template('index.html', data=data)

    return app

if __name__ == '__main__':
    app = create_app(RealCovidApi())
    app.run()