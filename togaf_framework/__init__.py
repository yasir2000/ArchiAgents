"""
TOGAF 9.0/10 Enterprise Architecture Framework Implementation

This package provides a comprehensive Python implementation of the TOGAF Architecture
Development Method (ADM), ArchiMate 3.2 modeling, and Saudi NORA compliance.

Modules:
    - adm: Architecture Development Method (8 phases)
    - core: Base classes, enumerations, exceptions
    - models: Data models for architecture artifacts
"""

__version__ = "1.0.0"
__author__ = "Enterprise Architecture Team"
__license__ = "MIT"

from .adm import ADMPhase, ADMCycle, PhaseAArchitectureVision, PhaseBBusinessArchitecture
from .models import ArchitectureArtifact, Stakeholder, ArchitecturePrinciple, Requirement

__all__ = [
    'ADMPhase',
    'ADMCycle',
    'PhaseAArchitectureVision',
    'PhaseBBusinessArchitecture',
    'ArchitectureArtifact',
    'Stakeholder',
    'ArchitecturePrinciple',
    'Requirement',
]
