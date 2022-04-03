import pandas as pd
import tools
from pathlib import Path
import os
from rich import print
from rich.console import Console

console = Console()

def write_to_excel_file(import_file, export_file):
    import_file = tools.folder_path / (import_file + '.csv')
    export_file = tools.folder_path / (export_file + '.xlsx')

    #check if the xlsx file exist
    if not os.path.isfile(import_file):
        console.print('Cannot find the import file to have a list of import file use command files' , style='Bold red')
    elif os.path.isfile(export_file):
        console.print('file already exist please use a different export file name' , style='Bold red')
    else:
        csv_file = pd.read_csv(import_file)
        csv_file.to_excel(export_file, sheet_name="Data", index=False)
        console.print(f'filename : {export_file} is created. Data was gathered from file : {import_file}', style='Bold green')

def file_list():
    console.print('File names are:' , style='Bold green')
    for file in os.listdir(tools.folder_path):
        if file.endswith('.csv'):
            file = file[:file.find('.')]
            console.print(file)