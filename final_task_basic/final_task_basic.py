import random
import csv
import os

def FileLoad(nick, sep=','):
    with open(nick, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=sep)
        data = [row for row in reader]
    return data

def Directories(data):
    if not os.path.exists('workdata'):
        os.makedirs('workdata')
    if not os.path.exists('workdata/Learning'):
        os.makedirs('workdata/Learning')
    if not os.path.exists('workdata/Testing'):
        os.makedirs('workdata/Testing')
    head_row = data[0]
    rows = data[1:]
    train_size = int(len(rows) * 0.7)
    train_data = random.sample(rows, train_size)
    test_data = [row for row in rows if row not in train_data]
    SaveFile('workdata/Learning/train.csv', [head_row] + train_data)
    SaveFile('workdata/Testing/test.csv', [head_row] + test_data)
    print("Saved!")

def SaveFile(filename, data, separator=','):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=separator)
        writer.writerows(data)

def Show(data, what_type='top', num_rows=5):
    head_row = data[0]
    rows = data[1:]
    if len(rows) < num_rows:
        print(f"Not enough rows! Total: {len(rows)}")
        num_rows = len(rows)
    if what_type == 'top':
        information_show = rows[:num_rows]
    elif what_type == 'bottom':
        information_show = rows[-num_rows:]
    elif what_type == 'random':
        information_show = random.sample(rows, num_rows)
    TableOutput([head_row] + information_show)

def Info(data):
    head_row = data[0]
    rows = data[1:]
    num_rows = len(rows)
    num_cols = len(head_row)
    print(f"{num_rows}x{num_cols}")
    column_info = []
    for col_index, column_name in enumerate(head_row):
        non_null = sum(1 for row in rows if row[col_index].strip())
        col_type = InfoVariableType([row[col_index] for row in rows if row[col_index].strip()])
        column_info.append(f"{column_name}: {non_null} Non null variables, type: {col_type}")
    for smth in column_info:
        print(smth)

def DelNaN(data):
    head_row = data[0]
    rows = data[1:]
    initial_rows = len(rows)
    rows = [row for row in rows if all(field.strip() for field in row)]
    remains = len(rows)
    print(f"Rows deleted: {initial_rows - remains}")
    return [head_row] + rows

def TableOutput(data):
    col_widths = [max(len(str(value)) for value in column) for column in zip(*data)]
    row_format = ' $ '.join(f'{{:<{width}}}' for width in col_widths)
    print(row_format.format(*data[0]))
    for row in data[1:]:
        print(row_format.format(*row))

def InfoVariableType(valuables):
    for value in valuables:
        try:
            int(value)
            return "int"
        except:
            try:
                float(value)
                return "float"
            except:
                return "str"
    return "str"

def SaveFile(filename, data, separator=','):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=separator)
        writer.writerows(data)

fileNickname = 'Titanic.csv'
sep = ','
data = FileLoad(fileNickname, sep)
Show(data, view_type='top', num_rows=5)
Info(data)
cleaning = DelNaN(data)
Directories(cleaning)