# Open Graph Image Specifications for ArchiAgents

## Purpose
Open Graph images are displayed when ArchiAgents links are shared on social media (LinkedIn, Twitter, Facebook, etc.) and messaging apps (Slack, Teams, Discord).

## Image Specifications

### Primary OG Image
**Filename**: `og-image.png`  
**Dimensions**: 1200 x 630 pixels  
**Format**: PNG (24-bit with transparency support)  
**File Size**: < 1MB (optimize for web)  
**Aspect Ratio**: 1.91:1

### Design Layout

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Logo Icon]     Archi Agents                          │
│                  Enterprise Architecture Platform      │
│                                                         │
│                                                         │
│     ✨ AI-Powered Automation                           │
│     🏗️ TOGAF 10 ADM                                   │
│     🎯 ArchiMate 3.2                                   │
│     🌐 Visual Modeling & Collaboration                │
│                                                         │
│                                                         │
│  Transform your enterprise architecture with           │
│  intelligent automation                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Design Elements

### Background
- **Color**: Gradient from `#f0f9ff` (sky-50) to `#ede9fe` (violet-50)
- **Style**: Subtle diagonal gradient (top-left to bottom-right)
- **Texture**: Clean, professional, minimal noise

### Logo
- **Position**: Top-left (60px from edges)
- **Size**: Icon 80x80px + Wordmark
- **File**: Use `archiagents-logo-icon.svg` + text

### Primary Heading
- **Text**: "ArchiAgents"
- **Font**: Inter Bold (700)
- **Size**: 72px
- **Color**: `#0284c7` (Brand Blue)
- **Position**: Below logo, left-aligned

### Subheading
- **Text**: "Enterprise Architecture Platform"
- **Font**: Inter Medium (500)
- **Size**: 32px
- **Color**: `#6b7280` (Gray-600)
- **Position**: Below heading

### Feature List
- **Font**: Inter Medium (500)
- **Size**: 28px
- **Color**: `#374151` (Gray-700)
- **Spacing**: 24px between items
- **Icons**: Emoji or unicode symbols (✨🏗️🎯🌐)

### Tagline
- **Text**: "Transform your enterprise architecture with intelligent automation"
- **Font**: Inter Regular (400)
- **Size**: 24px
- **Color**: `#4b5563` (Gray-600)
- **Position**: Bottom third, centered
- **Max Width**: 1000px

## Alternative Variations

### Twitter Card (Smaller)
**Dimensions**: 1200 x 675 pixels  
**Filename**: `twitter-card.png`  
**Layout**: Similar but more compact (larger text, less spacing)

### LinkedIn Share
**Dimensions**: 1200 x 627 pixels  
**Filename**: `linkedin-share.png`  
**Layout**: Same as primary OG image (very similar aspect ratio)

### GitHub Social Preview
**Dimensions**: 1280 x 640 pixels  
**Filename**: `github-social.png`  
**Layout**: Same design, slightly different aspect ratio

## HTML Implementation

```html
<!-- In index.html -->
<meta property="og:type" content="website" />
<meta property="og:title" content="ArchiAgents - Enterprise Architecture Platform" />
<meta property="og:description" content="Transform your enterprise architecture with AI-powered automation. TOGAF 10 ADM, ArchiMate 3.2 compliance." />
<meta property="og:image" content="https://archiagents.com/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:url" content="https://archiagents.com" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="ArchiAgents - Enterprise Architecture Platform" />
<meta name="twitter:description" content="Transform your enterprise architecture with AI-powered automation." />
<meta name="twitter:image" content="https://archiagents.com/twitter-card.png" />
```

## Design Tools

### Recommended Tools for Creation
1. **Figma** (preferred) - Web-based, collaborative
2. **Canva** - Quick template-based design
3. **Adobe Photoshop** - Professional raster editing
4. **Sketch** - Mac-based design tool

### Template Structure (Figma/Sketch)
```
Artboard: 1200x630px
├── Background Layer (gradient)
├── Logo Group
│   ├── Icon (80x80px)
│   └── Wordmark text
├── Content Group
│   ├── Heading
│   ├── Subheading
│   ├── Feature List
│   └── Tagline
└── Branding Elements
    └── Footer badge (optional)
```

## Export Settings

### PNG Export
- **Resolution**: 72 DPI (web standard)
- **Color Space**: sRGB
- **Compression**: Medium (balance quality/size)
- **Transparency**: No (use solid background)

### Optimization
```bash
# Using ImageOptim (Mac) or similar
- Remove metadata
- Compress PNG (lossless)
- Target: < 500KB ideally
```

## Testing

### Preview Tools
1. **Facebook Debugger**: https://developers.facebook.com/tools/debug/
2. **Twitter Card Validator**: https://cards-dev.twitter.com/validator
3. **LinkedIn Post Inspector**: https://www.linkedin.com/post-inspector/
4. **Slack Link Previews**: Paste URL in Slack channel

### Checklist
- [ ] Image displays correctly on Facebook
- [ ] Image displays correctly on Twitter
- [ ] Image displays correctly on LinkedIn
- [ ] Image displays correctly in Slack
- [ ] Text is readable at thumbnail size
- [ ] Logo is clear and recognizable
- [ ] Colors match brand guidelines
- [ ] File size is optimized (< 1MB)

## Content Variations

### For Different Pages
Create variations with different messaging:

**Homepage OG Image**:
- Tagline: "Transform your enterprise architecture with AI-powered automation"

**Documentation OG Image**:
- Tagline: "Complete TOGAF 10 & ArchiMate 3.2 implementation guides"

**Web App OG Image**:
- Tagline: "Visual modeling platform with real-time collaboration"

**GitHub Repository OG Image**:
- Tagline: "Open-source enterprise architecture framework"

## Placement

### File Locations
```
web_app/frontend/public/
├── og-image.png         # Primary OG image (1200x630)
├── twitter-card.png     # Twitter optimized (1200x675)
├── linkedin-share.png   # LinkedIn optimized (1200x627)
└── github-social.png    # GitHub optimized (1280x640)
```

### CDN Recommendations
- Host on same domain as website for best performance
- Use absolute URLs in meta tags
- Consider CDN (Cloudflare, AWS CloudFront) for faster loading
- Add cache headers (long-lived, 1 year+)

## Version History

- **v1.0.0** (Pending): Initial OG image specifications
  - Layout design defined
  - Dimensions and formats specified
  - HTML implementation documented
  - Export settings established

## Future Enhancements

- [ ] Animated GIF version for platforms that support it
- [ ] Video OG tags for Twitter/Facebook video previews
- [ ] Dark mode variant for dark-themed platforms
- [ ] Localized versions (Arabic for MENA markets)
- [ ] A/B tested variations for better engagement

---

## Quick Reference

| Platform | Dimensions | Format | Notes |
|----------|------------|--------|-------|
| Facebook | 1200 x 630 | PNG | Primary OG image |
| Twitter | 1200 x 675 | PNG | Slightly taller |
| LinkedIn | 1200 x 627 | PNG | Similar to Facebook |
| GitHub | 1280 x 640 | PNG | Repository social preview |
| WhatsApp | 1200 x 630 | PNG | Uses OG image |
| Slack | 1200 x 630 | PNG | Uses OG image |
| Discord | 1200 x 630 | PNG | Uses OG image |

**Recommended**: Create primary 1200x630 image first, then adapt for platform-specific sizes if needed.

---

*These specifications follow the brand guidelines in [BRAND_GUIDELINES.md](./BRAND_GUIDELINES.md)*
