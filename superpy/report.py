from calendar import c
import datetime
import tools
import csv
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()

table = Table(show_header=True, header_style='bold #2070b2',
              title='Report')


tools.check_if_folder_exist()
def show_inventory(filepath, time_frame = tools.read_today_handler()):
    i = 1
    my_dict = {}
    converted_time_frame = convert_date_str_to_date(time_frame)
    if converted_time_frame != 'all':
        if not tools.validate_date(converted_time_frame):
            return
    with open(filepath, newline='') as read_file:
        reader = csv.DictReader(read_file)
        list_of_column_names = reader.fieldnames
    
    with open(filepath, newline='') as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if 'sell_date' in row:
                column_name = 'sell_date'
            elif 'bought_date' in row:
                column_name = 'bought_date'

            if 'stock' in str(filepath) or time_frame == 'all':
                my_dict[i] = row
                i = i + 1
            else:
                if len(converted_time_frame) == 7: 
                    my_date = row[column_name][:len(converted_time_frame)]
                else:
                    my_date = row[column_name]
                if my_date == converted_time_frame:
                    my_dict[i] = row
                    i = i + 1

        for column in list_of_column_names:
            table.add_column(column, justify='right')

        for input in my_dict.values():
            a = ([key for key in input.values()])
            table.add_row(*a)

        console.print(table)

def show_profit(input_date):
    output_date = convert_date_str_to_date(input_date)
    if input_date == 'today' or  input_date == 'tomorrow' or input_date == 'yesterday':
        console.print(f'[bold green]Profit from date: {output_date} profit: {calcute_profit_writen(output_date)} [/bold green]')
    else:
        output_date = datetime.datetime.strptime(output_date, "%Y-%m")
        console.print(f'[bold green]Profit from date: year {output_date.year} month {output_date.month} profit: {calcute_profit_date(output_date)} [/bold green]')

def show_revenue(input_date):
    try:
        output_date = convert_date_str_to_date(input_date)
        if input_date == 'today' or  input_date == 'tomorrow' or input_date == 'yesterday':
            print(len('2022-04-17'))
            console.print(f'[bold green]Revenue from date: {output_date} Revenue: {calculate_revenue_written(output_date)} [/bold green]')
        else:
            output_date = datetime.datetime.strptime(output_date, "%Y-%m")
            console.print(f'[bold green]Revenue from date: year {output_date.year} month {output_date.month} revenue: {calculate_revenue_date(output_date)} [/bold green]')
    except:
        console.print('Error please check the readme file', style='Bold red')

def calcute_profit_writen(input_date):
    total_spend = calculate_expenses_written(input_date)
    total_revenue = calculate_revenue_written(input_date)
    return total_revenue - total_spend

def calcute_profit_date(input_date):
    total_spend = calculate_expenses_date(input_date)
    total_revenue = calculate_revenue_date(input_date)
    return total_revenue - total_spend


def calculate_revenue_date(input_date):
    total_sold = 0
    sell_dict = tools.csv_to_dict(tools.sold_file_path)
    for row in sell_dict.values():
        date_of_csv = convert_str_to_date(row['sell_date'])
        if date_of_csv.month == input_date.month and date_of_csv.year == input_date.year:
            total_sold = total_sold + int(row['sell_price'])
    return total_sold 

def calculate_revenue_written(input_date):
    total_sold = 0 
    sell_dict = tools.csv_to_dict(tools.sold_file_path)
    for row in sell_dict.values():
        if row['sell_date'] == input_date:
            total_sold = total_sold + int(row['sell_price'])
    return total_sold 

def calculate_expenses_date(input_date):
    total_bought_in = 0
    buy_dict = tools.csv_to_dict(tools.bought_file_path)
    for row in buy_dict.values():
        date_of_csv = convert_str_to_date(row['bought_date'])
        if date_of_csv.month == input_date.month and date_of_csv.year == input_date.year:
            total_bought_in = total_bought_in + int(row['product_price'])
    return total_bought_in

def calculate_expenses_written(input_date):
    buy_dict = tools.csv_to_dict(tools.bought_file_path)
    total_bought_in = 0
    for row in buy_dict.values():
        if row['bought_date'] == input_date:
            total_bought_in = total_bought_in + int(row['product_price'])
    return total_bought_in



def convert_str_to_date(input):
    return datetime.datetime.strptime(input, "%Y-%m-%d")

def convert_date_str_to_date(input_date):
    input_today = datetime.datetime.strptime(tools.read_today_handler(), '%Y-%m-%d')
    if input_date == 'today':
        return tools.remove_space_from_date_str(input_today)
    elif input_date == 'tomorrow':
        return tools.remove_space_from_date_str(input_today + datetime.timedelta(days = 1))
    elif input_date == 'yesterday':
        return tools.remove_space_from_date_str(input_today + datetime.timedelta(days = -1))
    else:
        return input_date

