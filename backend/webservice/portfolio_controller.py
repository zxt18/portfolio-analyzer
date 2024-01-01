from litestar import Controller, get
from typing import List
from backend.utils import TimedCache
from dto import PortfolioHoldingDTO
from constants import TRADING212_URL, TRADINGD212_HEADERS
import requests

# For a specific user, retrieve it from the database.
# Key is uuid, Value is Portfolio Object              
portfolio_cache = TimedCache(expiry_seconds=60)

# @cachetools.func.ttl_cache(maxsize=10, ttl=10 * 60)
def _get_portfolio(user_id) -> List[PortfolioHoldingDTO] :
    if portfolio_cache[user_id]: 
        portfolio_holdings = portfolio_cache[user_id]
    else : 
        response= requests.get(TRADING212_URL, headers=TRADINGD212_HEADERS)
        portfolio_holdings = response.json()
        portfolio_cache[user_id] = portfolio_holdings
    return portfolio_holdings
    

class PortfolioController(Controller):
    path="/portfolio"
    @get()
    async def get_portfolio(self, user_id: int = 0) -> List[PortfolioHoldingDTO]: 
        return _get_portfolio(user_id)
    
    @get("tickers")
    async def get_tickers(self, user_id: int = 0) -> List[str]:
        portfolio = _get_portfolio(user_id)
        tickers = [ticker_obj["ticker"] for ticker_obj in portfolio]
        return tickers