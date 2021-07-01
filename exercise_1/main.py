import sys
from os import system

from app.adapter.app_repository import AppDataCSVRepository
from app.domain.service import ProcessCSVService


def main():
    app_data_csv_repository = AppDataCSVRepository()
    service = ProcessCSVService(app_data_csv_repository, "2017.csv")

    clear_screen()

    ###############################################################################
    # Option 1: Do it yourself

    # Question 1
    print("Q1: What Exchange has had the most transactions in the file?")

    filtered_data = service.search_data("exchange")
    exchange = max(filtered_data, key=filtered_data.get)
    print("A1:", exchange)

    if exchange == "off exchange":
        print("\n\tIf off exchange is not considered as Exchange, the answer is:")
        filtered_data["off exchange"] = 0
        print(f"\tA1: {max(filtered_data, key=filtered_data.get)}")

    # Question 2
    print("\nQ2: In August 2017, which companyName had the highest combined valueEUR?")

    filtered_data = service.search_data("companyName", [{"tradedate": "201708"}], "valueEUR")
    print("A2:", max(filtered_data, key=filtered_data.get))

    ################################################################################
    # Option 2: More pythonics
    # Question 3

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

    print("\nQ3: For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?")

    service.format_print_percent(
        service.pythonics_search(search_key, [{"tradeSignificance": "3"}, {"tradedate": "2017"}])
    )

    print("\nFor the calculation of the percentages, only the 2017 operations that meet the given criteria were taken as an indicator\n\n")


def clear_screen() -> None:
    if sys.platform == "win32":
        system("cls")
    elif sys.platform in ('linux', 'linux2'):
        system("clear")


if __name__ == '__main__':
    main()
