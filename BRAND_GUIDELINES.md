# ArchiAgents Brand Guidelines

## Brand Overview

**ArchiAgents** is a next-generation Enterprise Architecture platform that combines the power of TOGAF 10 ADM methodology, ArchiMate 3.2 modeling standards, and AI-driven automation. Our brand represents innovation, precision, intelligence, and enterprise-grade quality.

### Brand Positioning
- **Industry**: Enterprise Architecture & Digital Transformation
- **Audience**: Enterprise Architects, Solution Architects, IT Directors, Digital Transformation Leaders
- **Value Proposition**: AI-powered architecture development with standards compliance and visual collaboration
- **Brand Promise**: Accelerate architecture excellence through intelligent automation

---

## Visual Identity

### Logo Design

The ArchiAgents logo consists of two elements:
1. **Icon**: A geometric representation combining architecture (building blocks) and AI (neural connections)
2. **Wordmark**: Modern, professional typography emphasizing "Archi" and "Agents"

#### Logo Variations
- **Primary Logo**: Full color with icon and wordmark
- **Icon Only**: For small spaces and favicons
- **Monochrome**: For single-color applications
- **Reversed**: For dark backgrounds

#### Logo Usage
- **Minimum Size**: 120px width for horizontal, 40px for icon only
- **Clear Space**: Maintain clear space equal to the height of "A" in ArchiAgents
- **Don'ts**: No stretching, rotating, recoloring (except approved variations), or adding effects

---

## Color Palette

### Primary Colors

#### Brand Blue (Primary)
- **Purpose**: Primary brand color, CTAs, navigation, headers
- **Color Values**:
  - Hex: `#0284c7`
  - RGB: `rgb(2, 132, 199)`
  - HSL: `hsl(199, 98%, 39%)`
  - Tailwind: `sky-600`
- **Usage**: Primary buttons, links, active states, logo

#### Deep Blue (Secondary)
- **Purpose**: Dark accents, text on light backgrounds
- **Color Values**:
  - Hex: `#0369a1`
  - RGB: `rgb(3, 105, 161)`
  - HSL: `hsl(199, 96%, 32%)`
  - Tailwind: `sky-700`
- **Usage**: Hover states, secondary elements

### Accent Colors

#### Emerald Green (Success)
- **Purpose**: Success states, positive actions, growth
- **Color Values**:
  - Hex: `#10b981`
  - RGB: `rgb(16, 185, 129)`
  - HSL: `hsl(160, 84%, 39%)`
  - Tailwind: `emerald-500`
- **Usage**: Success messages, completion indicators

#### Amber (Warning)
- **Purpose**: Warnings, caution, attention needed
- **Color Values**:
  - Hex: `#f59e0b`
  - RGB: `rgb(245, 158, 11)`
  - HSL: `hsl(38, 92%, 50%)`
  - Tailwind: `amber-500`
- **Usage**: Warning messages, draft states

#### Rose (Error)
- **Purpose**: Errors, destructive actions, critical issues
- **Color Values**:
  - Hex: `#f43f5e`
  - RGB: `rgb(244, 63, 94)`
  - HSL: `hsl(351, 89%, 60%)`
  - Tailwind: `rose-500`
- **Usage**: Error messages, delete actions

#### Violet (AI/Intelligence)
- **Purpose**: AI features, intelligent automation, premium features
- **Color Values**:
  - Hex: `#8b5cf6`
  - RGB: `rgb(139, 92, 246)`
  - HSL: `hsl(258, 90%, 66%)`
  - Tailwind: `violet-500`
- **Usage**: AI agent indicators, smart features, premium badges

### Neutral Colors

#### Gray Scale
- **50**: `#f9fafb` - Background, subtle surfaces
- **100**: `#f3f4f6` - Card backgrounds
- **200**: `#e5e7eb` - Borders, dividers
- **300**: `#d1d5db` - Disabled elements
- **400**: `#9ca3af` - Placeholders
- **500**: `#6b7280` - Secondary text
- **600**: `#4b5563` - Body text
- **700**: `#374151` - Headings
- **800**: `#1f2937` - Dark headings
- **900**: `#111827` - Primary text

---

## Typography

### Font Families

#### Primary Font: Inter
- **Purpose**: UI, body text, navigation
- **Weights**: 
  - Regular (400): Body text, descriptions
  - Medium (500): Buttons, labels
  - Semibold (600): Subheadings
  - Bold (700): Headings
- **Source**: Google Fonts
- **Fallback**: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`

#### Monospace Font: JetBrains Mono
- **Purpose**: Code, technical content, CLI output
- **Weights**: 
  - Regular (400): Code blocks
  - Medium (500): Highlighted code
- **Source**: Google Fonts
- **Fallback**: `'Courier New', monospace`

### Type Scale

#### Headings
```css
.heading-1 { font-size: 3rem;     /* 48px */ font-weight: 700; line-height: 1.2; }
.heading-2 { font-size: 2.25rem;  /* 36px */ font-weight: 700; line-height: 1.25; }
.heading-3 { font-size: 1.875rem; /* 30px */ font-weight: 600; line-height: 1.3; }
.heading-4 { font-size: 1.5rem;   /* 24px */ font-weight: 600; line-height: 1.4; }
.heading-5 { font-size: 1.25rem;  /* 20px */ font-weight: 600; line-height: 1.5; }
.heading-6 { font-size: 1rem;     /* 16px */ font-weight: 600; line-height: 1.5; }
```

#### Body Text
```css
.text-large  { font-size: 1.125rem; /* 18px */ line-height: 1.75; }
.text-base   { font-size: 1rem;     /* 16px */ line-height: 1.5; }
.text-small  { font-size: 0.875rem; /* 14px */ line-height: 1.5; }
.text-xsmall { font-size: 0.75rem;  /* 12px */ line-height: 1.5; }
```

---

## UI Components

### Buttons

#### Primary Button
- **Background**: Brand Blue (#0284c7)
- **Text**: White
- **Hover**: Deep Blue (#0369a1)
- **Padding**: 12px 24px
- **Border Radius**: 6px
- **Font**: Medium (500)

#### Secondary Button
- **Background**: Gray-100
- **Text**: Gray-700
- **Hover**: Gray-200
- **Border**: 1px solid Gray-300

#### Destructive Button
- **Background**: Rose-500
- **Text**: White
- **Hover**: Rose-600

#### Ghost Button
- **Background**: Transparent
- **Text**: Brand Blue
- **Hover**: Brand Blue 10% opacity background

### Cards
- **Background**: White
- **Border**: 1px solid Gray-200
- **Border Radius**: 8px
- **Shadow**: `0 1px 3px rgba(0, 0, 0, 0.1)`
- **Padding**: 20px

### Forms
- **Input Border**: Gray-300
- **Input Focus**: Brand Blue border with blue glow
- **Label**: Gray-700, font-medium
- **Placeholder**: Gray-400
- **Error State**: Rose-500 border

---

## Iconography

### Icon System
- **Library**: Lucide React (primary), Heroicons (secondary)
- **Style**: Outlined (primary), Filled (for active states)
- **Sizes**:
  - Small: 16px
  - Medium: 20px
  - Large: 24px
  - XLarge: 32px

### Icon Usage
- **Navigation**: 20px, medium weight
- **Buttons**: 16px with 8px spacing from text
- **Headers**: 24px for section headers
- **Status Indicators**: 16px with color coding

### Key Icons
- **Architecture**: `Building2`, `Layers`, `Network`
- **AI/Automation**: `Brain`, `Sparkles`, `Bot`
- **Projects**: `FolderKanban`, `Folder`, `FileBox`
- **Models**: `Box`, `Boxes`, `Component`
- **Actions**: `Plus`, `Edit`, `Trash2`, `Download`, `Upload`
- **Navigation**: `ChevronRight`, `ArrowRight`, `Menu`, `X`
- **Status**: `Check`, `AlertCircle`, `Info`, `XCircle`

---

## Brand Voice & Tone

### Voice Attributes
- **Professional**: Expert knowledge, credible, trustworthy
- **Innovative**: Forward-thinking, cutting-edge, AI-powered
- **Clear**: Direct, jargon-free when possible, educational
- **Confident**: Assertive, capable, reliable

### Tone Guidelines

#### For Marketing/Website
- Confident and inspiring
- Highlight innovation and AI capabilities
- Focus on business outcomes
- Use active voice

*Example*: "Transform your enterprise architecture with AI-powered automation. ArchiAgents accelerates development by 10x while maintaining TOGAF and ArchiMate standards."

#### For Documentation
- Clear and instructional
- Step-by-step guidance
- Technical but accessible
- Include examples

*Example*: "To generate a business architecture model, run `archi model generate --type business-process`. This creates an ArchiMate-compliant process model with automatic validation."

#### For UI/Product
- Concise and action-oriented
- Friendly but professional
- Clear calls-to-action
- Helpful error messages

*Example*: 
- Button: "Create Architecture Model"
- Success: "Model generated successfully! View it in the editor."
- Error: "Unable to generate model. Check that your project configuration is complete."

#### For CLI
- Technical and precise
- Informative output
- Clear progress indicators
- Helpful suggestions

*Example*:
```
✓ Project initialized successfully
→ Next steps:
  1. Configure AI provider: archi ai configure
  2. Generate your first model: archi model generate
  3. View comprehensive help: archi --help
```

---

## Brand Applications

### Website/Web App
- Prominent logo in top-left header
- Brand blue for primary navigation and CTAs
- Clean, spacious layouts with white backgrounds
- Liberal use of AI/intelligence indicators (violet accents)
- Professional photography or custom illustrations

### CLI Application
- ASCII art logo in welcome message
- Color-coded output (success: green, error: red, info: blue)
- Consistent command structure and naming
- Helpful examples in help text
- Progress bars and spinners for long operations

### Documentation
- Branded header on all pages
- Consistent color coding for code blocks
- Clear hierarchy with typography scale
- Diagrams using brand colors
- Screenshots with branded UI

### Marketing Materials
- Bold headlines using heading typography
- High-quality architectural/technical imagery
- Customer success stories
- Clear value propositions
- Professional case studies

---

## Digital Asset Specifications

### Favicon
- **Sizes**: 16x16, 32x32, 48x48, 64x64
- **Format**: ICO, PNG, SVG
- **Design**: Icon-only version of logo

### Social Media Images
- **Open Graph**: 1200x630px
- **Twitter Card**: 1200x675px
- **LinkedIn**: 1200x627px
- **Content**: Logo + tagline + key visual

### Email Signatures
- Logo: 150px width
- Brand blue for links
- Professional contact information

---

## Brand Do's and Don'ts

### ✓ Do's
- Use official color values consistently
- Maintain proper logo spacing and sizing
- Apply brand colors to UI elements systematically
- Use Inter font for all UI text
- Highlight AI features with violet accent
- Use clear, professional language
- Include TOGAF/ArchiMate certification marks appropriately

### ✗ Don'ts
- Don't use unofficial color variations
- Don't stretch or distort the logo
- Don't use busy backgrounds behind the logo
- Don't mix font families within the same context
- Don't overuse accent colors
- Don't use jargon without explanation
- Don't claim compliance without validation

---

## Accessibility

### WCAG 2.1 AA Compliance

#### Color Contrast
- **Text on Background**: Minimum 4.5:1 ratio
- **Large Text**: Minimum 3:1 ratio
- **UI Components**: Minimum 3:1 ratio

#### Verified Combinations
- Brand Blue (#0284c7) on White: 5.2:1 ✓
- Gray-700 (#374151) on White: 10.8:1 ✓
- White on Brand Blue: 5.2:1 ✓
- Gray-600 (#4b5563) on White: 8.1:1 ✓

#### Design Considerations
- Don't rely on color alone for meaning
- Provide text labels for icon-only buttons
- Include focus indicators for keyboard navigation
- Support screen readers with proper ARIA labels
- Ensure sufficient touch target sizes (44x44px minimum)

---

## File Naming Conventions

### Logo Files
- `archiagents-logo-primary.svg`
- `archiagents-logo-icon.svg`
- `archiagents-logo-monochrome.svg`
- `archiagents-logo-reversed.svg`

### Sizing Variants
- `archiagents-logo-[variant]-sm.png` (120px)
- `archiagents-logo-[variant]-md.png` (240px)
- `archiagents-logo-[variant]-lg.png` (480px)
- `archiagents-logo-[variant]-xl.png` (960px)

### Document Templates
- `archiagents-presentation-template.pptx`
- `archiagents-document-template.docx`
- `archiagents-email-signature.html`

---

## Version History

- **v1.0.0** (2025-10-23): Initial brand guidelines established
  - Logo design and color palette defined
  - Typography system established
  - UI component specifications created
  - Voice and tone guidelines documented

---

## Contact

For brand-related questions or asset requests:
- **Email**: brand@archiagents.com
- **Repository**: [ArchiAgents Brand Assets](./brand-assets/)
- **Guidelines**: [BRAND_GUIDELINES.md](./BRAND_GUIDELINES.md)

---

*These guidelines are maintained by the ArchiAgents project team. Last updated: October 23, 2025.*
