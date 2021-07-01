import ast
import csv
import os
import unittest
from unittest.mock import Mock

from app.domain.repository import DataCSVRepository
from app.domain.service import ProcessCSVService


class TestService(unittest.TestCase):
    def setUp(self):

        self._path = os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        ) + '/static/'
        self._transactions = []
        with open(self._path + '2017test.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._transactions.append(row)

        with open(self._path + "expected_q_3.txt", "r") as file:
            self._expected = ast.literal_eval(file.read())

    def test_Exchange_has_had_most_transactions(self):

        repository = Mock(sepc=DataCSVRepository)

        service = ProcessCSVService(
            repository=repository,
            file_name=self._path + '2017test.csv'
        )

        # values returned by the repository
        repository.get_data_from_csv.return_value = self._transactions

        expected = {'FIRST NORTH SWEDEN': 3, 'NASDAQ STOCKHOLM AB': 2, 'Istanbul (Turkey)': 4,
                    'off exchange': 11, 'OMX-Copenhagen (Denmark)': 4, 'Oslobors (Norway)': 5,
                    'ATHEX (Greece)': 1, 'AKTIETORGET': 1}
        actual = service.search_data("exchange")

        self.assertEqual(expected, actual)

    def test_August2017_which_companyName_had_the_highest_combined_valueEUR(self):

        repository = Mock(sepc=DataCSVRepository)

        service = ProcessCSVService(
            repository=repository,
            file_name=self._path + '2017test.csv'
        )

        # values returned by the repository
        repository.get_data_from_csv.return_value = self._transactions

        expected = {
            'GEN YATIRIM HOLDING AS': 4749.8203,
            'BLUE VISION A/S': 10335.2892,
            'ARCUS ASA': 28779671.413999997
        }
        actual = service.search_data("companyName", [{"tradedate": "201708"}], "valueEUR")

        self.assertEqual(expected, actual)

    def test_2017_tradeSignificance_3_what_is_the_percentage_of_transactions_per_month(self):

        repository = Mock(sepc=DataCSVRepository)

        service = ProcessCSVService(
            repository=repository,
            file_name=self._path + '2017test.csv'
        )

        # values returned by the repository
        repository.get_data_from_csv.return_value = self._transactions

        search_key = [
            {"tradedate": "201701"},
            {"tradedate": "201702"},
            {"tradedate": "201703"},
            {"tradedate": "201704"},
            {"tradedate": "201705"},
            {"tradedate": "201706"},
            {"tradedate": "201707"},
            {"tradedate": "201708"},
            {"tradedate": "201709"},
            {"tradedate": "201710"},
            {"tradedate": "201711"},
            {"tradedate": "201712"},
        ]

        actual = service.pythonics_search(
            search_key,
            [{"tradeSignificance": "3"}, {"tradedate": "2017"}]
        )

        self.assertEqual(self._expected, actual)


if __name__ == '__main__':
    unittest.main()
