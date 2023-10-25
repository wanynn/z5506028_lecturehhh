"""yf_example3"""
"""This module is used to download stock price data for Qantas for a given year and saving it in a CSV file."""
import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv (year):
    """ Download Qantas stock prices for a given year into a CSV file
    Parameters:

        tic : str
        Ticker

    pth : str
        Location of the output CSV file

     start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
        """
    startd=f"{year}-01-01"
    endd=f"{year}-12-31"
    tic="QAN.AX"
    outputfile=f"qan_prc_{year}.csv"
    pth=os.path.join(cfg.DATADIR,outputfile)
    yf_example2.yf_prc_to_csv(tic,pth,startd,endd)

if __name__ == "__main__":
    qan_prc_to_csv(2020)
