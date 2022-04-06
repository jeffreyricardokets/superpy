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
    request_input_parser()
    pass


if __name__ == "__main__":

    def request_input_parser():

        #create the top-level parser
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest = 'command')

        #create the parser for report
        parser_inventory = subparser.add_parser('report', help='report_ help')
        parser_inventory.add_argument('--inventory', action='store_true')
        parser_inventory.add_argument('--sales')
        parser_inventory.add_argument('--orders')
        parser_inventory.add_argument('--profit')
        parser_inventory.add_argument('--revenue')

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

        #create the parser for advance time
        parser_adv_time = subparser.add_parser('advancetime', help='advance time')
        parser_adv_time.add_argument('--days')
        parser_adv_time.add_argument('--weeks')

        #create the parser for clean_stock
        parser_cleanstock = subparser.add_parser('cleanstock', help='clean the stock')

        #creat the parser for export
        parser_export = subparser.add_parser('export', help='export')
        parser_export.add_argument('--import-file', help='import file')
        parser_export.add_argument('--export-file', help='export file')
        parser_export.add_argument('--start-date', help='start date')
        parser_export.add_argument('--end-date', help='end date')
        parser_export.add_argument('--file-extension', help='select file extension')

        #creat the parser to see the files in data
        parser_file = subparser.add_parser('files', help='see the filenames in data')

        args = parser.parse_args()
        print(args)

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
            buy_stock = buyproduct.product(args.product_name, args.price, args.expire_date, args.amount)
            buy_stock.bought_product()

        if args.command == 'sell':
            sales.sell_product(args.product_name,args.price)
        if args.command == 'cleanstock':
            tools.clean_stock()

        if args.command == 'advancetime':
            if args.days and args.weeks:
                tools.write_today_handler(args.days, args.weeks)
            if args.days:
                tools.write_today_handler(args.days)
            if args.weeks:
                tools.write_today_handler(args.weeks)

        if args.command == 'export':
            if args.start_date and args.end_date:
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