import json


class MockCovidApi:

    def call_api(self, source="./resources/fake_CA_historical_data.json"):
        file = open(source, 'r')
        r = file.read()
        file.close()
        return json.loads(r)
