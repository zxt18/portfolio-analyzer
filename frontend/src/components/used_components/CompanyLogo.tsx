interface CompanyLogoProps {
  logoSrc: string
  altText: string
}
export const CompanyLogo = ({ logoSrc, altText }: CompanyLogoProps) => {
  return (
    <div className="self-center">
      <img src={logoSrc} alt={altText} className=" h-11 w-auto" />
    </div>
  )
}
