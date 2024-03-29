import os
import datetime
import openpyxl

DATA_DIR = os.path.join("/quants-data", "daily-data")
BRAND_DIR = os.path.join("/quants-data", "brand-data")
CALENDAR_DIR = os.path.join("/quants-data", "calendar-data")
XLSX_DIR = os.path.join("/quants-data", "xlsx-data")

DEBUG_LEVEL = 1
TEST = False

if TEST:
    NUM_OF_THREADS = 1
else:
    NUM_OF_THREADS = int(os.environ.get('NUM_OF_THREADS'))


def create_dir(path) -> str:
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def year_week_number(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    return f'{year}-{datetime.datetime(year,month,day).strftime("%W")}'


def year_month(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    return f'{year}-{datetime.datetime(year,month,day).strftime("%m")}'


def curren_date():
    return f'{datetime.datetime.today().strftime("%Y-%m-%d")}'


def get_date(past_days):
    current_datetime = datetime.datetime.today()
    return current_datetime + datetime.timedelta(days=-1*past_days)


def brank_workbook():
    __workbook = openpyxl.Workbook()
    __worksheet = __workbook['Sheet']
    __workbook.remove(__worksheet)
    return __workbook


def save_and_close_workbook(workbook, path):
    workbook.save(path)
    workbook.close()
