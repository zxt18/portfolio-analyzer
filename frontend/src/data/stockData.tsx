import { StockCardProps } from '@/components/used_components/PortfolioCard'
import VFCLogo from '../assets/vfc_logo.png'
export const paypalProps: StockCardProps = {
  logoSrc: 'https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-200px.png',
  altText: 'PayPal Logo',
  subtitlesAndDescription: [
    {
      subTitle: 'Resilient through operating cycles',
      description: 'Operated for 25 years'
    },
    {
      subTitle: 'Management Quality',
      description: '2 hours ago'
    },
    {
      subTitle: 'Free Cash Flow',
      description: '2 hours ago'
    },
    {
      subTitle: 'Margin of Safety',
      description: '2 hours ago'
    }
  ]
}

export const vfcProps: StockCardProps = {
  logoSrc: VFCLogo,
  altText: 'VFC Logo',
  subtitlesAndDescription: [
    {
      subTitle: 'Hello',
      description: 'World'
    },
    {
      subTitle: 'Hello',
      description: 'World'
    },
    {
      subTitle: 'Hello',
      description: 'World'
    },
    {
      subTitle: 'Hello',
      description: 'World'
    }
  ]
}
