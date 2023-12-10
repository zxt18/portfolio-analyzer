from litestar import Controller, get
from typing import List
from dto import PortfolioHolding
from constants import TRADING212_URL, TRADINGD212_HEADERS
import cachetools.func 
import requests

@cachetools.func.ttl_cache(maxsize=10, ttl=10 * 60)
def _get_portfolio() -> List[PortfolioHolding] :
    response= requests.get(TRADING212_URL, headers=TRADINGD212_HEADERS)
    portfolio_holdings = response.json()
    return portfolio_holdings
    

class PortfolioController(Controller):
    path="/portfolio"
    @get()
    async def get_portfolio(self) -> List[PortfolioHolding]: 
        return _get_portfolio()