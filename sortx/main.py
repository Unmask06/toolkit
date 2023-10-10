import sys
import traceback
import time

from .core import CustomException, MasterIndex, MiDbParser, MiLister

paths = {"config_path": "", "xl_folder_path": "", "doc_folder_path": ""}



def run_merge_excel(paths):
    try:
        lister = MiLister(config_file_path=paths["config_path"])
        lister.merge_excel(paths["xl_folder_path"])
        lister.write_to_excel()

        lister.logger.info("Done! Files merged.")

    except CustomException as e:
        print(e)
        # print(traceback.format_exc())

def run_update_folder_link(): #! Add folder and file radio button
    try:
        lister = MiLister(config_file_path=paths["config_path"])
        lister.update_file_link(paths["file_path"])
        lister.write_to_excel()

        lister.logger.info("Done! File Path updated.")

    except CustomException as e:
        print(e)
        print(traceback.format_exc())

def run_open_master_index():
    lister = MiLister(config_file_path=paths["config_path"])
    lister.open_master_index()

def run_fill_data():
    db_parser = MiDbParser(config_file_path=paths["config_path"])
    db_parser.fill_missing_data()
    db_parser.write_to_excel()