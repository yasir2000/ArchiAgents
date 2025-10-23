# ArchiAgents Branding Assets Checklist

Use this checklist when implementing ArchiAgents branding in new components, pages, or features.

## 📋 Pre-Implementation Checklist

### Research Phase
- [ ] Review [BRAND_GUIDELINES.md](./BRAND_GUIDELINES.md) for complete specifications
- [ ] Check [BRANDING_QUICK_REFERENCE.md](./BRANDING_QUICK_REFERENCE.md) for quick lookups
- [ ] Review existing implementations in web app or CLI for examples
- [ ] Identify which brand elements apply to your component

## 🎨 Visual Elements Checklist

### Colors
- [ ] Use brand colors from palette (not custom colors)
  - [ ] Primary: `#0284c7` or `bg-primary-600`
  - [ ] Success: `#10b981` or `bg-emerald-500`
  - [ ] Warning: `#f59e0b` or `bg-amber-500`
  - [ ] Error: `#f43f5e` or `bg-rose-500`
  - [ ] AI/Intelligence: `#8b5cf6` or `bg-violet-500`
- [ ] Verify color contrast meets WCAG 2.1 AA (4.5:1 minimum)
- [ ] Use neutral grays for text and backgrounds
- [ ] Don't create custom color variations

### Logo Usage
- [ ] Import Logo component: `import Logo from './components/layout/Logo'`
- [ ] Use appropriate variant (primary vs icon-only)
- [ ] Set correct size (sm, md, lg)
- [ ] Include proper alt text
- [ ] Maintain minimum sizes (120px for primary, 40px for icon)
- [ ] Don't modify logo files or colors

### Typography
- [ ] Use Inter font for UI text (already configured in Tailwind)
- [ ] Use JetBrains Mono for code/technical content
- [ ] Apply correct font weights:
  - [ ] 400 (regular) for body text
  - [ ] 500 (medium) for buttons/labels
  - [ ] 600 (semibold) for subheadings
  - [ ] 700 (bold) for main headings
- [ ] Use typography scale (text-sm, text-base, text-lg, etc.)
- [ ] Don't mix font families in same context

### Icons
- [ ] Use Lucide React icons (`import { Icon } from 'lucide-react'`)
- [ ] Apply consistent sizing (16px, 20px, 24px)
- [ ] Use outlined style (primary), filled for active states
- [ ] Pair with appropriate colors
- [ ] Include descriptive aria-labels for icon-only buttons

## 🖥️ Web Component Checklist

### Buttons
- [ ] Primary button: `bg-primary-600 hover:bg-primary-700 text-white`
- [ ] Secondary button: `bg-gray-100 hover:bg-gray-200 text-gray-700`
- [ ] Destructive button: `bg-rose-500 hover:bg-rose-600 text-white`
- [ ] Use medium font weight (500)
- [ ] Apply rounded-lg (8px border radius)
- [ ] Include proper padding (px-6 py-3 for medium size)
- [ ] Add transition-colors for smooth hover effects

### Cards
- [ ] White background (`bg-white`)
- [ ] Border: `border border-gray-200`
- [ ] Rounded corners: `rounded-lg` (8px)
- [ ] Shadow: `shadow-sm`
- [ ] Padding: `p-6` (24px)

### Forms
- [ ] Input border: `border-gray-300`
- [ ] Focus state: `focus:ring-2 focus:ring-primary-500 focus:border-primary-500`
- [ ] Label: `text-gray-700 font-medium`
- [ ] Placeholder: `text-gray-400`
- [ ] Error state: `border-rose-500`

### Status/Alert Components
- [ ] Success: `bg-emerald-50 border-emerald-200 text-emerald-900`
- [ ] Warning: `bg-amber-50 border-amber-200 text-amber-900`
- [ ] Error: `bg-rose-50 border-rose-200 text-rose-900`
- [ ] Info: `bg-sky-50 border-sky-200 text-sky-900`
- [ ] Include appropriate icon (CheckCircle, AlertCircle, etc.)

### AI-Specific Components
- [ ] Use violet accent color (`bg-violet-50`, `text-violet-900`)
- [ ] Include Sparkles or Brain icon
- [ ] Badge: `bg-violet-50 border-violet-200 rounded-full`
- [ ] Highlight AI features with purple/violet gradient

## 💻 CLI Checklist

### Output Styling
- [ ] Import branding module: `from cli.branding import *`
- [ ] Use styled output functions:
  - [ ] `print_success()` for successful operations
  - [ ] `print_error()` for errors
  - [ ] `print_warning()` for warnings
  - [ ] `print_info()` for informational messages
  - [ ] `print_ai_message()` for AI-related output
  - [ ] `print_progress()` for progress updates
- [ ] Don't use plain `print()` for user-facing messages

### Welcome/Help Messages
- [ ] Use `print_welcome()` for initial greeting
- [ ] Use `print_version_info()` for version display
- [ ] Use `print_feature_highlights()` for feature lists
- [ ] Use `print_quick_start()` for command examples
- [ ] Format help text with proper indentation

### Progress Indicators
- [ ] Use Rich library for progress bars
- [ ] Show spinner for long operations
- [ ] Use brand colors (cyan/blue for primary)
- [ ] Include descriptive status messages

## 📱 Responsive Design Checklist

### Mobile (< 768px)
- [ ] Use icon-only logo variant (`Logo variant="icon-only" size="sm"`)
- [ ] Ensure touch targets are 44x44px minimum
- [ ] Stack content vertically
- [ ] Use mobile-friendly spacing
- [ ] Test on actual mobile devices

### Tablet (768px - 1024px)
- [ ] Adjust layout for medium screens
- [ ] Consider sidebar collapse/expand
- [ ] Optimize font sizes

### Desktop (> 1024px)
- [ ] Use full logo (`Logo size="md"`)
- [ ] Utilize horizontal space
- [ ] Show additional information/features

## ♿ Accessibility Checklist

### Color & Contrast
- [ ] Text has 4.5:1 contrast ratio minimum
- [ ] Large text (18px+) has 3:1 contrast minimum
- [ ] Don't rely on color alone to convey information
- [ ] Provide text labels alongside color indicators

### Semantic HTML
- [ ] Use proper heading hierarchy (h1 → h2 → h3)
- [ ] Include alt text for all images
- [ ] Use semantic elements (nav, main, section, article)
- [ ] Add ARIA labels for icon-only buttons

### Keyboard Navigation
- [ ] All interactive elements are keyboard accessible
- [ ] Visible focus indicators on all focusable elements
- [ ] Logical tab order
- [ ] Support keyboard shortcuts where appropriate

### Screen Readers
- [ ] Add aria-labels for icon-only buttons
- [ ] Use aria-describedby for additional context
- [ ] Test with screen reader (NVDA, JAWS, VoiceOver)

## 📝 Content Checklist

### Voice & Tone
- [ ] Professional and confident
- [ ] Clear and concise
- [ ] Technical but accessible
- [ ] Highlight AI/innovation where relevant
- [ ] Avoid jargon without explanation

### Messaging
- [ ] Success messages are encouraging
- [ ] Error messages are helpful and actionable
- [ ] Warning messages are clear about consequences
- [ ] Info messages provide context

### Copy Examples
- [ ] Button text is action-oriented ("Create Project", not "Submit")
- [ ] Headings are descriptive and scannable
- [ ] Descriptions are concise (2-3 sentences max)

## 🧪 Testing Checklist

### Visual Testing
- [ ] Component matches brand guidelines
- [ ] Colors are correct (use browser DevTools to verify)
- [ ] Typography is consistent
- [ ] Spacing follows design system
- [ ] Logo displays correctly at all sizes

### Functional Testing
- [ ] Hover states work correctly
- [ ] Focus states are visible
- [ ] Active states provide feedback
- [ ] Transitions are smooth
- [ ] Loading states are branded

### Cross-Browser Testing
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (if on Mac)
- [ ] Mobile browsers (iOS Safari, Chrome Mobile)

### Accessibility Testing
- [ ] Tab through all interactive elements
- [ ] Test with screen reader
- [ ] Verify color contrast with online tools
- [ ] Ensure text is readable when zoomed to 200%

## 📦 Deployment Checklist

### Assets
- [ ] Logo files are in public/assets directory
- [ ] Favicon is referenced in HTML
- [ ] Google Fonts are loaded
- [ ] All SVG files are optimized

### Configuration
- [ ] Tailwind config includes brand colors
- [ ] Font families are configured
- [ ] Custom CSS variables are defined (if used)

### Documentation
- [ ] Component usage is documented
- [ ] Brand decisions are explained
- [ ] Examples are provided

## ✅ Final Review

Before merging/deploying:
- [ ] All brand colors match guidelines
- [ ] Typography is consistent throughout
- [ ] Logo usage follows rules
- [ ] Accessibility requirements met (WCAG 2.1 AA)
- [ ] Responsive design works on all screen sizes
- [ ] Voice & tone matches brand guidelines
- [ ] No custom colors or fonts introduced
- [ ] Code reviewed by another developer
- [ ] Tested in production-like environment

## 🔗 Quick Links

- [Brand Guidelines](./BRAND_GUIDELINES.md) - Complete style guide
- [Quick Reference](./BRANDING_QUICK_REFERENCE.md) - Color palette, typography scale
- [Implementation Summary](./BRANDING_IMPLEMENTATION_SUMMARY.md) - Examples and patterns
- [Brand Assets](./brand-assets/README.md) - Logo files and usage

## 📧 Questions?

If you're unsure about any branding decision:
1. Check the brand guidelines first
2. Look for similar examples in existing code
3. Ask in team discussion/code review
4. Document your decision for future reference

---

*Last updated: October 23, 2025*
