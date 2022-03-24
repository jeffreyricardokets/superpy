from dataclasses import dataclass
import datetime
import tools
import csv
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style='bold #2070b2',
              title='Report')


def show_inventory(filepath, time_frame = datetime.date.today()):
    i = 1
    my_dict = {}
    if time_frame == 'today':
        time_frame = str(tools.read_today_handler())
        time_frame = time_frame[:time_frame.find(" ")]

    with open(filepath, newline='') as read_file:
        reader = csv.DictReader(read_file)

        dict_from_csv = dict(list(reader)[0])
        list_of_column_names = list(dict_from_csv.keys())

    with open(filepath, newline='') as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if filepath == tools.sold_file_path:
                sell_bought_row = 'sell_date'
            else:
                sell_bought_row = 'bought_date'
            if row[sell_bought_row] == time_frame:
                my_dict[i] = row
                i = i + 1

    for column in list_of_column_names:
        table.add_column(column, justify='right')



    for input in my_dict.values():
        a = ([key for key in input.values()])
        table.add_row(*a)

    console.print(table)

def show_revenue(input_date):
    input_today = datetime.datetime.strptime(tools.read_today_handler(), '%Y-%m-%d')
    if input_date == 'today':
        input_date = input_today
    elif input_date == 'tomorrow':
        input_date = input_today + datetime.timedelta(days = 1)
    elif input_date == 'yesterday':
        input_date = input_today + datetime.timedelta(days = -1)
    else:
        print('test')
    print (input_date)
