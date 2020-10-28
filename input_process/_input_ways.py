import argparse
import pathlib

from ._input_data import InputData


def input_from_cmd() -> InputData:

    parser = argparse.ArgumentParser()
    parser.add_argument('--actual_period_sales', type=str, required=True)

    args = vars(parser.parse_args())
    actual_period_sales = pathlib.Path(args['actual_period_sales'])

    input_ = InputData(actual_period_sales=actual_period_sales)
    return input_

#r' https://deglsappj2.delaval.local:51401/irj/servlet/prt/portal/prtroot/pcd!3aportal_content!2fcom.sap.pct!2fplatform_add_ons!2fcom.sap.ip.bi!2fiViews!2fcom.sap.ip.bi.bex?BOOKMARK=00O2THWO6XQCG9VZZIGM1LHLO '