import './App.css'
import { StockCard } from './components/used_components/PortfolioCard'
import { paypalProps, vfcProps } from './data/stockData'

function App() {
  // const [count, setCount] = useState(0)
  const StockCardLists = [
    <StockCard {...paypalProps} />,
    <StockCard {...vfcProps} />,
    <StockCard {...paypalProps} />,
    <StockCard {...paypalProps} />
  ]

  return (
    <div className="flex flex-wrap gap-9">
      {StockCardLists.map((card, index) => (
        <div key={index}>{card}</div>
      ))}
    </div>
  )
}

export default App
