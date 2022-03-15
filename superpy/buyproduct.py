import main
import tools
import csv


field_names = ['ID', 'product_name', 'amount' , 'product_price', 'bought_date', 'expire_date']

class product:
    def __init__(self, product_name, price, expire_date, amount):
        self.product_name = product_name
        self.price = price
        self.expire_date = expire_date
        self.amount = amount
        self.date = main.date.today()

    def bought_product(self):
        buy_id = tools.make_id('buy')
        with open(tools.bought_file_path , mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writerow({'ID' :  buy_id, 'product_name': self.product_name, 'amount' : self.amount, 'product_price' : self.price, 'bought_date': self.date ,'expire_date': self.expire_date })
        with open(tools.stock_file_path , mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writerow({'ID' : buy_id , 'product_name': self.product_name, 'amount' : self.amount, 'product_price' : self.price, 'bought_date': self.date ,'expire_date': self.expire_date })
