import tools
import buyproduct
import csv
import datetime

fieldnames = ['ID', 'bought_id', 'sell_date', 'sell_price']

def sell_product(product_name, price):
    tools.check_if_file_exist(tools.sold_file_path)
    stock_file = tools.csv_to_dict(tools.stock_file_path)
    product_in_stock = check_in_stock(stock_file,product_name)
    if product_in_stock:
        product = product_to_sell(stock_file, product_name)
        with open(tools.stock_file_path, mode='w') as csv_writer:
            dict_writer = csv.DictWriter(csv_writer, fieldnames=buyproduct.field_names)
            dict_writer.writeheader()
            for row in stock_file.values():
                if int(row['amount']) <= 0:
                    print('row delete')
                else:
                    dict_writer.writerow(row)
        with open(tools.sold_file_path, mode='a') as csv_append:
            dict_writer = csv.DictWriter(csv_append, fieldnames=fieldnames)
            dict_writer.writerow(add_product_to_sales_list(product,price))
    else:
        print('product not in stock')

def add_product_to_sales_list(product, price):
    return {'ID': tools.make_id('sell'), 'bought_id': product['ID'], 'sell_date': tools.read_today_handler(), 'sell_price': price} 

def check_in_stock(stock_file, product_name):
    for row in stock_file.values():
        if row['product_name'] == product_name:
            return True
    return False

def product_to_sell(buyDict, product_name):
    expir_date = datetime.datetime(9999,12,31).strftime("%Y %b %d")
    best_product_to_sell = {}
    for row in buyDict.values():
        if row['product_name'] == product_name:
            if not row['amount'] == 0:
                if expir_date > row['expire_date']:
                    expir_date = row['expire_date']
                    best_product_to_sell = row
    best_product_to_sell['amount'] = int(best_product_to_sell['amount']) - 1
    return best_product_to_sell

