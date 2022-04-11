# Imports
import argparse
from sys import argv
import buyproduct
import tools
import report
import sales
import export



# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    tools.check_if_folder_exist()
    tools.check_if_file_exist(tools.stock_file_path)
    tools.check_if_file_exist(tools.bought_file_path)
    tools.check_if_file_exist(tools.sold_file_path)
    tools.clean_stock()
    request_input_parser()
    pass


if __name__ == "__main__":

    def request_input_parser():

        #create the top-level parser
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest = 'command')

        #create the parser for report
        parser_inventory = subparser.add_parser('report', help='Report a sets of data')
        parser_inventory.add_argument('--inventory', action='store_true', help='show the inventory')
        parser_inventory.add_argument('--sales' , help='show the sales')
        parser_inventory.add_argument('--orders', help='show the orders')
        parser_inventory.add_argument('--profit', help='show the profit')
        parser_inventory.add_argument('--revenue', help='show the revenue')

        #create the parser for buy
        parser_buy = subparser.add_parser('buy', help='Buy a product')
        parser_buy.add_argument('--product-name', help='the product that we want to buy')
        parser_buy.add_argument('--price' , help='the price that we want to buy each product')
        parser_buy.add_argument('--expire-date', help='the expire date of the product format YYYY-MM-DD')
        parser_buy.add_argument('--amount', help='the ammount of products we want to buy')

        #create the parser for selling
        parser_sell = subparser.add_parser('sell', help='Sell a product')
        parser_sell.add_argument('--product-name', help='product that we want to seel')
        parser_sell.add_argument('--price', help='the product price')

        #create the parser for advance time
        parser_adv_time = subparser.add_parser('advancetime', help='advance time')
        parser_adv_time.add_argument('--days', help='select the days we want to advance')
        parser_adv_time.add_argument('--weeks', help='select the weeks we want to advance')

        #creat the parser for export
        parser_export = subparser.add_parser('export', help='export a set of data')
        parser_export.add_argument('--import-file', help='import file')
        parser_export.add_argument('--export-file', help='export file')
        parser_export.add_argument('--start-date', help='start date')
        parser_export.add_argument('--end-date', help='end date')
        parser_export.add_argument('--file-extension', help='select file extension')

        #creat the parser to see the files in data
        parser_file = subparser.add_parser('files', help='see the filenames in data')

        args = parser.parse_args()

        if args.command == 'report':
            if args.inventory:
                report.show_inventory(tools.stock_file_path, args.inventory)
            if args.sales:
                report.show_inventory(tools.sold_file_path, args.sales)
            if args.orders:
                report.show_inventory(tools.bought_file_path, args.orders)
            if args.profit:
                report.show_profit(args.profit)
            if args.revenue:
                report.show_revenue(args.revenue)

            
        if args.command == 'buy':
            if tools.validate_date(args.expire_date):
                if args.product_name and args.price and args.expire_date and args.amount:
                    buy_stock = buyproduct.product(args.product_name, args.price, args.expire_date, args.amount)
                    buy_stock.bought_product()
                else:
                    print('Error: not all data is filled in')

        if args.command == 'sell':
            if args.product_name and args.price:
                sales.sell_product(args.product_name,args.price)
            else:
                print('Error: not all data is filled in')

        if args.command == 'advancetime':
            if args.days and args.weeks:
                tools.write_today_handler(args.days, args.weeks)
            if args.days:
                tools.write_today_handler(args.days)
            if args.weeks:
                tools.write_today_handler(args.weeks)

        if args.command == 'export':
            if args.start_date and args.end_date:
                if tools.validate_date(args.start_date) and tools.validate_date(args.end_date):
                    if(args.file_extension):
                        export.write_to_excel_file(args.import_file, args.export_file, args.start_date, args.end_date, args.file_extension)
                    else:
                        export.write_to_excel_file(args.import_file, args.export_file, args.start_date, args.end_date)
            else:
                if(args.file_extension):
                    export.write_to_excel_file(args.import_file, args.export_file,0,0, args.file_extension)
                else:
                    export.write_to_excel_file(args.import_file, args.export_file)
        
        if args.command == 'files':
            export.file_list()



    main()