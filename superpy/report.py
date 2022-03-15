from datetime import date
import tools
import csv

def show_inventory(filepath, time_frame = date.today()):
    i = 1
    my_dict = {}
    if time_frame == 'today':
        time_frame = str(tools.convert_time_today())
        time_frame = time_frame[:time_frame.find(" ")]


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

        for input in my_dict.values():
            print(input)
