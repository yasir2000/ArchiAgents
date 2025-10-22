"""
Data Models for TOGAF Framework

This module contains all data models used throughout the framework.
"""

from .stakeholder import Stakeholder
from .principle import ArchitecturePrinciple
from .requirement import Requirement
from .artifact import ArchitectureArtifact
from .capability import BusinessCapability
from .process import BusinessProcess
from .application import Application
from .technology import TechnologyComponent

__all__ = [
    'Stakeholder',
    'ArchitecturePrinciple',
    'Requirement',
    'ArchitectureArtifact',
    'BusinessCapability',
    'BusinessProcess',
    'Application',
    'TechnologyComponent',
]
