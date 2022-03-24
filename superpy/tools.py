from calendar import week
import csv
from pathlib import Path
import os
from datetime import date
from datetime import datetime
import datetime
import buyproduct
import sales


path = Path(os.path.realpath(__file__)).parent.absolute()
folder_path = path / 'data'
bought_file_path = folder_path / 'bought.csv'
sold_file_path = folder_path / 'sold.csv'
stock_file_path = folder_path / 'stock.csv'
datetoday_file_path = folder_path / 'datetoday.txt'
"""
buy_fieldnames = ['ID', 'product_name', 'amount' , 'product_price', 'bought_date', 'expire_date']
sell_fieldnames = ['ID', 'bought_id', 'sell_date', 'sell_price']
"""

def check_if_folder_exist():
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
        print('made a folder')



def check_if_file_exist(file_path):
    if not os.path.isfile(file_path):
        with open(file_path , mode="w") as csv_file:
            #we check if this is the bought file path or sold that three different files need different headers
            if file_path == datetoday_file_path:
                csv_file.write(str(convert_time_today()))
            else:
                if file_path == bought_file_path or stock_file_path:
                    writer = csv.DictWriter(csv_file, fieldnames=buyproduct.fieldnames)
                if file_path == sold_file_path:
                    writer = csv.DictWriter(csv_file, sales.fieldnames)
                writer.writeheader()

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

def convert_time_today():
        time_today = str(date.today()).replace('-', ' ').split()
        time_today = map(int, time_today)
        time_today = list(time_today)
        time_today = datetime.datetime(time_today[0],time_today[1],time_today[2])
        return time_today

def clean_stock():
    myDict = {}
    i = 0
    with open(stock_file_path, mode='r') as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            myDict[i] = {'ID': row['ID'], 'product_name': row['product_name'], 'amount': row['amount'], 'product_price': row['product_price'], 'bought_date': row['bought_date'], 'expire_date': row['expire_date'] }
            i = i +1
    with open(stock_file_path, mode='w') as writefile:
        writer = csv.DictWriter(writefile, fieldnames=buyproduct.fieldnames)
        writer.writeheader()
        time_today = convert_time_today()
        for i in myDict.values():
            converdate = i['expire_date'].replace('-', ' ').split()
            converdate = map(int,converdate)
            converdate = list(converdate)
            converdate = datetime.datetime(converdate[0],converdate[1],converdate[2])
            if converdate >= time_today:
                writer.writerow({'ID' : i['ID'] , 'product_name': i['product_name'], 'amount' : i['amount'], 'product_price' : i['product_price'], 'bought_date': i['bought_date'] ,'expire_date': i['expire_date'] })
            else:
                print('deteled row')

def read_today_handler():
    check_if_file_exist(datetoday_file_path)
    str_date_today = str(convert_time_today())
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

def csv_to_dict(filename):
    my_dict = {}
    my_counter = 1
    with open(filename, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            my_dict[my_counter] = row
            my_counter = my_counter + 1
    return(my_dict)

