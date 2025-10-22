"""
ADM Cycle Coordinator

This module coordinates the execution of the complete TOGAF ADM cycle.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from ..core.base import TOGAFComponent
from ..core.enums import ADMPhaseType
from .adm_phase import ADMPhase


class ADMCycle(TOGAFComponent):
    """
    Coordinates the execution of the TOGAF ADM cycle.
    
    The ADM cycle manages the iterative process through all phases,
    ensuring proper sequencing, governance, and requirements management.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, metadata=metadata)
        self.phases: List[ADMPhase] = []
        self.current_phase_index: int = -1
        self.cycle_status: str = "not_started"
        self.iterations: int = 0
        self.cycle_start_date: Optional[datetime] = None
        self.cycle_end_date: Optional[datetime] = None
        
    def add_phase(self, phase: ADMPhase) -> None:
        """Add a phase to the cycle"""
        self.phases.append(phase)
        
    def start_cycle(self) -> None:
        """Start the ADM cycle"""
        self.cycle_status = "in_progress"
        self.cycle_start_date = datetime.now()
        self.current_phase_index = 0
        self.iterations += 1
        
    def next_phase(self) -> Optional[ADMPhase]:
        """Move to the next phase"""
        if self.current_phase_index < len(self.phases) - 1:
            self.current_phase_index += 1
            return self.phases[self.current_phase_index]
        return None
    
    def get_current_phase(self) -> Optional[ADMPhase]:
        """Get the current phase"""
        if 0 <= self.current_phase_index < len(self.phases):
            return self.phases[self.current_phase_index]
        return None
    
    def complete_cycle(self) -> None:
        """Complete the ADM cycle"""
        self.cycle_status = "completed"
        self.cycle_end_date = datetime.now()
        
    def reset_cycle(self) -> None:
        """Reset for another iteration"""
        self.current_phase_index = -1
        self.cycle_status = "not_started"
        
    def get_cycle_progress(self) -> float:
        """Get overall cycle progress"""
        if not self.phases:
            return 0.0
        total_progress = sum(phase.completion_percentage for phase in self.phases)
        return total_progress / len(self.phases)
    
    def execute_full_cycle(self) -> Dict[str, Any]:
        """Execute the complete ADM cycle"""
        self.start_cycle()
        
        results = {
            'cycle_name': self.name,
            'iteration': self.iterations,
            'phases_executed': [],
            'start_time': self.cycle_start_date.isoformat() if self.cycle_start_date else None,
        }
        
        for phase in self.phases:
            phase_result = phase.execute()
            results['phases_executed'].append({
                'phase': phase.name,
                'phase_type': phase.phase_type.value if phase.phase_type else None,
                'result': phase_result,
            })
            self.next_phase()
            
        self.complete_cycle()
        results['end_time'] = self.cycle_end_date.isoformat() if self.cycle_end_date else None
        results['overall_progress'] = self.get_cycle_progress()
        
        return results
    
    def validate(self) -> bool:
        """Validate the ADM cycle"""
        return bool(self.name and self.phases)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'phases_count': len(self.phases),
            'current_phase': self.get_current_phase().name if self.get_current_phase() else None,
            'cycle_status': self.cycle_status,
            'iterations': self.iterations,
            'overall_progress': self.get_cycle_progress(),
        })
        return base_dict
