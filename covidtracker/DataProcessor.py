

class DataProcessor:

    def process(self, list_of_days):
        result = list(map(lambda day: {"date": self._format_date_for_display(day["date"]), "death_count": day["death"]},
                   list_of_days))
        return result

    def _format_date_for_display(self, date_string):
        return date_string
