import json
import csv
import sys

def json_to_csv(json_main):
    with open(json_main) as json_file:
        data = json.load(json_file)
    root_call = json_main.split('.')[0]

    csv_main = f"{root_call}.csv"

    employees_data = data.get('Employees')
    with open(csv_main, 'w', newline='') as csv_file:
        csv_write_in = csv.writer(csv_file)

        csv_write_in.writerow(employees_data[0].keys())
        for employee in employees_data:
            csv_write_in.writerow(employee.values())
json_main = sys.argv[1]
json_to_csv(json_main)