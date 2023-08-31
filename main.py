import csv
from datetime import datetime, timedelta
from icalendar import Calendar, Event, vRecur

def create_ics_file(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        cal = Calendar()

        for row in reader:
            name, birthdate = row[0], row[1]
            event = Event()

            # Parse birthdate from the CSV
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()

            # Set event details
            event.add('summary', f'Anniversaire de : {name}')
            event.add('dtstart', birthdate)
            event.add('dtend', birthdate)

            # Create a repeating rule for annual recurrence
            rrule = vRecur()
            rrule['freq'] = 'yearly'
            rrule['interval'] = 1

            # Set the rule as the event's recurrence rule
            event.add('rrule', rrule)

            # Add event to calendar
            cal.add_component(event)

    return cal

def save_ics_file(cal, output_file):
    with open(output_file, 'wb') as file:
        file.write(cal.to_ical())

    print(f"ICS file '{output_file}' created successfully!")

if __name__ == '__main__':
    csv_file = 'data/formatted_dates.csv'
    output_file = 'data/birthdays.ics'

    calendar = create_ics_file(csv_file)
    save_ics_file(calendar, output_file)

