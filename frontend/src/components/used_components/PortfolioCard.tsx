import { BellRing, Check } from 'lucide-react'
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardFooter, CardHeader } from '@/components/ui/card'
import { CompanyLogo } from './CompanyLogo'

export interface StockCardProps {
  logoSrc: string
  altText: string
  subtitlesAndDescription: { subTitle: string; description: string }[]
}

type CardProps = React.ComponentProps<typeof Card>

export function StockCard({ className, ...props }: CardProps & StockCardProps) {
  return (
    <Card className={cn('w-[380px]', className)} {...props}>
      <CardHeader>
        <CompanyLogo logoSrc={props.logoSrc} altText={props.altText} />
        <CardDescription>Online payment solutions for individuals and businesses</CardDescription>
      </CardHeader>
      <CardContent className="grid gap-4">
        <div>
          {props.subtitlesAndDescription.map((notification, index) => (
            <div
              key={index}
              className="mb-4 grid grid-cols-[25px_1fr] items-start pb-4 last:mb-0 last:pb-0"
            >
              <span className="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500" />
              <div className="space-y-1">
                <p className=" text-sm font-medium leading-none">{notification.subTitle}</p>
                <p className="text-sm text-muted-foreground">{notification.description}</p>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
      <CardFooter>
        <Button className="w-full">
          <Check className="mr-2 h-4 w-4" /> Mark all as read
        </Button>
      </CardFooter>
    </Card>
  )
}

// <div className=" flex items-center space-x-4 rounded-md border p-4">
// <BellRing />
// <div className="flex-1 space-y-1">
//   <p className="text-sm font-medium leading-none">Push Notifications</p>
//   <p className="text-sm text-muted-foreground">Send notifications to device.</p>
// </div>
// <Switch />
// </div>
