"""
TOGAF ADM Complete End-to-End Framework

This module provides a comprehensive orchestrator that ties all 8 TOGAF ADM phases
together into a cohesive framework with full lifecycle management.

Features:
- Complete ADM cycle execution
- Phase-to-phase integration
- State management and persistence
- Progress tracking and reporting
- Real-world business scenario support

TOGAF 9.0 Compliance:
- Full 8-phase ADM cycle
- Architecture Development Method
- Enterprise Continuum
- Architecture Repository
- Governance Framework
"""

import json
from typing import Dict, List, Optional, Any
from datetime import datetime, date
from pathlib import Path

from .adm_phase import ADMPhase
from .phase_a_vision import PhaseAArchitectureVision
from .phase_b_business import PhaseBBusinessArchitecture
from .phase_c_information import PhaseCInformationSystems
from .phase_d_technology import PhaseDTechnologyArchitecture
from .phase_e_opportunities import PhaseEOpportunitiesAndSolutions
from .phase_f_migration import PhaseFMigrationPlanning
from .phase_g_governance import PhaseGImplementationGovernance
from .phase_h_change import PhaseHChangeManagement
from ..core.enums import ArchitectureStatus
from ..core.exceptions import ValidationException


class TOGAFADMOrchestrator:
    """
    Complete TOGAF ADM Framework Orchestrator
    
    Manages the entire Architecture Development Method lifecycle from
    vision through change management with full integration between phases.
    """
    
    def __init__(
        self,
        enterprise_name: str,
        project_name: str,
        architecture_scope: str
    ):
        self.enterprise_name = enterprise_name
        self.project_name = project_name
        self.architecture_scope = architecture_scope
        self.started_at = datetime.now()
        self.completed_at: Optional[datetime] = None
        
        # Initialize all phases
        self.phase_a: Optional[PhaseAArchitectureVision] = None
        self.phase_b: Optional[PhaseBBusinessArchitecture] = None
        self.phase_c: Optional[PhaseCInformationSystems] = None
        self.phase_d: Optional[PhaseDTechnologyArchitecture] = None
        self.phase_e: Optional[PhaseEOpportunitiesAndSolutions] = None
        self.phase_f: Optional[PhaseFMigrationPlanning] = None
        self.phase_g: Optional[PhaseGImplementationGovernance] = None
        self.phase_h: Optional[PhaseHChangeManagement] = None
        
        # Execution tracking
        self.current_phase: Optional[str] = None
        self.execution_history: List[Dict] = []
        self.phase_results: Dict[str, Dict] = {}
        self.overall_status = ArchitectureStatus.DRAFT
        
        # Architecture artifacts
        self.architecture_repository: Dict[str, Any] = {
            'principles': [],
            'standards': [],
            'patterns': [],
            'models': [],
            'deliverables': {}
        }
        
    def initialize_phase_a(self) -> PhaseAArchitectureVision:
        """Initialize Phase A: Architecture Vision"""
        self.phase_a = PhaseAArchitectureVision()
        self.current_phase = "Phase A"
        self._log_phase_start("Phase A: Architecture Vision")
        return self.phase_a
    
    def execute_phase_a(self) -> Dict:
        """Execute Phase A and capture results"""
        if not self.phase_a:
            raise ValidationException("Phase A not initialized")
        
        results = self.phase_a.execute()
        self.phase_results['phase_a'] = results
        
        # Store artifacts in repository
        self._store_phase_artifacts('phase_a', results)
        
        self._log_phase_completion("Phase A", results)
        return results
    
    def initialize_phase_b(self) -> PhaseBBusinessArchitecture:
        """Initialize Phase B: Business Architecture"""
        if not self.phase_a or 'phase_a' not in self.phase_results:
            raise ValidationException("Phase A must be completed before Phase B")
        
        self.phase_b = PhaseBBusinessArchitecture()
        self.current_phase = "Phase B"
        self._log_phase_start("Phase B: Business Architecture")
        return self.phase_b
    
    def execute_phase_b(self) -> Dict:
        """Execute Phase B and capture results"""
        if not self.phase_b:
            raise ValidationException("Phase B not initialized")
        
        results = self.phase_b.execute()
        self.phase_results['phase_b'] = results
        
        self._store_phase_artifacts('phase_b', results)
        self._log_phase_completion("Phase B", results)
        return results
    
    def initialize_phase_c(self) -> PhaseCInformationSystems:
        """Initialize Phase C: Information Systems Architecture"""
        if not self.phase_b or 'phase_b' not in self.phase_results:
            raise ValidationException("Phase B must be completed before Phase C")
        
        self.phase_c = PhaseCInformationSystems()
        self.current_phase = "Phase C"
        self._log_phase_start("Phase C: Information Systems")
        return self.phase_c
    
    def execute_phase_c(self) -> Dict:
        """Execute Phase C and capture results"""
        if not self.phase_c:
            raise ValidationException("Phase C not initialized")
        
        results = self.phase_c.execute()
        self.phase_results['phase_c'] = results
        
        self._store_phase_artifacts('phase_c', results)
        self._log_phase_completion("Phase C", results)
        return results
    
    def initialize_phase_d(self) -> PhaseDTechnologyArchitecture:
        """Initialize Phase D: Technology Architecture"""
        if not self.phase_c or 'phase_c' not in self.phase_results:
            raise ValidationException("Phase C must be completed before Phase D")
        
        self.phase_d = PhaseDTechnologyArchitecture()
        self.current_phase = "Phase D"
        self._log_phase_start("Phase D: Technology Architecture")
        return self.phase_d
    
    def execute_phase_d(self) -> Dict:
        """Execute Phase D and capture results"""
        if not self.phase_d:
            raise ValidationException("Phase D not initialized")
        
        results = self.phase_d.execute()
        self.phase_results['phase_d'] = results
        
        self._store_phase_artifacts('phase_d', results)
        self._log_phase_completion("Phase D", results)
        return results
    
    def initialize_phase_e(self) -> PhaseEOpportunitiesAndSolutions:
        """Initialize Phase E: Opportunities and Solutions"""
        if not self.phase_d or 'phase_d' not in self.phase_results:
            raise ValidationException("Phase D must be completed before Phase E")
        
        self.phase_e = PhaseEOpportunitiesAndSolutions()
        self.current_phase = "Phase E"
        self._log_phase_start("Phase E: Opportunities and Solutions")
        return self.phase_e
    
    def execute_phase_e(self) -> Dict:
        """Execute Phase E and capture results"""
        if not self.phase_e:
            raise ValidationException("Phase E not initialized")
        
        results = self.phase_e.execute()
        self.phase_results['phase_e'] = results
        
        self._store_phase_artifacts('phase_e', results)
        self._log_phase_completion("Phase E", results)
        return results
    
    def initialize_phase_f(self) -> PhaseFMigrationPlanning:
        """Initialize Phase F: Migration Planning"""
        if not self.phase_e or 'phase_e' not in self.phase_results:
            raise ValidationException("Phase E must be completed before Phase F")
        
        self.phase_f = PhaseFMigrationPlanning()
        self.current_phase = "Phase F"
        self._log_phase_start("Phase F: Migration Planning")
        return self.phase_f
    
    def execute_phase_f(self) -> Dict:
        """Execute Phase F and capture results"""
        if not self.phase_f:
            raise ValidationException("Phase F not initialized")
        
        results = self.phase_f.execute()
        self.phase_results['phase_f'] = results
        
        self._store_phase_artifacts('phase_f', results)
        self._log_phase_completion("Phase F", results)
        return results
    
    def initialize_phase_g(self) -> PhaseGImplementationGovernance:
        """Initialize Phase G: Implementation Governance"""
        if not self.phase_f or 'phase_f' not in self.phase_results:
            raise ValidationException("Phase F must be completed before Phase G")
        
        self.phase_g = PhaseGImplementationGovernance()
        self.current_phase = "Phase G"
        self._log_phase_start("Phase G: Implementation Governance")
        return self.phase_g
    
    def execute_phase_g(self) -> Dict:
        """Execute Phase G and capture results"""
        if not self.phase_g:
            raise ValidationException("Phase G not initialized")
        
        results = self.phase_g.execute()
        self.phase_results['phase_g'] = results
        
        self._store_phase_artifacts('phase_g', results)
        self._log_phase_completion("Phase G", results)
        return results
    
    def initialize_phase_h(self) -> PhaseHChangeManagement:
        """Initialize Phase H: Architecture Change Management"""
        if not self.phase_g or 'phase_g' not in self.phase_results:
            raise ValidationException("Phase G must be completed before Phase H")
        
        self.phase_h = PhaseHChangeManagement()
        self.current_phase = "Phase H"
        self._log_phase_start("Phase H: Architecture Change Management")
        return self.phase_h
    
    def execute_phase_h(self) -> Dict:
        """Execute Phase H and capture results"""
        if not self.phase_h:
            raise ValidationException("Phase H not initialized")
        
        results = self.phase_h.execute()
        self.phase_results['phase_h'] = results
        
        self._store_phase_artifacts('phase_h', results)
        self._log_phase_completion("Phase H", results)
        
        # Mark ADM cycle as complete
        self.completed_at = datetime.now()
        self.overall_status = ArchitectureStatus.APPROVED
        
        return results
    
    def execute_full_cycle(
        self,
        config: Dict[str, Any],
        auto_execute: bool = False
    ) -> Dict:
        """
        Execute complete ADM cycle from Phase A through Phase H
        
        Args:
            config: Configuration for each phase
            auto_execute: If True, automatically execute each phase after initialization
        
        Returns:
            Complete results from all phases
        """
        results = {
            'enterprise': self.enterprise_name,
            'project': self.project_name,
            'scope': self.architecture_scope,
            'started_at': self.started_at.isoformat(),
            'phases': {}
        }
        
        try:
            # Phase A: Architecture Vision
            phase_a = self.initialize_phase_a()
            if config.get('phase_a'):
                self._configure_phase(phase_a, config['phase_a'])
            if auto_execute:
                results['phases']['phase_a'] = self.execute_phase_a()
            
            # Phase B: Business Architecture
            phase_b = self.initialize_phase_b()
            if config.get('phase_b'):
                self._configure_phase(phase_b, config['phase_b'])
            if auto_execute:
                results['phases']['phase_b'] = self.execute_phase_b()
            
            # Phase C: Information Systems
            phase_c = self.initialize_phase_c()
            if config.get('phase_c'):
                self._configure_phase(phase_c, config['phase_c'])
            if auto_execute:
                results['phases']['phase_c'] = self.execute_phase_c()
            
            # Phase D: Technology Architecture
            phase_d = self.initialize_phase_d()
            if config.get('phase_d'):
                self._configure_phase(phase_d, config['phase_d'])
            if auto_execute:
                results['phases']['phase_d'] = self.execute_phase_d()
            
            # Phase E: Opportunities and Solutions
            phase_e = self.initialize_phase_e()
            if config.get('phase_e'):
                self._configure_phase(phase_e, config['phase_e'])
            if auto_execute:
                results['phases']['phase_e'] = self.execute_phase_e()
            
            # Phase F: Migration Planning
            phase_f = self.initialize_phase_f()
            if config.get('phase_f'):
                self._configure_phase(phase_f, config['phase_f'])
            if auto_execute:
                results['phases']['phase_f'] = self.execute_phase_f()
            
            # Phase G: Implementation Governance
            phase_g = self.initialize_phase_g()
            if config.get('phase_g'):
                self._configure_phase(phase_g, config['phase_g'])
            if auto_execute:
                results['phases']['phase_g'] = self.execute_phase_g()
            
            # Phase H: Architecture Change Management
            phase_h = self.initialize_phase_h()
            if config.get('phase_h'):
                self._configure_phase(phase_h, config['phase_h'])
            if auto_execute:
                results['phases']['phase_h'] = self.execute_phase_h()
            
            results['completed_at'] = self.completed_at.isoformat() if self.completed_at else None
            results['status'] = self.overall_status.value
            results['execution_history'] = self.execution_history
            results['architecture_repository'] = self.architecture_repository
            
        except Exception as e:
            results['error'] = str(e)
            results['failed_at'] = datetime.now().isoformat()
            raise
        
        return results
    
    def get_progress_summary(self) -> Dict:
        """Get overall ADM cycle progress summary"""
        phases_completed = len(self.phase_results)
        total_phases = 8
        
        return {
            'enterprise': self.enterprise_name,
            'project': self.project_name,
            'current_phase': self.current_phase,
            'phases_completed': phases_completed,
            'total_phases': total_phases,
            'progress_percentage': (phases_completed / total_phases) * 100,
            'status': self.overall_status.value,
            'started_at': self.started_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'duration_minutes': (
                (self.completed_at - self.started_at).total_seconds() / 60
                if self.completed_at else
                (datetime.now() - self.started_at).total_seconds() / 60
            ),
            'completed_phases': list(self.phase_results.keys())
        }
    
    def generate_comprehensive_report(self) -> Dict:
        """Generate comprehensive report across all phases"""
        report = {
            'executive_summary': self._generate_executive_summary(),
            'architecture_vision': self._extract_vision_summary(),
            'business_architecture': self._extract_business_summary(),
            'information_systems': self._extract_information_summary(),
            'technology_architecture': self._extract_technology_summary(),
            'solutions_analysis': self._extract_solutions_summary(),
            'migration_plan': self._extract_migration_summary(),
            'governance_framework': self._extract_governance_summary(),
            'change_management': self._extract_change_summary(),
            'architecture_repository': self.architecture_repository,
            'recommendations': self._generate_recommendations()
        }
        
        return report
    
    def save_architecture_state(self, filepath: str):
        """Save complete architecture state to file"""
        state = {
            'metadata': {
                'enterprise': self.enterprise_name,
                'project': self.project_name,
                'scope': self.architecture_scope,
                'saved_at': datetime.now().isoformat()
            },
            'progress': self.get_progress_summary(),
            'phase_results': self.phase_results,
            'repository': self.architecture_repository,
            'history': self.execution_history
        }
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_architecture_state(self, filepath: str):
        """Load architecture state from file"""
        with open(filepath, 'r') as f:
            state = json.load(f)
        
        self.enterprise_name = state['metadata']['enterprise']
        self.project_name = state['metadata']['project']
        self.architecture_scope = state['metadata']['scope']
        self.phase_results = state['phase_results']
        self.architecture_repository = state['repository']
        self.execution_history = state['history']
    
    # Private helper methods
    
    def _configure_phase(self, phase: ADMPhase, config: Dict):
        """Configure phase with provided settings"""
        # This would contain phase-specific configuration logic
        pass
    
    def _log_phase_start(self, phase_name: str):
        """Log phase start"""
        self.execution_history.append({
            'phase': phase_name,
            'event': 'started',
            'timestamp': datetime.now().isoformat()
        })
    
    def _log_phase_completion(self, phase_name: str, results: Dict):
        """Log phase completion"""
        self.execution_history.append({
            'phase': phase_name,
            'event': 'completed',
            'timestamp': datetime.now().isoformat(),
            'status': results.get('status', 'unknown')
        })
    
    def _store_phase_artifacts(self, phase_key: str, results: Dict):
        """Store phase artifacts in repository"""
        self.architecture_repository['deliverables'][phase_key] = {
            'timestamp': datetime.now().isoformat(),
            'artifacts': results.get('deliverables', [])
        }
    
    def _generate_executive_summary(self) -> Dict:
        """Generate executive summary"""
        return {
            'enterprise': self.enterprise_name,
            'project': self.project_name,
            'scope': self.architecture_scope,
            'status': self.overall_status.value,
            'phases_completed': len(self.phase_results),
            'key_achievements': self._extract_key_achievements()
        }
    
    def _extract_vision_summary(self) -> Optional[Dict]:
        """Extract Phase A summary"""
        if 'phase_a' not in self.phase_results:
            return None
        return {
            'goals': len(self.phase_results['phase_a'].get('goals', [])),
            'principles': len(self.phase_results['phase_a'].get('principles', [])),
            'stakeholders': len(self.phase_results['phase_a'].get('stakeholders', []))
        }
    
    def _extract_business_summary(self) -> Optional[Dict]:
        """Extract Phase B summary"""
        if 'phase_b' not in self.phase_results:
            return None
        return {
            'capabilities': len(self.phase_results['phase_b'].get('capabilities', [])),
            'processes': len(self.phase_results['phase_b'].get('processes', []))
        }
    
    def _extract_information_summary(self) -> Optional[Dict]:
        """Extract Phase C summary"""
        if 'phase_c' not in self.phase_results:
            return None
        return {
            'applications': len(self.phase_results['phase_c'].get('applications', [])),
            'data_entities': len(self.phase_results['phase_c'].get('data_entities', []))
        }
    
    def _extract_technology_summary(self) -> Optional[Dict]:
        """Extract Phase D summary"""
        if 'phase_d' not in self.phase_results:
            return None
        return {
            'cloud_services': len(self.phase_results['phase_d'].get('cloud_services', [])),
            'security_controls': len(self.phase_results['phase_d'].get('security_controls', []))
        }
    
    def _extract_solutions_summary(self) -> Optional[Dict]:
        """Extract Phase E summary"""
        if 'phase_e' not in self.phase_results:
            return None
        return {
            'solution_blocks': len(self.phase_results['phase_e'].get('solution_building_blocks', [])),
            'projects': len(self.phase_results['phase_e'].get('projects', []))
        }
    
    def _extract_migration_summary(self) -> Optional[Dict]:
        """Extract Phase F summary"""
        if 'phase_f' not in self.phase_results:
            return None
        return {
            'migration_projects': len(self.phase_results['phase_f'].get('migration_projects', [])),
            'roadmap_phases': len(self.phase_results['phase_f'].get('roadmap_phases', []))
        }
    
    def _extract_governance_summary(self) -> Optional[Dict]:
        """Extract Phase G summary"""
        if 'phase_g' not in self.phase_results:
            return None
        return {
            'contracts': len(self.phase_results['phase_g'].get('contracts', [])),
            'compliance_checks': len(self.phase_results['phase_g'].get('compliance_checks', []))
        }
    
    def _extract_change_summary(self) -> Optional[Dict]:
        """Extract Phase H summary"""
        if 'phase_h' not in self.phase_results:
            return None
        return {
            'change_requests': len(self.phase_results['phase_h'].get('change_requests', [])),
            'monitors': len(self.phase_results['phase_h'].get('monitors', []))
        }
    
    def _extract_key_achievements(self) -> List[str]:
        """Extract key achievements across all phases"""
        achievements = []
        
        if 'phase_a' in self.phase_results:
            achievements.append("Architecture vision and strategic goals established")
        if 'phase_b' in self.phase_results:
            achievements.append("Business capabilities and processes mapped")
        if 'phase_c' in self.phase_results:
            achievements.append("Application and data architectures defined")
        if 'phase_d' in self.phase_results:
            achievements.append("Technology infrastructure designed")
        if 'phase_e' in self.phase_results:
            achievements.append("Solution alternatives analyzed with ROI")
        if 'phase_f' in self.phase_results:
            achievements.append("Migration roadmap and plan created")
        if 'phase_g' in self.phase_results:
            achievements.append("Governance framework established")
        if 'phase_h' in self.phase_results:
            achievements.append("Change management process activated")
        
        return achievements
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on architecture"""
        recommendations = []
        
        # Add general recommendations
        recommendations.append("Establish Architecture Board for ongoing governance")
        recommendations.append("Implement continuous monitoring of architecture compliance")
        recommendations.append("Maintain architecture repository with regular updates")
        recommendations.append("Conduct quarterly architecture reviews")
        recommendations.append("Foster architecture community of practice")
        
        return recommendations
