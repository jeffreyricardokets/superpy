import csv
from pathlib import Path
import os
import datetime
import buyproduct
import sales
from rich.console import Console
from rich import print

console = Console()


path = Path(os.path.realpath(__file__)).parent.absolute()
folder_path = path / 'data'
bought_file_path = folder_path / 'bought.csv'
sold_file_path = folder_path / 'sold.csv'
stock_file_path = folder_path / 'stock.csv'
datetoday_file_path = folder_path / 'datetoday.txt'


def check_if_folder_exist():
    if not os.path.isdir(folder_path):
        try:
            os.makedirs(folder_path)
            print('made a folder')
        except:
            print('something went wrong with creating a folder')


def check_if_file_exist(file_path):
    if not os.path.isfile(file_path):
        with open(file_path , mode="w") as csv_file:
            if file_path == datetoday_file_path:
                csv_file.write(str(datetime.date.today()))
            else:
                if file_path == bought_file_path or stock_file_path:
                    writer = csv.DictWriter(csv_file, fieldnames=buyproduct.field_names)
                if file_path == sold_file_path:
                    writer = csv.DictWriter(csv_file, sales.field_names)
                writer.writeheader()

def validate_date(date_text):
    try:
        if len(date_text) > 7:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        else:
            datetime.datetime.strptime(date_text, '%Y-%m')
        return True
    except ValueError:
        console.print('ERROR: Incorrect data form it should be YYYY-MM-DD', style='Bold red')
        return False


def make_id(action):
    if action == 'buy':
        file_path = bought_file_path
    elif action == 'sell':
        file_path = sold_file_path
    with open(file_path, newline='') as read_file:
        id_list = []
        reader = csv.DictReader(read_file)
        for row in reader:
            id_list.append(int(row['ID']))
        if id_list == []:
            return 1
        return (max(id_list)) + 1


def clean_stock():
    myDict = {}
    i = 0
    with open(stock_file_path, mode='r') as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            myDict[i] = {'ID': row['ID'], 'product_name': row['product_name'], 'amount': row['amount'], 'product_price': row['product_price'], 'bought_date': row['bought_date'], 'expire_date': row['expire_date'] }
            i = i +1
    with open(stock_file_path, mode='w') as writefile:
        writer = csv.DictWriter(writefile, fieldnames=buyproduct.field_names)
        writer.writeheader()
        for i in myDict.values():
            convert_date = datetime.datetime.strptime(i['expire_date'],'%Y-%m-%d')
            convert_time_today = datetime.datetime.strptime(read_today_handler(),'%Y-%m-%d')
            if convert_date >= convert_time_today:
                writer.writerow({'ID' : i['ID'] , 'product_name': i['product_name'], 'amount' : i['amount'], 'product_price' : i['product_price'], 'bought_date': i['bought_date'] ,'expire_date': i['expire_date'] })
            else:
                console.print('Today ' + read_today_handler() + ' Product : '+ i['product_name'] + ' is removed from stock due expiration date', style='Bold red')
                console.print('The expire date was ' + i['expire_date'], style='Bold red')

def read_today_handler():
    check_if_file_exist(datetoday_file_path)
    str_date_today = str(datetime.date.today())
    str_date_today = str_date_today[:str_date_today.find(" ")]
    with open(datetoday_file_path, mode='r') as readfile:
        return readfile.readline()

def write_today_handler(day_int = 0, week_int = 0):
    day_int = int(day_int)
    week_int = int(week_int)
    old_date = datetime.datetime.strptime(read_today_handler(), '%Y-%m-%d')
    new_date = str(old_date + datetime.timedelta(days = day_int, weeks = week_int))
    new_date = new_date[:new_date.find(" ")]
    with open(datetoday_file_path , mode='w') as writefile:
        writefile.write(str(new_date))
        console.print(f'New date is {new_date}')

def csv_to_dict(filename):
    my_dict = {}
    my_counter = 1
    with open(filename, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            my_dict[my_counter] = row
            my_counter = my_counter + 1
    return(my_dict)

def remove_space_from_date_str(input):
    input_date = str(input)
    return input_date[:input_date.find(' ')]
