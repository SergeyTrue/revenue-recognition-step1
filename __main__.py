from tabulate import tabulate

from rr_step_one.input_process import input_from_cmd, get_data_from_input
from rr_step_one.common.config import HISTORY, PERIOD
from rr_step_one.processor import make_report
from rr_step_one.output import save_to_xl

input_data = input_from_cmd()
actual_sales_df, historical_sales_df, period = get_data_from_input(input_data, HISTORY)
report_df = make_report(actual_sales_df, historical_sales_df)
save_to_xl(report_df, actual_sales_df)
with open(PERIOD, 'w') as stream:
    stream.write(period)

print(tabulate(report_df, headers='keys', tablefmt='psql'))


