from litestar import Litestar
from portfolio_controller import PortfolioController

app = Litestar(route_handlers=[PortfolioController])
