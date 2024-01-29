import os
import datetime

DATA_DIR = os.path.join(os.environ.get('HOME'), "quonts_data")
DEBUG_LEVEL = 1


def create_dir(path) -> str:
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_date(past_days):
    current_datetime = datetime.datetime.today()
    return current_datetime + datetime.timedelta(days=-1*past_days)
