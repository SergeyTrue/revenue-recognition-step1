import pandas as pd
from tabulate import tabulate


def _group_deferred_invoices(df: pd.DataFrame) ->pd.DataFrame:

    df = df.groupby([
                     'customer_number',
                     'customer_name',
                     'wbs_element',
                     'customer_po',
                     'sales_document',
                     'order_reason',
                     'invoice',
                    ], as_index=False)[['ni', 'cogs']].sum()
    df = df.loc[(df['cogs'] > 0.001) | (df['ni'] > 0.001), :]
    df['action'] = ''
    df['period'] = 'pending_to_recognize'
    df['ni'] = df['ni'].map('{:,.2f}'.format)
    df['cogs'] = df['cogs'].map('{:,.2f}'.format)

    return df


def _group_actual_period_invoices(df: pd.DataFrame) -> pd.DataFrame:

    df = df.groupby([
                     'customer_number',
                     'customer_name',
                     'wbs_element',
                     'customer_po',
                     'sales_document',
                     'order_reason',
                     'invoice',
                    ], as_index=False)[['ni', 'cogs']].sum()

    df['action'] = ''
    df['period'] = 'actual_period'
    df['ni'] = df['ni'].map('{:,.2f}'.format)
    df['cogs'] = df['cogs'].map('{:,.2f}'.format)

    return df


def make_report(actual_df: pd.DataFrame, deferred_df: pd.DataFrame) -> pd.DataFrame:
    deferred_df = _group_deferred_invoices(deferred_df)

    actual_df = _group_actual_period_invoices(actual_df)

    merged_df = actual_df.append(deferred_df)
    merged_df.reset_index(drop=True, inplace=True)
    return merged_df
