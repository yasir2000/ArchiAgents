"""
Enumerations for TOGAF Framework

This module defines all enumerations used throughout the framework.
"""

from enum import Enum, auto


class ADMPhaseType(Enum):
    """TOGAF ADM Phase Types"""
    PRELIMINARY = "preliminary"
    PHASE_A = "architecture_vision"
    PHASE_B = "business_architecture"
    PHASE_C = "information_systems"
    PHASE_D = "technology_architecture"
    PHASE_E = "opportunities_solutions"
    PHASE_F = "migration_planning"
    PHASE_G = "implementation_governance"
    PHASE_H = "architecture_change_management"
    REQUIREMENTS = "requirements_management"


class ArchiMateLayerType(Enum):
    """ArchiMate 3.2 Layer Types"""
    STRATEGY = "strategy"
    BUSINESS = "business"
    APPLICATION = "application"
    TECHNOLOGY = "technology"
    PHYSICAL = "physical"
    IMPLEMENTATION = "implementation"
    MOTIVATION = "motivation"


class ArchiMateAspect(Enum):
    """ArchiMate Aspects"""
    ACTIVE_STRUCTURE = "active_structure"
    BEHAVIOR = "behavior"
    PASSIVE_STRUCTURE = "passive_structure"


class StakeholderType(Enum):
    """Stakeholder Types"""
    EXECUTIVE = "executive"
    BUSINESS = "business"
    ARCHITECT = "architect"
    DEVELOPER = "developer"
    OPERATIONS = "operations"
    SECURITY = "security"
    COMPLIANCE = "compliance"
    VENDOR = "vendor"
    END_USER = "end_user"


class ComplianceLevel(Enum):
    """Compliance Assessment Levels"""
    FULLY_COMPLIANT = 4
    LARGELY_COMPLIANT = 3
    PARTIALLY_COMPLIANT = 2
    NON_COMPLIANT = 1
    NOT_ASSESSED = 0


class RiskLevel(Enum):
    """Risk Assessment Levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NEGLIGIBLE = "negligible"


class PriorityLevel(Enum):
    """Priority Levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class PrincipleCategory(Enum):
    """Architecture Principle Categories"""
    BUSINESS = "business"
    DATA = "data"
    APPLICATION = "application"
    TECHNOLOGY = "technology"
    SECURITY = "security"
    PROCESS = "process"


class RequirementType(Enum):
    """Requirement Types"""
    FUNCTIONAL = "functional"
    NON_FUNCTIONAL = "non_functional"
    CONSTRAINT = "constraint"


class GovernanceRole(Enum):
    """Governance Roles"""
    BOARD_MEMBER = "board_member"
    EXECUTIVE_SPONSOR = "executive_sponsor"
    ARCHITECTURE_BOARD_MEMBER = "architecture_board_member"
    CHANGE_ADVISORY_BOARD_MEMBER = "cab_member"
    ENTERPRISE_ARCHITECT = "enterprise_architect"
    DOMAIN_ARCHITECT = "domain_architect"
    SOLUTION_ARCHITECT = "solution_architect"
    BUSINESS_ARCHITECT = "business_architect"


class DecisionAuthority(Enum):
    """Decision Authority Levels"""
    BOARD = "board"
    EXECUTIVE = "executive"
    MANAGEMENT = "management"
    OPERATIONAL = "operational"


class ArchitectureStatus(Enum):
    """Architecture Status"""
    DRAFT = "draft"
    PROPOSED = "proposed"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    BASELINE = "baseline"
    DEPRECATED = "deprecated"
    RETIRED = "retired"


class ChangeType(Enum):
    """Change Types"""
    STRATEGIC = "strategic"
    TACTICAL = "tactical"
    OPERATIONAL = "operational"
    EMERGENCY = "emergency"


class ProcessType(Enum):
    """Business Process Types"""
    CORE = "core"  # Core business processes that directly create value
    SUPPORTING = "supporting"  # Supporting processes that enable core processes
    MANAGEMENT = "management"  # Management processes that govern and control


class MaturityLevel(Enum):
    """Capability Maturity Levels"""
    INITIAL = 1  # Ad-hoc, unpredictable
    DEFINED = 2  # Documented and standardized
    MANAGED = 3  # Measured and controlled
    OPTIMIZED = 4  # Continuous improvement


class ArtifactType(Enum):
    """TOGAF Artifact Types"""
    CATALOG = "catalog"  # List of architectural elements
    MATRIX = "matrix"  # Relationship between elements
    DIAGRAM = "diagram"  # Visual representation


class IntegrationType(Enum):
    """Integration Pattern Types"""
    SYNCHRONOUS = "synchronous"
    ASYNCHRONOUS = "asynchronous"
    BATCH = "batch"
    REAL_TIME = "real_time"
    EVENT_DRIVEN = "event_driven"


class SecurityPatternType(Enum):
    """Security Pattern Types"""
    ZERO_TRUST = "zero_trust"
    DEFENSE_IN_DEPTH = "defense_in_depth"
    LEAST_PRIVILEGE = "least_privilege"
    ENCRYPTION = "encryption"
    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"


class MonitoringMetricType(Enum):
    """Monitoring Metric Types"""
    AVAILABILITY = "availability"
    PERFORMANCE = "performance"
    CAPACITY = "capacity"
    SECURITY = "security"
    BUSINESS = "business"


class CloudProvider(Enum):
    """Cloud Provider Types"""
    AZURE = "azure"
    AWS = "aws"
    GCP = "gcp"
    HYBRID = "hybrid"
    ON_PREMISE = "on_premise"


class NORADomain(Enum):
    """Saudi NORA Framework Domains"""
    BUSINESS_ARCHITECTURE = "business_architecture"
    INFORMATION_ARCHITECTURE = "information_architecture"
    APPLICATION_ARCHITECTURE = "application_architecture"
    TECHNOLOGY_ARCHITECTURE = "technology_architecture"
    SECURITY_ARCHITECTURE = "security_architecture"
    GOVERNANCE = "governance"
    INTEGRATION = "integration"


class Vision2030Pillar(Enum):
    """Saudi Vision 2030 Pillars"""
    DIGITAL_GOVERNMENT = "digital_government"
    DIGITAL_ECONOMY = "digital_economy"
    DIGITAL_SOCIETY = "digital_society"
