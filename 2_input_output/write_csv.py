import csv

with open('employee_file.csv', mode='w') as employee_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    employee_writer = csv.writer(employee_file, delimiter=',')

    employee_writer.writerow(fieldnames)
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])