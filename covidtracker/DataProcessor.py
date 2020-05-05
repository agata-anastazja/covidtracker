

class DataProcessor:

    def process(self, list_of_days):
        result = list(map(lambda day: {"date": self._format_date_for_display(day["date"]), "death_count": self._get_death_key(day)},
                   list_of_days))
        return result

    def _format_date_for_display(self, date_string):
        return date_string

    def _get_death_key(self, day_dictionary):
        if "death" in day_dictionary:
            return day_dictionary["death"]
        else:
            return 0
