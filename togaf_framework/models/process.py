"""
Business Process Model

Represents business processes in the architecture.
"""

from typing import Optional, Dict, Any, List
from ..core.base import ArchitectureElement
from ..core.enums import ArchiMateLayerType


class BusinessProcess(ArchitectureElement):
    """
    Represents a business process.
    
    A business process represents a sequence of business behaviors that
    achieves a specific business outcome.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        process_owner: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            name,
            description,
            owner=process_owner,
            layer=ArchiMateLayerType.BUSINESS.value,
            metadata=metadata
        )
        self.steps: List[Dict[str, Any]] = []
        self.inputs: List[str] = []
        self.outputs: List[str] = []
        self.automation_level: float = 0.0  # 0.0 to 1.0 (percentage)
        self.cycle_time: Optional[float] = None  # in hours
        self.process_type: str = "core"  # core, supporting, management
        
    def add_step(self, name: str, sequence: int, description: str, responsible: Optional[str] = None) -> None:
        """Add a process step"""
        step = {
            'name': name,
            'description': description,
            'responsible': responsible,
            'sequence': sequence,
        }
        self.steps.append(step)
        
    def add_input(self, input_item: str) -> None:
        """Add a process input"""
        if input_item not in self.inputs:
            self.inputs.append(input_item)
            
    def add_output(self, output_item: str) -> None:
        """Add a process output"""
        if output_item not in self.outputs:
            self.outputs.append(output_item)
            
    def set_automation_level(self, level: float) -> None:
        """Set automation level (0.0 to 1.0)"""
        if 0.0 <= level <= 1.0:
            self.automation_level = level
            
    def set_cycle_time(self, hours: float) -> None:
        """Set process cycle time in hours"""
        self.cycle_time = hours
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'steps_count': len(self.steps),
            'inputs_count': len(self.inputs),
            'outputs_count': len(self.outputs),
            'automation_level': f"{self.automation_level * 100}%",
            'cycle_time': f"{self.cycle_time} hours" if self.cycle_time else None,
            'process_type': self.process_type,
        })
        return base_dict
