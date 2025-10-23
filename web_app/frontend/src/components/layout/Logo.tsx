import { Link } from 'react-router-dom'

interface LogoProps {
  variant?: 'primary' | 'icon-only'
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

export default function Logo({ variant = 'primary', size = 'md', className = '' }: LogoProps) {
  const sizeClasses = {
    sm: 'h-8',
    md: 'h-10',
    lg: 'h-12'
  }

  if (variant === 'icon-only') {
    return (
      <Link to="/" className={`flex items-center ${className}`}>
        <img 
          src="/logo-icon.svg" 
          alt="ArchiAgents" 
          className={`${sizeClasses[size]} w-auto`}
        />
      </Link>
    )
  }

  return (
    <Link to="/" className={`flex items-center ${className}`}>
      <div className="flex items-center space-x-2">
        <img 
          src="/logo-icon.svg" 
          alt="ArchiAgents" 
          className={`${sizeClasses[size]} w-auto`}
        />
        <div className="flex flex-col">
          <div className="flex items-baseline space-x-0.5">
            <span className={`font-bold text-primary-600 ${
              size === 'sm' ? 'text-lg' : size === 'lg' ? 'text-3xl' : 'text-xl'
            }`}>
              Archi
            </span>
            <span className={`font-bold text-primary-700 ${
              size === 'sm' ? 'text-lg' : size === 'lg' ? 'text-3xl' : 'text-xl'
            }`}>
              Agents
            </span>
          </div>
          {size !== 'sm' && (
            <span className="text-xs text-gray-500 tracking-wider uppercase font-medium -mt-1">
              Enterprise Architecture
            </span>
          )}
        </div>
      </div>
    </Link>
  )
}
