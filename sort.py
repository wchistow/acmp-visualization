import csv
import pandas as pd


def download_status():
    pd.read_csv('https://acmp.ru/download/status.7z',
                sep=';').to_csv('status.csv')


def write_year(year):
    filename = f'status_{year}.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        while True:
            row = yield
            writer.writerow(row)


def read():
    with open('status.csv') as f:
        reader = csv.reader(f, delimiter=';')
        yield from reader


writers = {str(year): write_year(year) for year in range(2006, 2023)}
for writer in writers.values():
    next(writer)

for row in read():
    year = row[1][6:10]
    writers[year].send(row)
