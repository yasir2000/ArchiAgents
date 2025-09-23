#!/usr/bin/env python3
"""
TOGAF 9 Templates Navigation Index Generator

This script creates a comprehensive navigation index for all converted markdown files
in the TOGAF 9 Templates directory, organized by category and phase.
"""

import os
from pathlib import Path
from typing import Dict, List

def create_navigation_index():
    """Create a comprehensive navigation index for converted templates"""
    
    # Base directory
    base_dir = Path(r"C:\Users\yasir\Code\enterprise-architecture-project\Templates\Togaf9 Templates")
    
    # Find all markdown files
    md_files = list(base_dir.rglob("*.md"))
    
    # Organize files by category
    categories = {
        "Phase A - Architecture Vision": [],
        "Phase B - Business Architecture": [],
        "Phase C - Information Systems": [],
        "Phase D - Technology Architecture": [],
        "Phase E - Opportunities and Solutions": [],
        "Phase F - Migration Planning": [],
        "Phase G - Implementation Governance": [],
        "Phase H - Architecture Change Management": [],
        "Preliminary Phase": [],
        "Artifacts - Catalogs": [],
        "Artifacts - Matrices": [],
        "Artifacts - Diagrams": [],
        "MS Word Templates": [],
        "Other": []
    }
    
    # Categorize files
    for md_file in md_files:
        relative_path = md_file.relative_to(base_dir)
        path_str = str(relative_path)
        
        if "CONVERSION_REPORT.md" in path_str:
            continue  # Skip the conversion report
            
        if "Phase A" in path_str:
            categories["Phase A - Architecture Vision"].append(relative_path)
        elif "Phase B" in path_str:
            categories["Phase B - Business Architecture"].append(relative_path)
        elif "Phase C" in path_str:
            categories["Phase C - Information Systems"].append(relative_path)
        elif "Phase D" in path_str:
            categories["Phase D - Technology Architecture"].append(relative_path)
        elif "Phase E" in path_str:
            categories["Phase E - Opportunities and Solutions"].append(relative_path)
        elif "Phase F" in path_str:
            categories["Phase F - Migration Planning"].append(relative_path)
        elif "Phase G" in path_str:
            categories["Phase G - Implementation Governance"].append(relative_path)
        elif "Phase H" in path_str:
            categories["Phase H - Architecture Change Management"].append(relative_path)
        elif "_Preliminary Phase" in path_str:
            categories["Preliminary Phase"].append(relative_path)
        elif "Catalogs" in path_str:
            categories["Artifacts - Catalogs"].append(relative_path)
        elif "Matrices" in path_str:
            categories["Artifacts - Matrices"].append(relative_path)
        elif "Diagrams" in path_str or "Extension Diagrams" in path_str or "Core Diagrams" in path_str:
            categories["Artifacts - Diagrams"].append(relative_path)
        elif "MS Word Templates" in path_str:
            categories["MS Word Templates"].append(relative_path)
        else:
            categories["Other"].append(relative_path)
    
    # Generate navigation index
    navigation_content = f"""# TOGAF 9 Templates - Professional Markdown Collection

## Overview
This directory contains professionally converted TOGAF 9 templates in markdown format, supporting the Enterprise Architecture project's implementation of TOGAF 10 ADM methodology with ArchiMate 3.2 modeling standards and Saudi NORA compliance.

## Conversion Summary
- **Total Files Converted:** {len(md_files) - 1}  <!-- Excluding conversion report -->
- **Conversion Date:** {import_date}
- **Format:** Professional Markdown with GitHub-flavored tables
- **Integration:** TOGAF 10 ADM + ArchiMate 3.2 + Saudi NORA compliance

## Template Categories

"""
    
    # Add each category
    for category, files in categories.items():
        if not files:
            continue
            
        navigation_content += f"### {category}\n\n"
        
        # Sort files alphabetically
        files.sort()
        
        for file_path in files:
            # Get the file title (remove .md extension and format)
            title = file_path.stem
            if title.startswith("TOGAF 9 Template - "):
                title = title[20:]  # Remove prefix
            title = title.replace("_", " ").replace("-", " ")
            
            # Create relative link
            link_path = str(file_path).replace("\\", "/")
            navigation_content += f"- [{title}]({link_path})\n"
        
        navigation_content += "\n"
    
    # Add footer
    navigation_content += f"""## Enterprise Architecture Integration

### TOGAF 10 ADM Alignment
These templates support the eight-phase TOGAF Architecture Development Method:
- **Preliminary Phase:** Architecture capability and governance
- **Phase A:** Architecture Vision and stakeholder alignment
- **Phase B:** Business Architecture optimization
- **Phase C:** Information Systems Architecture
- **Phase D:** Technology Architecture and cloud strategy
- **Phase E:** Opportunities and Solutions assessment
- **Phase F:** Migration Planning and roadmaps
- **Phase G:** Implementation Governance and oversight
- **Phase H:** Architecture Change Management

### ArchiMate 3.2 Integration
Templates align with ArchiMate architectural layers:
- **Strategy Layer:** Goals, capabilities, value streams
- **Business Layer:** Processes, functions, services
- **Application Layer:** Microservices, APIs, data flows  
- **Technology Layer:** Cloud infrastructure, security, DevOps
- **Physical Layer:** Data centers, network, IoT
- **Implementation Layer:** Migration and transformation

### Saudi NORA Compliance
Templates include considerations for:
- **Vision 2030 Alignment:** Digital government transformation targets
- **Data Sovereignty:** Saudi PDPL compliance and localization
- **Arabic-First Design:** RTL interfaces and cultural considerations
- **Government Integration:** Absher, NSSO, and DGA standards
- **Cybersecurity:** NCA framework and ECC implementation

## Usage Guidelines

### Template Selection
1. **Phase-Based Selection:** Choose templates based on current ADM phase
2. **Artifact Type:** Select catalogs, matrices, or diagrams as needed
3. **Integration Points:** Reference cross-cutting concerns and governance

### Customization Process
1. **Content Review:** Examine template structure and requirements
2. **Enterprise Context:** Adapt to specific organizational needs
3. **Compliance Mapping:** Ensure NORA and governance alignment
4. **ArchiMate Integration:** Link to architectural models and views

### Quality Assurance
- Follow enterprise documentation standards
- Maintain traceability to architecture decisions
- Ensure stakeholder review and approval
- Document changes and version control

## Cross-References
- **Parent Project:** [Enterprise Architecture Documentation](../../README.md)
- **Governance Framework:** [Cross-Cutting Concerns](../../Cross-Cutting-Concerns/)
- **ArchiMate Models:** [Architecture Models](../../ArchiMate-Models/)
- **NORA Compliance:** [Saudi NORA Framework](../../NORA-Compliance/)

---
*TOGAF 9 Templates converted to professional markdown format*  
*Enterprise Architecture Project - TOGAF 10 ADM + ArchiMate 3.2 + Saudi NORA*  
*Conversion completed: {import_date}*
"""
    
    # Write navigation index
    index_path = base_dir / "TEMPLATES_INDEX.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(navigation_content)
    
    print(f"Navigation index created: {index_path}")
    print(f"Total templates indexed: {len(md_files) - 1}")
    
    return str(index_path)

def main():
    """Main function to create navigation index"""
    from datetime import datetime
    global import_date
    import_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    index_path = create_navigation_index()
    print("\n" + "="*60)
    print("TOGAF 9 TEMPLATES NAVIGATION INDEX CREATED")
    print("="*60)
    print(f"Index Location: {index_path}")
    print("="*60)

if __name__ == "__main__":
    main()