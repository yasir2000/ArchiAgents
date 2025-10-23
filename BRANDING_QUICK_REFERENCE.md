# ArchiAgents Branding Quick Reference

## 🎨 Color Palette

### Primary Colors
```
#0284c7  Brand Blue      Use for: CTAs, navigation, primary brand
#0369a1  Deep Blue       Use for: Hover states, secondary elements
#8b5cf6  AI Violet       Use for: AI features, intelligent automation
```

### Accent Colors
```
#10b981  Success Green   ✓ Success messages, completions
#f59e0b  Warning Amber   ⚠ Warnings, drafts, caution
#f43f5e  Error Rose      ✗ Errors, destructive actions
```

### Grays
```
#f9fafb  Gray-50        Background
#4b5563  Gray-600       Body text
#374151  Gray-700       Headings
```

## 📝 Typography

### Fonts
- **UI/Body**: Inter (400, 500, 600, 700)
- **Code**: JetBrains Mono (400, 500)
- **CDN**: `fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500`

### Scale
```
.text-4xl { 36px, bold }  # Page titles
.text-3xl { 30px, bold }  # Section headers
.text-2xl { 24px, semibold }  # Subsections
.text-xl  { 20px, semibold }  # Card titles
.text-lg  { 18px }  # Large body
.text-base { 16px }  # Body text
.text-sm  { 14px }  # Small text
```

## 🖼️ Logo Usage

### Web App
```tsx
import Logo from './components/layout/Logo'

<Logo size="md" />                    // Full logo
<Logo variant="icon-only" size="sm" /> // Icon only
```

### HTML
```html
<link rel="icon" href="/favicon.svg" />
<img src="/logo.svg" alt="ArchiAgents" class="h-10" />
```

### CLI
```python
from cli.branding import print_welcome
print_welcome()
```

## 🎯 Common Components

### Primary Button
```tsx
<button className="bg-primary-600 hover:bg-primary-700 text-white font-medium px-6 py-3 rounded-lg">
  Create Project
</button>
```

### Success Message
```tsx
<div className="bg-emerald-50 border border-emerald-200 text-emerald-900 p-4 rounded-lg">
  ✓ Success message
</div>
```

### AI Badge
```tsx
<div className="bg-violet-50 border border-violet-200 text-violet-900 px-3 py-1 rounded-full inline-flex items-center">
  <Sparkles className="h-4 w-4 mr-1" />
  AI-Powered
</div>
```

## 📐 Spacing

### Padding/Margin
```
px-2  8px    sm  4  16px   lg  6  24px   2xl
py-1  4px    md  5  20px   xl  8  32px   3xl
```

### Border Radius
```
rounded-sm   2px   Card corners
rounded-md   6px   Buttons, inputs
rounded-lg   8px   Modals, panels
rounded-xl   12px  Featured cards
rounded-2xl  16px  Large containers
```

## 🎨 Gradients

### Background Gradients
```css
/* Auth pages */
bg-gradient-to-br from-sky-50 via-blue-50 to-violet-50

/* Headers */
bg-gradient-to-r from-primary-600 to-primary-700

/* AI features */
bg-gradient-to-r from-violet-50 to-purple-50
```

## 💬 Voice & Tone

### Marketing
**Bold, inspiring, AI-focused**  
"Transform your enterprise architecture with AI-powered automation"

### Documentation
**Clear, instructional, helpful**  
"To generate a model, run `archi model generate --type business-process`"

### UI Messages
**Concise, friendly, actionable**  
Success: "Model generated successfully! View in editor."  
Error: "Unable to save. Check your connection and try again."

## 🔤 Copy Examples

### Feature Highlights
- ✨ AI-Powered Automation
- 🏗️ TOGAF 10 ADM
- 🎯 ArchiMate 3.2
- 🌐 Visual Modeling
- 🇸🇦 NORA Compliance

### Taglines
- "Enterprise Architecture Platform"
- "AI-Powered • TOGAF 10 • ArchiMate 3.2"
- "Transform architecture with intelligent automation"

## 📏 Logo Specs

### Minimum Sizes
- Primary logo: 120px width
- Icon logo: 40px
- Favicon: 16px

### Clear Space
Equal to height of "A" in ArchiAgents

### Files
- `logo.svg` - Full logo with wordmark
- `logo-icon.svg` - Icon only
- `favicon.svg` - Browser favicon

## 🎯 Quick Copy-Paste

### Tailwind Classes
```tsx
// Primary button
className="bg-primary-600 hover:bg-primary-700 text-white font-medium px-6 py-3 rounded-lg shadow-sm transition-colors"

// Card
className="bg-white border border-gray-200 rounded-lg shadow-sm p-6"

// Input
className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"

// Badge
className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-violet-100 text-violet-800"
```

### CLI Output
```python
from cli.branding import print_success, print_error, print_info, print_ai_message

print_success("Operation completed")
print_error("Failed to connect")
print_info("Processing architecture model")
print_ai_message("AI agent analyzing requirements")
```

## 📚 Documentation

- **Full Guidelines**: `BRAND_GUIDELINES.md`
- **Implementation**: `BRANDING_IMPLEMENTATION_SUMMARY.md`
- **Assets**: `brand-assets/README.md`

## ✅ Checklist

When creating new content:
- [ ] Use brand colors from palette
- [ ] Apply Inter font family
- [ ] Include Logo component
- [ ] Follow typography scale
- [ ] Maintain proper spacing
- [ ] Use branded icons (Lucide)
- [ ] Test accessibility (contrast)
- [ ] Match voice & tone

---

*Quick access to [Full Brand Guidelines →](./BRAND_GUIDELINES.md)*
