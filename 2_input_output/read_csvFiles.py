import csv

with open('employee.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} have address in {row["address"]} , and was join date at {row["date joined"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')