#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fix Unicode characters in Phase D example"""

content = open('togaf_framework/examples/phase_d_technology_example.py', 'r', encoding='utf-8').read()

# Replace emoji
replacements = {
    '📊': '[ANALYSIS]',
    '🏗️': '[INFRA]',
    '🔒': '[SECURITY]',
    '⚙️': '[DEVOPS]',
    '📋': '[DOCS]',
    '🎯': '[GOALS]',
    '•': '*'
}

for old, new in replacements.items():
    content = content.replace(old, new)

open('togaf_framework/examples/phase_d_technology_example.py', 'w', encoding='utf-8').write(content)
print('Replaced all emoji characters successfully!')
