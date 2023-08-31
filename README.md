# py-write-ics

> Generate a valid ics file with several recurring events using Python's icalendar package from a csv file containing dates

## Installation

Clone the repository :

```
git clone https://github.com/spinning-fantasies/py-write-ics.git
```

Enable a virtualenv :

```
cd py-write-ics
python - venv .
source ./bin/activate
```


## Usage

Format dates from a csv file with ``name`` and ``date`` columns and print the output to ``formatted_dates.csv`` :

|name|date|
-----|----|
|John Doe|01/05/1984|

```
python format_dates.py > formatted_dates.csv
```

Generate an ics file :

```
python main.py
```
