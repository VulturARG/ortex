from typing import Optional, Dict, List

from app.domain.repository import DataCSVRepository


class ProcessCSVService:

    def __init__(self, repository: DataCSVRepository, file_name: str) -> None:
        self._repository: DataCSVRepository = repository
        self._file_name = file_name

    def _sanitize(self, data_input):
        return data_input.strip("\t")

    ###############################################################################
    # Option 1: Do it yourself
    def search_data(
            self,
            search_key: str,
            filter_key: Optional[list] = None,
            search_wanted: Optional[str] = None,
    ) -> Dict:

        csv_data = self._repository.get_data_from_csv(self._file_name)

        searched_data = {}
        for transaction in csv_data:
            if not filter_key:
                searched_data = self._add_data(transaction, searched_data, search_key, search_wanted)
                continue
            for key, value in filter_key[0].items():
                if value in transaction.get(key):
                    searched_data = self._add_data(transaction, searched_data, search_key, search_wanted)

        return searched_data

    def _add_data(
            self,
            row: Dict,
            searched_data: [dict],
            search_key: str,
            search_wanted: Optional[str] = None
    ):
        accum = float(self._sanitize(row[search_wanted])) if search_wanted else 1
        if searched_data.get(self._sanitize(row[search_key])):
            searched_data[self._sanitize(row[search_key])] += accum
        else:
            searched_data[self._sanitize(row[search_key])] = accum

        return searched_data

    ################################################################################
    # Option 2: More pythonics
    def _filter_set(self, data_csv: List, search_key: str, search_value: str):
        def iterator_func(x):
            if search_value in x.get(search_key):
                return True
            return False

        return filter(iterator_func, data_csv)

    def pythonics_search(
            self,
            search_key: Optional[list] = None,
            filters: Optional[list] = None,
    ):
        # Since I am going to filter items from the CSV loaded data list, I work with a auxiliary list
        filtered_records = self._repository.get_data_from_csv(self._file_name)

        # This filters using multiple excluding conditions (AND). For this reason I replace the list in each iteration
        for one_filter in filters:
            for key, value in one_filter.items():
                filtered_records = list(self._filter_set(filtered_records, key, value))

        filtered_items = {}

        for s_key in search_key:
            for key, value in s_key.items():
                filtered_items[value] = list(self._filter_set(filtered_records, key, value))

        return {
            "filtered_records": len(filtered_records),
            "data": filtered_items
        }

    def format_print_percent(self, filtered_data: [dict]) -> None:
        month = ["Ene", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"]

        total_filtered = filtered_data["filtered_records"]

        for key, value in filtered_data["data"].items():
            percent = round(len(value) * 100 / total_filtered, 0)
            print(f"{month[int(key[4:]) - 1]}, {int(percent):2d}%")



