from datetime import datetime
from pydantic import UUID4, BaseModel


class PortfolioHolding(BaseModel) : 
    ticker : str
    quantity : float
    average_price : float
    current_price : float
    initial_fill_date : datetime
    frontend : str
    ppl : float
    max_buy : float
    max_sell : float
    pie_quantity : float
    
class User(BaseModel):
    uuid : UUID4
    first_name : str
    last_name : str
    api_key : str
    