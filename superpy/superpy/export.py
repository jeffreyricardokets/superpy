import pandas as pd
import tools
from pathlib import Path
import os
from rich import print
from rich.console import Console

console = Console()
exports_folder_path = tools.path / 'exports'

def write_to_excel_file(import_file, export_file ,start_date=0 ,end_date = 0, file_extension= 'xlsx'):
    import_file = tools.folder_path / (import_file + '.csv')
    export_file = exports_folder_path / (export_file + '.' + file_extension)

    if not os.path.isdir(exports_folder_path):
        os.mkdir(exports_folder_path)
        console.print('made the exports folder')

    #check if the xlsx file exist
    if not os.path.isfile(import_file):
        console.print('Cannot find the import file to have a list of import file use command [bold blue]python3 main.py files[/Bold blue]' , style='Bold red')
    elif os.path.isfile(export_file):
        console.print('file already exist please use a different export file name' , style='Bold red')
    else:
        #get information from csv file
        csv_file = pd.read_csv(import_file, sep=',')
        #check if the user want to filter the date
        if start_date != 0 and end_date !=0:
            if 'sell_date' in csv_file:
                column_name = 'sell_date'
            if 'bought_date' in csv_file:
                column_name = 'bought_date'
            #write to excel file
            csv_file[column_name] = pd.to_datetime(csv_file[column_name], format='%Y-%m-%d')
            filtered_csv_file = csv_file.loc[(csv_file[column_name] >= start_date) & (csv_file[column_name] <= end_date)]
            if file_extension == 'xlsx':
                filtered_csv_file.to_excel(export_file, sheet_name="Data", index=False)
            elif file_extension == 'csv':
                filtered_csv_file.to_csv(export_file,index=False)
            else:
                console.print('unsupported file extension', style='Bold red')
        else:
            #user dont want to sort on date and we will write to the excel file
            csv_file.to_excel(export_file, sheet_name="Data", index=False)
            if file_extension == 'xlsx':
                csv_file.to_excel(export_file, sheet_name="Data", index=False)
            elif file_extension == 'csv':
                csv_file.to_csv(export_file, index=False)
            else:
                console.print('unsupported file extension', style='Bold red')
        console.print(f'filename : {export_file} is created. Data was gathered from file : {import_file}', style='Bold green')


def file_list():
    console.print('File names are:' , style='Bold green')
    for file in os.listdir(tools.folder_path):
        if file.endswith('.csv'):
            file = file[:file.find('.')]
            console.print(file)