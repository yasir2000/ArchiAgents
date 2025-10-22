"""
TOGAF Architecture Development Method (ADM) Implementation

This module implements the complete TOGAF ADM 8-phase cycle with all associated
deliverables, activities, and governance checkpoints.
"""

from .adm_cycle import ADMCycle
from .adm_phase import ADMPhase
from .phase_a_vision import PhaseAArchitectureVision
from .phase_b_business import PhaseBBusinessArchitecture
from .phase_c_information import PhaseCInformationSystems
from .phase_d_technology import PhaseDTechnologyArchitecture
from .phase_e_opportunities import PhaseEOpportunitiesAndSolutions
from .phase_f_migration import PhaseFMigrationPlanning
from .phase_g_governance import PhaseGImplementationGovernance
from .phase_h_change import PhaseHChangeManagement

__all__ = [
    'ADMCycle',
    'ADMPhase',
    'PhaseAArchitectureVision',
    'PhaseBBusinessArchitecture',
    'PhaseCInformationSystems',
    'PhaseDTechnologyArchitecture',
    'PhaseEOpportunitiesAndSolutions',
    'PhaseFMigrationPlanning',
    'PhaseGImplementationGovernance',
    'PhaseHChangeManagement',
]
