from datetime import datetime

'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
### Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}
### Do not change anything in the section above, it is just setting up some sample data


def date_to_display_date(date):
    # E.g. Monday 8th February, 2021
    return f'{date.strftime("%A")} {date.strftime("%d")}th {date.strftime("%B")}, {date.strftime("%Y")}'


def print_report(start, end):
    print("\nSales Report\n")
    print(f'Report start date: {date_to_display_date(start["date"])}. Starting value: ${start["sales"]:8.2f}')
    print(f'Report end date:   {date_to_display_date(end["date"])}. Ending Value:   ${end["sales"]:8.2f}\n')
    total = 0
    print("Date\t\t\t\t    Sales\tMount to Date  ")
    for key, value in test_data.items():
        if month == "2" and key == "29":
            print("Leap year")  # Must be displayed if data is for a leap year
        total += value["sales"]
        print(f"{date_to_display_date(value['date'])}\t${value['sales']:8.2f}\t${total:8.2f}")

    print(f"\nTotal sales for the month: ${total:.2f}\n")


print_report(test_data['1'], test_data['28'])


