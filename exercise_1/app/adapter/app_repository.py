import csv
import os
from typing import List, Dict


class AppDataCSVRepository:

    def get_data_from_csv(self, file_name: str) -> List[Dict]:
        """Get a Transactions object list from a given csv."""

        path = os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        ) + '/static/'

        transactions = []
        with open(path + file_name, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append(row)

        return transactions
