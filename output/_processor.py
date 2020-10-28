import os

import pandas as pd
import time
import tempfile

from rr_step_one.common.config import LAST_RUN


def save_to_xl(report_df: pd.DataFrame, actual_sales_df:  pd.DataFrame):

    actual_sales_df.to_excel(LAST_RUN, index=False, engine='openpyxl')

    file_name = time.strftime('%Y-%m-%d_%H-%M-%S') + '_to_recognize.xlsx'
    os.chdir(tempfile.gettempdir())
    report_df.to_excel(file_name, index=False, engine='openpyxl')
    os.system(f'start excel {file_name}')

