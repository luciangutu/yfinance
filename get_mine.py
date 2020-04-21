#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import yfinance as yf
from datetime import datetime
import pandas as pd


ticker = yf.Ticker('C')
# always should have info and history for valid symbols
# assert (ticker.info is not None and ticker.info != {})
# assert (ticker.history(period="max").empty is False)
ticker.info
ticker.financials
ticker.balance_sheet
ticker.cashflow
#
# data = "2019-12-31"
# date_format = "%Y-%m-%d"
# date = datetime.strptime(data, date_format)
#
# net_revenue = ticker.financials[date].loc["Net Income"]
# print(net_revenue)
#
# total_revenue = ticker.financials[date].loc["Total Revenue"]
# print(total_revenue)
