from datetime import datetime
from pydantic import UUID4, BaseModel


class PortfolioHoldingDTO(BaseModel) : 
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
    
class UserDTO(BaseModel):
    uuid : UUID4
    first_name : str
    last_name : str
    api_key : str
    