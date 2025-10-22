"""
Setup configuration for TOGAF Framework
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='togaf-framework',
    version='1.0.0',
    author='Enterprise Architecture Team',
    author_email='ea-team@example.com',
    description='Comprehensive Python implementation of TOGAF 10 ADM, ArchiMate 3.2, and Saudi NORA',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yasir2000/ArchiAgents',
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'pydantic>=2.0.0',
        'python-dateutil>=2.8.0',
        'pyyaml>=6.0',
        'jsonschema>=4.0.0',
        'networkx>=3.0',
        'matplotlib>=3.5.0',
        'pandas>=1.5.0',
        'requests>=2.28.0',
        'sqlalchemy>=2.0.0',
        'alembic>=1.10.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.2.0',
        ],
        'nora': [
            'arabic-reshaper>=3.0.0',
            'python-bidi>=0.4.0',
        ],
        'visualization': [
            'graphviz>=0.20.0',
            'plotly>=5.0.0',
            'dash>=2.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'togaf=togaf_framework.cli:main',
        ],
    },
    project_urls={
        'Documentation': 'https://github.com/yasir2000/ArchiAgents/wiki',
        'Source': 'https://github.com/yasir2000/ArchiAgents',
        'Tracker': 'https://github.com/yasir2000/ArchiAgents/issues',
    },
    keywords='togaf, archimate, enterprise-architecture, nora, vision2030, adm, governance',
    include_package_data=True,
    zip_safe=False,
)
