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
