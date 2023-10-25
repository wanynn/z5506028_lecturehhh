import pandas as pd
import numpy as np


# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    aud_usd = pd.Series([val for row_id, val in aud_usd_info], index=[row_id for row_id, val in aud_usd_info])
    eur_aud = pd.Series([val for row_id, val in eur_aud_info], index=[row_id for row_id, val in eur_aud_info])
    dates = sorted(set(date for row_id, date in date_info))
    aud_usd_values = [aud_usd.get(row_id, np.nan) for row_id, date in date_info]
    eur_aud_values = [eur_aud.get(row_id, np.nan) for row_id, date in date_info]
    df = pd.DataFrame({'AUD/USD': aud_usd_values, 'EUR/AUD': eur_aud_values}, index=dates)
    return df


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11, '2020-09-08'),
    (70, '2020-09-09'),
    (99, '2020-09-10'),
    (4, '2020-09-11'),
    (7, '2020-09-14'),
    (100, '2020-09-15'),
]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70, 0.7209),
    (4, 0.7263),
    (11, 0.7280),
    (7, 0.7281),
    (100, 0.7285),
]

# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70, 1.6321),
    (4, 1.6282),
    (99, 1.6221),
    (100, 1.6288),
    (11, 1.6232),
]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)
