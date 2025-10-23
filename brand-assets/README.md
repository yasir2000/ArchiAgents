# ArchiAgents Brand Assets

This directory contains all official branding assets for the ArchiAgents Enterprise Architecture Platform.

## 📁 Contents

### Logo Files

#### Primary Logo (`archiagents-logo-primary.svg`)
- **Usage**: Primary logo for websites, documents, presentations
- **Format**: SVG (scalable)
- **Contains**: Icon + full wordmark + tagline
- **Dimensions**: 200x60px (base size)
- **Colors**: Brand Blue (#0284c7) + Deep Blue (#0369a1) + AI Violet (#8b5cf6)

#### Icon Logo (`archiagents-logo-icon.svg`)
- **Usage**: Small spaces, social media avatars, app icons
- **Format**: SVG (scalable)
- **Contains**: Icon only with background
- **Dimensions**: 48x48px (base size)
- **Colors**: Brand Blue, Deep Blue, AI Violet on light background

#### Favicon (`favicon.svg`)
- **Usage**: Browser tabs, bookmarks, mobile home screens
- **Format**: SVG (scalable)
- **Contains**: Simplified icon optimized for 16-32px display
- **Dimensions**: 32x32px (base size)
- **Colors**: Brand Blue background with white/violet icon

## 🎨 Brand Colors

### Primary Colors
- **Brand Blue**: `#0284c7` (Primary brand color)
- **Deep Blue**: `#0369a1` (Secondary brand color)
- **AI Violet**: `#8b5cf6` (AI features indicator)

### Accent Colors
- **Success Green**: `#10b981` (Success states)
- **Warning Amber**: `#f59e0b` (Warnings)
- **Error Rose**: `#f43f5e` (Errors)

### Neutral Colors
- **Gray Scale**: `#f9fafb` to `#111827` (50-900)

## 📐 Logo Usage Guidelines

### ✓ Do's
- Use official logo files from this directory
- Maintain aspect ratio when scaling
- Ensure sufficient clear space (equal to height of "A" in ArchiAgents)
- Use on clean, uncluttered backgrounds
- Use primary logo for horizontal layouts
- Use icon logo for square/small spaces

### ✗ Don'ts
- Don't stretch or distort the logo
- Don't rotate the logo
- Don't change logo colors (except approved variants)
- Don't add drop shadows, gradients, or effects
- Don't place on busy or low-contrast backgrounds
- Don't recreate or modify the logo

## 📏 Minimum Sizes

- **Primary Logo**: 120px width minimum
- **Icon Logo**: 40px minimum
- **Favicon**: 16px minimum (use simplified version)

## 🎯 Application Examples

### Web Application
```html
<!-- Header/Navigation -->
<img src="/logo.svg" alt="ArchiAgents" class="h-10" />

<!-- Icon only (mobile) -->
<img src="/logo-icon.svg" alt="ArchiAgents" class="h-8" />

<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
```

### Documentation
```markdown
![ArchiAgents Logo](./brand-assets/archiagents-logo-primary.svg)
```

### CLI
```python
# Use ASCII art version from cli/branding.py
from cli.branding import print_welcome
print_welcome()
```

## 🖼️ File Formats

### SVG (Scalable Vector Graphics)
- **Advantages**: Scales infinitely, small file size, web-optimized
- **Usage**: Web, print, any size requirements
- **All logos provided in SVG format**

### Future Formats (to be added as needed)
- **PNG**: Raster format for specific sizes (sm/md/lg/xl)
- **ICO**: Multi-resolution favicon for broader browser support
- **PDF**: For print production

## 🚀 Getting Started

### For Web Developers
1. Copy logo files to your `public/` directory
2. Update `index.html` with favicon reference
3. Use Logo component in React: `import Logo from './components/layout/Logo'`
4. Reference brand colors from `tailwind.config.js`

### For CLI Developers
1. Import branding module: `from cli.branding import *`
2. Use branded output functions: `print_success()`, `print_error()`, etc.
3. Display welcome message: `print_welcome()`
4. Show version info: `print_version_info()`

### For Documentation Authors
1. Link to logos using relative paths
2. Follow typography guidelines from BRAND_GUIDELINES.md
3. Use brand colors in diagrams and callouts
4. Maintain consistent voice and tone

## 📚 Related Resources

- **[BRAND_GUIDELINES.md](../BRAND_GUIDELINES.md)**: Complete brand style guide
- **[Web App](../web_app/frontend/)**: Branded web application
- **[CLI](../cli/)**: Branded command-line interface
- **[Documentation](../Docs/)**: Architecture documentation

## 📞 Questions?

For branding questions, asset requests, or guidelines clarification:
- Review [BRAND_GUIDELINES.md](../BRAND_GUIDELINES.md) for detailed guidance
- Check existing usage in web app and CLI for examples
- Submit issues/PRs for brand asset improvements

## 📅 Version History

- **v1.0.0** (2025-10-23): Initial brand assets created
  - Primary logo (SVG)
  - Icon logo (SVG)
  - Favicon (SVG)
  - CLI branding module
  - Brand guidelines document

## 📄 License

These brand assets are part of the ArchiAgents project. Usage outside of ArchiAgents should maintain proper attribution and follow brand guidelines.

---

*For complete brand guidelines including typography, color usage, voice & tone, and UI components, see [BRAND_GUIDELINES.md](../BRAND_GUIDELINES.md)*
