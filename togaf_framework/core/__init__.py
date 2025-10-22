"""
Core TOGAF Framework Components

This module contains the foundational classes and utilities for the TOGAF framework.
"""

from .base import TOGAFComponent, ArchitectureElement
from .enums import (
    ADMPhaseType,
    ArchiMateLayerType,
    StakeholderType,
    ComplianceLevel,
    RiskLevel,
    PriorityLevel
)
from .exceptions import (
    TOGAFException,
    ValidationException,
    GovernanceException,
    ComplianceException
)

__all__ = [
    'TOGAFComponent',
    'ArchitectureElement',
    'ADMPhaseType',
    'ArchiMateLayerType',
    'StakeholderType',
    'ComplianceLevel',
    'RiskLevel',
    'PriorityLevel',
    'TOGAFException',
    'ValidationException',
    'GovernanceException',
    'ComplianceException',
]
