# from functools import lru_cache
# import yfinance as yf
from db_conn import MySQLDatabase

# def get_fcf_positive_years(ticker):         
#     cashflow = ticker.cashflow
#     if cashflow.empty : 
#         return None 
#     else : 
#         fcf = cashflow.loc["Free Cash Flow"]
#         fcf_positive_years = (fcf > 0).sum()
#         return fcf_positive_years

# def get_fcf_positive_quarters(ticker):
#     quarterly_cashflow = ticker.quarterly_cashflow
#     if quarterly_cashflow.empty : 
#         return None 
#     else : 
#         fcf_positive_quarters = (quarterly_cashflow.loc["Free Cash Flow"] > 0).sum()
#         return fcf_positive_quarters    
    
# def get_equity_steady_years(ticker):
#     annual_balance_sheet = ticker.balance_sheet
#     if annual_balance_sheet.empty : 
#         return None 
#     else : 
#         equity_growth_years = (annual_balance_sheet.loc["Ordinary Shares Number"].sort_index().pct_change()*100 < 1).sum()
#         return equity_growth_years
    
# def workflow():
#     @lru_cache(maxsize=None)
#     def get_ticker_attributes(): 
#         ticker_names = [
#             'CPS',
#             'XPEV',
#             'PYPL',
#         ]
#         tickers = yf.Tickers(" ".join(ticker_names))
#         ticker_attributes = {}
#         for ticker_name in tickers.tickers.keys() : 
#             yahoo_ticker = tickers.tickers[ticker_name]
#             attributes_dict = {}
#             attributes_dict["fcf_positive_years"] = get_fcf_positive_years(yahoo_ticker)
#             attributes_dict["fcf_positive_quarters"] = get_fcf_positive_quarters(yahoo_ticker)
#             attributes_dict["equity_steady_years"] = get_equity_steady_years(yahoo_ticker)
#             ticker_attributes[ticker_name] = attributes_dict
#         return ticker_attributes
#     ticker_attributes = get_ticker_attributes()
    
#     return ticker_attributes
        



def workflow2(): 
    db = MySQLDatabase()
    name_list = ("CPS", "AAPL") # get_all_russell_2000_equities + S&P 500 equities
    query = f"""    
        SELECT bs.act_symbol, bs.date, bs.period, bs.common_stock,  bs.shares_outstanding, 
               cf.net_income, 
               (cf.net_cash_from_operating_activities + cf.property_and_equipment) AS fcf,
               cf.net_cash_from_operating_activities AS ocf
        FROM balance_sheet_equity AS bs
        INNER JOIN cash_flow_statement as cf 
            ON bs.act_symbol = cf.act_symbol 
            AND bs.date = cf.date
            AND bs.period = cf.period
        WHERE bs.act_symbol IN {name_list}
        AND bs.period = 'Year'
        LIMIT 100"""   
    df = db.query_to_pandas(query)
    return df


# Debt and company liquidity indicators 
 # # Debt to equity ratio (Rate of change of debt to equity ratio) 
 # # Current Ratio
# Positive revenue growth over the past X years 
# Cash Flow Statements 
    ## Positive OCF over time 
    ## Periods of positive Free Cash Flow 

# Reckless management (if they don't respect equity) Common Stock issued 
 # Rising Debt but consistent D/E 
 # If number of shares outstanding is increasing 
 


# Perform comparative analysis with competitors
