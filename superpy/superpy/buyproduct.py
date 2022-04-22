import tools
import csv
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="[bold green] Gekocht product[/bold green]")

field_names = ['ID', 'product_name', 'amount' , 'product_price', 'bought_date', 'expire_date']

class product:
    def __init__(self, product_name, price, expire_date, amount):
        self.product_name = product_name
        self.price = price
        self.expire_date = expire_date
        self.amount = amount
        self.date = tools.read_today_handler()
        self.total_price =  int(price) *  int(amount)

    def bought_product(self):
        buy_id = str(tools.make_id('buy'))
        buy_dict = {'ID' :  buy_id, 'product_name': self.product_name, 'amount' : self.amount, 'product_price' : str(self.total_price), 'bought_date': self.date ,'expire_date': self.expire_date }
        with open(tools.bought_file_path , mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writerow(buy_dict)
        with open(tools.stock_file_path , mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writerow(buy_dict)
        for column in buy_dict:
            table.add_column(column)
        list_of_values = [key for key in buy_dict.values()]
        table.add_row(*list_of_values)
        console.print(table)