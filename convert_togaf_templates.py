#!/usr/bin/env python3
"""
TOGAF 9 Templates to Professional Markdown Converter (Enhanced with MarkItDown)

This script converts various file formats (.doc, .xls, .xlsx, .txt, .pdf, .pptx) in the TOGAF 9 Templates
directory to professional markdown format while preserving folder structure.

Features:
- Uses Microsoft MarkItDown for superior conversion quality
- Handles multiple file formats including Office documents and PDFs
- Preserves directory structure
- Creates professional markdown with proper headers, tables, and formatting
- Follows enterprise architecture documentation standards
- Integrates with NORA compliance and TOGAF 10 methodology

Requirements:
- markitdown (Microsoft's document conversion tool)
- pandas (for Excel file enhancement)
- tabulate (for professional table formatting)
"""

import os
import sys
import subprocess
import re
from pathlib import Path
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TOGAFTemplateConverter:
    """Converter class for TOGAF 9 templates to markdown"""
    
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.converted_files = []
        self.failed_files = []
        
        # Install required packages
        self._install_dependencies()
        
        # Import packages after installation
        try:
            import pandas as pd
            from markitdown import MarkItDown
            self.pd = pd
            self.markitdown = MarkItDown()
        except ImportError as e:
            logger.error(f"Failed to import required packages: {e}")
            sys.exit(1)
    
    def _install_dependencies(self):
        """Install required Python packages"""
        packages = [
            'markitdown',
            'pandas',
            'openpyxl', 
            'xlrd',
            'tabulate'
        ]
        
        for package in packages:
            try:
                if package == 'markitdown':
                    from markitdown import MarkItDown
                elif package == 'pandas':
                    import pandas
                elif package == 'openpyxl':
                    import openpyxl
                elif package == 'xlrd':
                    import xlrd
                elif package == 'tabulate':
                    import tabulate
                logger.info(f"Package {package} already installed")
            except ImportError:
                logger.info(f"Installing {package}...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    
    def convert_document_with_markitdown(self, file_path: Path) -> str:
        """Convert any document format to markdown using MarkItDown"""
        try:
            logger.info(f"Converting {file_path.name} using MarkItDown...")
            
            # Use MarkItDown to convert the file
            result = self.markitdown.convert(str(file_path))
            
            if not result or not result.text_content.strip():
                return self._create_placeholder_markdown(file_path, file_path.suffix.upper())
            
            # Clean and enhance the converted content
            content = result.text_content.strip()
            
            # Create professional markdown wrapper
            markdown_content = f"""# {self._format_title(file_path.stem)}

## Document Overview
This document is converted from a TOGAF 9 template using Microsoft MarkItDown for high-quality conversion.

**Original File:** `{file_path.name}`  
**File Type:** {file_path.suffix.upper()}  
**Conversion Tool:** Microsoft MarkItDown

## Content

{content}

## Enterprise Integration Notes
- This template supports TOGAF 10 ADM methodology implementation
- Integrate with ArchiMate 3.2 modeling standards
- Ensure NORA compliance for Saudi Vision 2030 alignment
- Follow enterprise governance frameworks

## Usage Guidelines
- Adapt content to specific enterprise architecture context
- Reference cross-cutting concerns and governance patterns
- Maintain traceability to architecture decisions
- Ensure stakeholder review and approval processes

---
*Converted from TOGAF 9 {file_path.suffix} template using Microsoft MarkItDown*  
*Enterprise Architecture Project - Professional Markdown Format*
"""
            return markdown_content
            
        except Exception as e:
            logger.error(f"Error converting file {file_path} with MarkItDown: {e}")
            return self._create_placeholder_markdown(file_path, file_path.suffix.upper())
    
    def convert_txt_to_markdown(self, file_path: Path) -> str:
        """Convert TXT file to professional markdown"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Basic markdown formatting
            markdown_content = f"""# {file_path.stem}

## Overview
This document contains the content from the original TOGAF 9 template file.

## Content

{content}

---
*Converted from TOGAF 9 template to professional markdown format*
*Part of Enterprise Architecture Project - TOGAF 10 ADM Implementation*
"""
            return markdown_content
            
        except Exception as e:
            logger.error(f"Error converting TXT file {file_path}: {e}")
            return ""
    
    def convert_doc_to_markdown(self, file_path: Path) -> str:
        """Convert DOC file to professional markdown using MarkItDown"""
        try:
            # Use MarkItDown for better DOC conversion
            return self.convert_document_with_markitdown(file_path)
            
        except Exception as e:
            logger.error(f"Error converting DOC file {file_path}: {e}")
            return self._create_placeholder_markdown(file_path, "DOC")
            
            content = '\n\n'.join(formatted_lines)
            
            markdown_content = f"""# {self._format_title(file_path.stem)}

## Document Overview
This document is converted from a TOGAF 9 template and contains enterprise architecture guidance and templates.

## Original Content

{content}

## Usage Guidelines
- This template supports TOGAF 10 ADM methodology implementation
- Integrate with ArchiMate 3.2 modeling standards
- Ensure NORA compliance for Saudi Vision 2030 alignment
- Follow enterprise governance frameworks

---
*Converted from TOGAF 9 {file_path.suffix} template*  
*Enterprise Architecture Project - Professional Markdown Format*
"""
            return markdown_content
            
        except Exception as e:
            logger.error(f"Error converting DOC file {file_path}: {e}")
            return self._create_placeholder_markdown(file_path, "DOC")
    
    def convert_excel_enhanced(self, file_path: Path) -> str:
        """Enhanced Excel conversion with better formatting"""
        try:
            # First try MarkItDown for the conversion
            markitdown_result = self.convert_document_with_markitdown(file_path)
            
            # If MarkItDown provides good content, enhance it with pandas table formatting
            if "## Content" in markitdown_result and not "placeholder" in markitdown_result.lower():
                return markitdown_result
            
            # Fallback to pandas-based conversion for better table formatting
            logger.info(f"Using pandas for enhanced Excel conversion: {file_path.name}")
            
            # Read Excel file
            if file_path.suffix.lower() == '.xlsx':
                excel_data = self.pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
            else:  # .xls
                excel_data = self.pd.read_excel(file_path, sheet_name=None, engine='xlrd')
            
            markdown_content = f"""# {self._format_title(file_path.stem)}

## Document Overview
This document contains structured data from a TOGAF 9 template, converted with enhanced formatting for enterprise architecture documentation.

**Original File:** `{file_path.name}`  
**File Type:** Excel  
**Conversion Method:** Enhanced pandas + MarkItDown

"""
            
            # Process each sheet
            for sheet_name, df in excel_data.items():
                if df.empty:
                    continue
                    
                markdown_content += f"## {sheet_name}\n\n"
                
                # Clean the dataframe
                df = df.dropna(how='all').dropna(axis=1, how='all')
                
                if not df.empty:
                    # Convert to markdown table
                    markdown_table = df.to_markdown(index=False, tablefmt='github')
                    markdown_content += f"{markdown_table}\n\n"
                else:
                    markdown_content += "*No data available in this sheet*\n\n"
            
            markdown_content += f"""## Implementation Notes
- This template supports enterprise architecture modeling and documentation
- Integrate with existing ArchiMate models and TOGAF phases
- Ensure compliance with governance frameworks and NORA standards
- Use for strategic planning and architecture development

## Related Templates
- Reference other TOGAF 9 templates in this collection
- Align with Phase-specific deliverables in the enterprise architecture project
- Follow cross-cutting concerns for security, integration, and performance

---
*Converted from TOGAF 9 Excel template using enhanced conversion*  
*Enterprise Architecture Project - Professional Markdown Format*
"""
            return markdown_content
            
        except Exception as e:
            logger.error(f"Error in enhanced Excel conversion {file_path}: {e}")
            return self._create_placeholder_markdown(file_path, "Excel")
    
    def _format_title(self, filename: str) -> str:
        """Format filename into a professional title"""
        # Remove common prefixes and clean up
        title = filename.replace('TOGAF 9 Template - ', '').replace('TOGAF9 Template - ', '')
        title = title.replace('_', ' ').replace('-', ' ')
        
        # Convert to title case
        title = ' '.join(word.capitalize() for word in title.split())
        
        return title
    
    def _create_placeholder_markdown(self, file_path: Path, file_type: str) -> str:
        """Create placeholder markdown for files that couldn't be converted"""
        return f"""# {self._format_title(file_path.stem)}

## Document Overview
This is a placeholder for a TOGAF 9 template that requires manual conversion.

**Original File:** `{file_path.name}`  
**File Type:** {file_type}  
**Location:** `{file_path.parent}`

## Manual Conversion Required
This {file_type} file contains structured content that requires manual review and conversion to maintain formatting and context.

### Recommended Actions
1. Open the original file: `{file_path}`
2. Review the content structure and formatting
3. Create appropriate markdown sections and tables
4. Integrate with enterprise architecture documentation standards

## Template Integration
- Align with TOGAF 10 ADM methodology
- Follow ArchiMate 3.2 modeling standards  
- Ensure NORA compliance requirements
- Reference cross-cutting concerns and governance frameworks

---
*Placeholder created during automated conversion process*  
*Enterprise Architecture Project - Professional Markdown Format*
"""
    
    def convert_file(self, file_path: Path) -> bool:
        """Convert a single file to markdown"""
        try:
            output_path = file_path.with_suffix('.md')
            
            # Skip if already converted
            if output_path.exists():
                logger.info(f"Skipping {file_path.name} - markdown version already exists")
                return True
            
            logger.info(f"Converting {file_path.name}...")
            
            # Determine conversion method based on file extension
            extension = file_path.suffix.lower()
            
            if extension == '.txt':
                markdown_content = self.convert_txt_to_markdown(file_path)
            elif extension in ['.doc', '.docx']:
                markdown_content = self.convert_doc_to_markdown(file_path)
            elif extension in ['.xls', '.xlsx']:
                markdown_content = self.convert_excel_enhanced(file_path)
            elif extension in ['.pdf', '.pptx', '.ppt']:
                # Use MarkItDown for additional file types
                markdown_content = self.convert_document_with_markitdown(file_path)
            else:
                logger.warning(f"Unsupported file type: {extension}")
                return False
            
            if not markdown_content:
                logger.error(f"No content generated for {file_path.name}")
                return False
            
            # Write markdown file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            logger.info(f"Successfully converted {file_path.name} -> {output_path.name}")
            self.converted_files.append(str(output_path))
            return True
            
        except Exception as e:
            logger.error(f"Failed to convert {file_path}: {e}")
            self.failed_files.append(str(file_path))
            return False
    
    def convert_directory(self) -> Dict[str, int]:
        """Convert all supported files in the directory"""
        logger.info(f"Starting conversion process for: {self.source_dir}")
        
        # Supported file extensions (expanded with MarkItDown capabilities)
        supported_extensions = {'.txt', '.doc', '.docx', '.xls', '.xlsx', '.pdf', '.pptx', '.ppt'}
        
        # Find all files to convert
        files_to_convert = []
        for ext in supported_extensions:
            files_to_convert.extend(self.source_dir.rglob(f"*{ext}"))
        
        logger.info(f"Found {len(files_to_convert)} files to convert")
        
        # Convert each file
        for file_path in files_to_convert:
            self.convert_file(file_path)
        
        # Create summary report
        summary = {
            'total_files': len(files_to_convert),
            'converted': len(self.converted_files),
            'failed': len(self.failed_files)
        }
        
        self._create_conversion_report()
        
        return summary
    
    def _create_conversion_report(self):
        """Create a conversion summary report"""
        report_path = self.source_dir / 'CONVERSION_REPORT.md'
        
        report_content = f"""# TOGAF 9 Templates Conversion Report

## Summary
- **Total Files Processed:** {len(self.converted_files) + len(self.failed_files)}
- **Successfully Converted:** {len(self.converted_files)}
- **Failed Conversions:** {len(self.failed_files)}
- **Conversion Date:** {import_date}

## Successfully Converted Files
"""
        
        for file_path in sorted(self.converted_files):
            relative_path = Path(file_path).relative_to(self.source_dir)
            report_content += f"- `{relative_path}`\n"
        
        if self.failed_files:
            report_content += "\n## Failed Conversions\n"
            for file_path in sorted(self.failed_files):
                relative_path = Path(file_path).relative_to(self.source_dir)
                report_content += f"- `{relative_path}` - Requires manual conversion\n"
        
        report_content += f"""
## Next Steps
1. Review converted markdown files for formatting accuracy
2. Manually convert any failed files if needed
3. Integrate templates with enterprise architecture documentation
4. Update navigation and cross-references in parent README files

## Integration Guidelines
- Align converted templates with TOGAF 10 ADM methodology
- Follow ArchiMate 3.2 modeling standards
- Ensure NORA compliance for Saudi Vision 2030 requirements
- Reference cross-cutting concerns and governance frameworks

---
*Generated by TOGAF Template Converter*  
*Enterprise Architecture Project*
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        logger.info(f"Conversion report created: {report_path}")

def main():
    """Main conversion function"""
    from datetime import datetime
    global import_date
    import_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Set the source directory
    source_dir = r"C:\Users\yasir\Code\enterprise-architecture-project\Templates\Togaf9 Templates"
    
    if not os.path.exists(source_dir):
        logger.error(f"Source directory not found: {source_dir}")
        sys.exit(1)
    
    # Create converter instance and run conversion
    converter = TOGAFTemplateConverter(source_dir)
    summary = converter.convert_directory()
    
    # Print summary
    print("\n" + "="*60)
    print("TOGAF 9 TEMPLATES CONVERSION COMPLETE")
    print("="*60)
    print(f"Total Files: {summary['total_files']}")
    print(f"Converted: {summary['converted']}")
    print(f"Failed: {summary['failed']}")
    print(f"Success Rate: {(summary['converted']/summary['total_files']*100):.1f}%")
    print("="*60)
    
    if summary['failed'] > 0:
        print(f"\nNote: {summary['failed']} files require manual conversion.")
        print("Check CONVERSION_REPORT.md for details.")

if __name__ == "__main__":
    main()