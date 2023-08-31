from datetime import datetime
import csv

# Read the CSV file and print dates in the desired format
with open('data/dates.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        date_string = row['date']
        parsed_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        formatted_date = parsed_date.strftime("%Y-%m-%d")
        print(f"{row['name']},{formatted_date}")
