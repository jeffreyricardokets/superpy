# Imports
import argparse
import csv
from datetime import date
from datetime import datetime
import datetime
from sys import argv
import sys
import os
from pathlib import Path
import buyproduct
import tools
import report

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    
    check_if_file_exist(stock_file_path)
    request_input_parser()
    check_if_folder_exist()
    check_if_file_exist(bought_file_path)

    pass


if __name__ == "__main__":
    
    path = Path(os.path.realpath(__file__)).parent.absolute()
    folder_path = path / 'data'
    bought_file_path = folder_path / 'bought.csv'
    sold_file_path = folder_path / 'sold.csv'
    stock_file_path = folder_path / 'stock.csv'
    buy_fieldnames = ['ID', 'product_name', 'amount' , 'product_price', 'bought_date', 'expire_date']
    sell_fieldnames = ['ID', 'bought_id', 'sell_date', 'sell_price']

    


    def request_input_parser():

        #create the top-level parser
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest = 'command')

        #create the parser for report
        parser_inventory = subparser.add_parser('report', help='report_ help')
        parser_inventory.add_argument('--inventory')
        parser_inventory.add_argument('--sales')
        parser_inventory.add_argument('--orders')

        #create the parser for buy
        parser_buy = subparser.add_parser('buy', help='buy a product')
        parser_buy.add_argument('--product-name')
        parser_buy.add_argument('--price')
        parser_buy.add_argument('--expire-date')
        parser_buy.add_argument('--amount')

        #create the parser for selling
        parser_sell = subparser.add_parser('sell', help='sell a product')
        parser_sell.add_argument('--product-name')
        parser_sell.add_argument('--price')

        #create the parser for clean_stock
        parser_cleanstock = subparser.add_parser('cleanstock', help='clean the stock')

        args = parser.parse_args()
        print(args)

        if args.command == 'report':
            if args.inventory:
                report.show_inventory(stock_file_path, args.inventory)
            if args.sales:
                report.show_inventory(sold_file_path, args.sales)
            if args.orders:
                report.show_inventory(bought_file_path, args.orders)
            
        if args.command == 'buy':
            buy_stock = buyproduct.product(args.product_name, args.price, args.expire_date, args.amount)
            buy_stock.bought_product()
        if args.command == 'sell':
            sell_product(args.product_name,args.price)
        if args.command == 'cleanstock':
            tools.clean_stock()

        
    def check_if_folder_exist():
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
            print('made a folder')



    def check_if_file_exist(file_path):
        if not os.path.isfile(file_path):
            with open(file_path , mode="w") as csv_file:
                #we check if this is the bought file path or sold that three different files need different headers
                if file_path == bought_file_path or stock_file_path:
                    writer = csv.DictWriter(csv_file, fieldnames=buy_fieldnames)
                if file_path == sold_file_path:
                    writer = csv.DictWriter(csv_file, sell_fieldnames)
                writer.writeheader()
            



#migrate this to sell.py
    def sell_product(product_name, sell_price,ammount_of_product = 6):
        check_if_file_exist(sold_file_path)
        buyDict = {}
        sellDict = {}
        stock_of_item = 0
        i = 1
        p = 0
        with open(stock_file_path, newline='') as read_file:
            reader = csv.DictReader(read_file)
            for row in reader:
                if row['product_name'] == product_name:
                    new_time = row['expire_date'].replace('-', ' ').split()
                    map_object = map(int, new_time)
                    new_time = list(map_object)
                    rftime = datetime.datetime(new_time[0],new_time[1],new_time[2]).strftime("%Y-%m-%d")
                    buyDict[i]  = {'ID': row['ID'], 'product_name': row['product_name'], 'amount': row['amount'], 'product_price': row['product_price'], 'bought_date': row['bought_date'], 'expire_date': rftime  }
                    i = i + 1

            for i in buyDict.values():
                stock_of_item = stock_of_item + int(i['amount'])

            if stock_of_item < ammount_of_product:
                print('not enough stock')
            else:
                with open(stock_file_path, mode='w') as writeFile:
                    writer = csv.DictWriter(writeFile, fieldnames=buy_fieldnames)
                    writer.writeheader()

                    while ammount_of_product > 0:
                        for i in buyDict.values():
                            best_product_to_sell = product_to_sell(buyDict)
                            if i['ID'] == best_product_to_sell['ID']:
                                for o in range(int(i['amount'])):
                                    i['amount'] = int(i['amount']) - 1
                                    ammount_of_product = ammount_of_product - 1
                                    if i['amount'] == 0:
                                        counter = 1
                                        for k in buyDict.values():
                                            if not i['amount'] == 0:
                                                buyDict[counter] = k
                                                counter = counter + 1
                                        break
                                    if ammount_of_product == 0:
                                        break                     
                            if int(i['amount']) > 0:
                                writer.writerow({'ID' : i['ID'] , 'product_name': i['product_name'], 'amount' : i['amount'], 'product_price' : i['product_price'], 'bought_date': i['bought_date'] ,'expire_date': i['expire_date'] })
                    

                with open(sold_file_path, mode='a') as csv_file:
                    for i in buyDict.values():
                        writer = csv.DictWriter(csv_file, fieldnames=sell_fieldnames)
                        writer.writerow({'ID' : tools.make_id('sell'), 'bought_id' : i['ID'], 'sell_date' : date.today(), 'sell_price' : sell_price})



                
    def product_to_sell(buyDict):
        expir_date = datetime.datetime(9999,12,31).strftime("%Y %b %d")
        best_product_to_sell = {}
        for i in buyDict.values():
            if not i['amount'] == 0:
                if expir_date > i['expire_date']:
                    expir_date = i['expire_date']
                    best_product_to_sell = i
        return best_product_to_sell



    main()





