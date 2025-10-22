"""
Runtime Decision Engine

Core AI-driven decision-making engine for architecture governance.
Provides intelligent, context-aware decisions across TOGAF phases
and ArchiMate layers.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from datetime import datetime
import json


class DecisionType(Enum):
    """Types of architecture decisions"""
    STRATEGIC = "strategic"              # Strategic direction
    TACTICAL = "tactical"                # Implementation approach
    TECHNICAL = "technical"              # Technology selection
    ORGANIZATIONAL = "organizational"    # Org structure/roles
    GOVERNANCE = "governance"            # Policies and standards
    RISK = "risk"                        # Risk mitigation
    COMPLIANCE = "compliance"            # Regulatory compliance
    OPTIMIZATION = "optimization"        # Performance/cost optimization


class DecisionPriority(Enum):
    """Priority levels for decisions"""
    CRITICAL = "critical"    # Immediate action required
    HIGH = "high"           # Action needed soon
    MEDIUM = "medium"       # Normal priority
    LOW = "low"             # Can be deferred


class DecisionConfidence(Enum):
    """Confidence level in decision"""
    VERY_HIGH = "very_high"  # 90-100% confident
    HIGH = "high"            # 75-90% confident
    MEDIUM = "medium"        # 50-75% confident
    LOW = "low"              # 25-50% confident
    VERY_LOW = "very_low"    # <25% confident


@dataclass
class DecisionContext:
    """Context for making architecture decisions"""
    
    # TOGAF Phase Context
    togaf_phase: str                    # Current TOGAF phase (A-H)
    phase_objectives: List[str]         # Phase-specific objectives
    
    # ArchiMate Layer Context
    archimate_layer: str                # ArchiMate layer
    affected_elements: List[Dict]       # Affected architecture elements
    
    # Business Context
    business_drivers: List[str]         # Business drivers
    stakeholders: List[Dict]            # Stakeholder information
    constraints: List[str]              # Known constraints
    
    # Technical Context
    current_state: Dict[str, Any]       # Current architecture state
    target_state: Dict[str, Any]        # Target architecture state
    gaps: List[Dict]                    # Identified gaps
    
    # Decision Context
    decision_type: DecisionType         # Type of decision needed
    decision_scope: str                 # Scope of decision
    urgency: DecisionPriority           # Urgency level
    
    # Additional Context
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DecisionOption:
    """Represents a decision option/alternative"""
    
    option_id: str
    name: str
    description: str
    
    # Evaluation Criteria
    feasibility: float                  # 0-1 score
    cost: float                         # Estimated cost
    time_to_implement: int              # Days
    complexity: float                   # 0-1 score
    risk_level: float                   # 0-1 score
    
    # Benefits
    benefits: List[str]
    strategic_alignment: float          # 0-1 score
    technical_fit: float                # 0-1 score
    
    # Constraints & Dependencies
    dependencies: List[str]
    constraints: List[str]
    prerequisites: List[str]
    
    # Impact Analysis
    impacted_systems: List[str]
    impacted_stakeholders: List[str]
    organizational_impact: str
    
    # Additional Info
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DecisionResult:
    """Result of AI-driven decision-making"""
    
    # Decision Info
    decision_id: str
    timestamp: datetime
    context: DecisionContext
    
    # Recommended Decision
    recommended_option: DecisionOption
    confidence: DecisionConfidence
    reasoning: str                      # AI reasoning explanation
    
    # Alternative Options
    alternative_options: List[DecisionOption]
    comparison_matrix: Dict[str, Any]   # Comparison of options
    
    # Implementation Guidance
    implementation_plan: List[Dict]     # Step-by-step plan
    success_criteria: List[str]         # How to measure success
    risk_mitigation: List[Dict]         # Risk mitigation strategies
    
    # Governance & Approval
    required_approvals: List[str]       # Who needs to approve
    governance_checkpoints: List[Dict]  # Governance gates
    compliance_requirements: List[str]  # Compliance needs
    
    # Monitoring & Learning
    kpis: List[Dict]                    # KPIs to track
    review_schedule: str                # When to review decision
    learning_notes: List[str]           # Notes for learning system
    
    # Additional Info
    metadata: Dict[str, Any] = field(default_factory=dict)


class RuntimeDecisionEngine:
    """
    AI-driven runtime decision engine for enterprise architecture.
    
    Provides autonomous, intelligent decision-making across TOGAF phases
    and ArchiMate layers using LLM-powered analysis.
    """
    
    def __init__(self, llm=None, knowledge_graph=None):
        """
        Initialize decision engine.
        
        Args:
            llm: Language model for AI reasoning (optional)
            knowledge_graph: Architecture knowledge graph (optional)
        """
        self.llm = llm
        self.knowledge_graph = knowledge_graph
        self.decision_history: List[DecisionResult] = []
        self.decision_templates: Dict[str, Any] = {}
        self.learning_enabled = True
        
        # Initialize decision templates
        self._initialize_templates()
    
    def _initialize_templates(self):
        """Initialize decision templates for common scenarios"""
        
        self.decision_templates = {
            "cloud_migration": {
                "type": DecisionType.TECHNICAL,
                "criteria": ["cost", "scalability", "security", "vendor_lock_in"],
                "stakeholders": ["CTO", "CFO", "Security"],
            },
            "microservices_adoption": {
                "type": DecisionType.TECHNICAL,
                "criteria": ["complexity", "team_skills", "scalability", "maintenance"],
                "stakeholders": ["Architects", "Development", "Operations"],
            },
            "data_governance": {
                "type": DecisionType.GOVERNANCE,
                "criteria": ["compliance", "data_quality", "privacy", "cost"],
                "stakeholders": ["Legal", "Compliance", "Data Office"],
            },
            "security_framework": {
                "type": DecisionType.GOVERNANCE,
                "criteria": ["threat_coverage", "compliance", "usability", "cost"],
                "stakeholders": ["CISO", "Compliance", "IT"],
            },
        }
    
    def make_decision(
        self,
        context: DecisionContext,
        options: List[DecisionOption],
        use_ai: bool = True
    ) -> DecisionResult:
        """
        Make an intelligent architecture decision.
        
        Args:
            context: Decision context
            options: Available decision options
            use_ai: Whether to use AI for analysis
        
        Returns:
            DecisionResult with recommendation
        """
        print(f"\n🤖 Making decision for: {context.decision_scope}")
        print(f"   Phase: {context.togaf_phase}, Layer: {context.archimate_layer}")
        print(f"   Type: {context.decision_type.value}, Priority: {context.urgency.value}")
        
        # Analyze options
        analyzed_options = self._analyze_options(context, options, use_ai)
        
        # Select best option
        recommended, confidence = self._select_best_option(
            context, analyzed_options, use_ai
        )
        
        # Generate reasoning
        reasoning = self._generate_reasoning(
            context, recommended, analyzed_options, use_ai
        )
        
        # Create implementation plan
        impl_plan = self._create_implementation_plan(
            context, recommended, use_ai
        )
        
        # Identify risks and mitigation
        risks = self._identify_risks(context, recommended, use_ai)
        
        # Determine approvals needed
        approvals = self._determine_approvals(context, recommended)
        
        # Create decision result
        result = DecisionResult(
            decision_id=f"DEC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            timestamp=datetime.now(),
            context=context,
            recommended_option=recommended,
            confidence=confidence,
            reasoning=reasoning,
            alternative_options=[opt for opt in analyzed_options if opt != recommended],
            comparison_matrix=self._create_comparison_matrix(analyzed_options),
            implementation_plan=impl_plan,
            success_criteria=self._define_success_criteria(context, recommended),
            risk_mitigation=risks,
            required_approvals=approvals,
            governance_checkpoints=self._define_governance_checkpoints(context),
            compliance_requirements=self._identify_compliance_requirements(context),
            kpis=self._define_kpis(context, recommended),
            review_schedule=self._determine_review_schedule(context),
            learning_notes=[]
        )
        
        # Store decision for learning
        self.decision_history.append(result)
        
        print(f"✅ Decision made: {recommended.name}")
        print(f"   Confidence: {confidence.value}")
        print(f"   Reasoning: {reasoning[:100]}...")
        
        return result
    
    def _analyze_options(
        self,
        context: DecisionContext,
        options: List[DecisionOption],
        use_ai: bool
    ) -> List[DecisionOption]:
        """Analyze and score all options"""
        
        if use_ai and self.llm:
            # Use AI to analyze options
            return self._ai_analyze_options(context, options)
        else:
            # Use rule-based analysis
            return self._rule_based_analyze(context, options)
    
    def _ai_analyze_options(
        self,
        context: DecisionContext,
        options: List[DecisionOption]
    ) -> List[DecisionOption]:
        """Use AI to analyze decision options"""
        
        # Prepare analysis prompt
        prompt = self._create_analysis_prompt(context, options)
        
        # Get AI analysis (placeholder - would use actual LLM)
        # analysis = self.llm.invoke(prompt)
        
        # For now, return options as-is
        # In real implementation, would enhance with AI insights
        return options
    
    def _rule_based_analyze(
        self,
        context: DecisionContext,
        options: List[DecisionOption]
    ) -> List[DecisionOption]:
        """Rule-based option analysis"""
        
        # Apply context-specific scoring rules
        for option in options:
            # Adjust scores based on context
            if context.urgency == DecisionPriority.CRITICAL:
                # Prioritize faster options
                option.feasibility *= (1.0 - option.time_to_implement / 365)
            
            if "compliance" in context.constraints:
                # Prioritize low-risk options
                option.feasibility *= (1.0 - option.risk_level)
        
        return options
    
    def _select_best_option(
        self,
        context: DecisionContext,
        options: List[DecisionOption],
        use_ai: bool
    ) -> Tuple[DecisionOption, DecisionConfidence]:
        """Select the best option from analyzed alternatives"""
        
        # Calculate composite scores
        scored_options = []
        for option in options:
            score = self._calculate_composite_score(context, option)
            scored_options.append((option, score))
        
        # Sort by score
        scored_options.sort(key=lambda x: x[1], reverse=True)
        
        # Get best option
        best_option, best_score = scored_options[0]
        
        # Determine confidence based on score spread
        if len(scored_options) > 1:
            second_score = scored_options[1][1]
            score_diff = best_score - second_score
            
            if score_diff > 0.3:
                confidence = DecisionConfidence.VERY_HIGH
            elif score_diff > 0.2:
                confidence = DecisionConfidence.HIGH
            elif score_diff > 0.1:
                confidence = DecisionConfidence.MEDIUM
            else:
                confidence = DecisionConfidence.LOW
        else:
            confidence = DecisionConfidence.MEDIUM
        
        return best_option, confidence
    
    def _calculate_composite_score(
        self,
        context: DecisionContext,
        option: DecisionOption
    ) -> float:
        """Calculate composite score for an option"""
        
        # Define weights based on decision type
        weights = {
            DecisionType.STRATEGIC: {
                "strategic_alignment": 0.4,
                "feasibility": 0.2,
                "risk_level": 0.2,
                "cost": 0.2,
            },
            DecisionType.TACTICAL: {
                "feasibility": 0.3,
                "technical_fit": 0.3,
                "complexity": 0.2,
                "cost": 0.2,
            },
            DecisionType.TECHNICAL: {
                "technical_fit": 0.4,
                "feasibility": 0.3,
                "complexity": 0.2,
                "cost": 0.1,
            },
            DecisionType.ORGANIZATIONAL: {
                "feasibility": 0.3,
                "strategic_alignment": 0.3,
                "risk_level": 0.2,
                "cost": 0.2,
            },
            DecisionType.GOVERNANCE: {
                "feasibility": 0.3,
                "risk_level": 0.3,
                "strategic_alignment": 0.2,
                "cost": 0.2,
            },
            DecisionType.RISK: {
                "risk_level": 0.4,
                "feasibility": 0.3,
                "cost": 0.2,
                "technical_fit": 0.1,
            },
            DecisionType.COMPLIANCE: {
                "feasibility": 0.4,
                "risk_level": 0.3,
                "cost": 0.2,
                "technical_fit": 0.1,
            },
            DecisionType.OPTIMIZATION: {
                "technical_fit": 0.3,
                "complexity": 0.3,
                "cost": 0.2,
                "feasibility": 0.2,
            },
        }
        
        # Default weights for unknown types
        default_weights = {
            "strategic_alignment": 0.25,
            "technical_fit": 0.25,
            "feasibility": 0.25,
            "risk_level": 0.25,
        }
        
        # Get weights for decision type
        type_weights = weights.get(context.decision_type, default_weights)
        
        # Calculate score
        score = 0.0
        score += type_weights.get("strategic_alignment", 0.2) * option.strategic_alignment
        score += type_weights.get("technical_fit", 0.2) * option.technical_fit
        score += type_weights.get("feasibility", 0.2) * option.feasibility
        score += type_weights.get("risk_level", 0.2) * (1.0 - option.risk_level)
        score += type_weights.get("complexity", 0.2) * (1.0 - option.complexity)
        score += type_weights.get("cost", 0.0) * (1.0 - min(option.cost / 1000000, 1.0))
        
        return score
    
    def _generate_reasoning(
        self,
        context: DecisionContext,
        recommended: DecisionOption,
        all_options: List[DecisionOption],
        use_ai: bool
    ) -> str:
        """Generate explanation for the decision"""
        
        reasoning = f"Selected '{recommended.name}' based on the following analysis:\n\n"
        
        reasoning += f"Context: {context.decision_scope} in {context.togaf_phase}\n"
        reasoning += f"Decision Type: {context.decision_type.value}\n\n"
        
        reasoning += "Key Factors:\n"
        reasoning += f"- Strategic Alignment: {recommended.strategic_alignment:.2f}\n"
        reasoning += f"- Technical Fit: {recommended.technical_fit:.2f}\n"
        reasoning += f"- Feasibility: {recommended.feasibility:.2f}\n"
        reasoning += f"- Risk Level: {recommended.risk_level:.2f}\n"
        reasoning += f"- Estimated Cost: ${recommended.cost:,.0f}\n"
        reasoning += f"- Time to Implement: {recommended.time_to_implement} days\n\n"
        
        reasoning += "Benefits:\n"
        for benefit in recommended.benefits[:3]:
            reasoning += f"- {benefit}\n"
        
        return reasoning
    
    def _create_implementation_plan(
        self,
        context: DecisionContext,
        option: DecisionOption,
        use_ai: bool
    ) -> List[Dict]:
        """Create implementation plan for decision"""
        
        plan = []
        
        # Phase 1: Preparation
        plan.append({
            "phase": "Preparation",
            "duration_days": 14,
            "activities": [
                "Stakeholder communication",
                "Resource allocation",
                "Risk assessment",
                "Governance approval",
            ],
            "deliverables": ["Kick-off presentation", "Resource plan"],
        })
        
        # Phase 2: Implementation
        plan.append({
            "phase": "Implementation",
            "duration_days": option.time_to_implement - 28,
            "activities": [
                "Execute implementation",
                "Quality assurance",
                "Documentation",
                "Training",
            ],
            "deliverables": ["Implemented solution", "Documentation"],
        })
        
        # Phase 3: Validation
        plan.append({
            "phase": "Validation",
            "duration_days": 14,
            "activities": [
                "Testing and validation",
                "Stakeholder review",
                "Performance monitoring",
                "Lessons learned",
            ],
            "deliverables": ["Validation report", "Lessons learned"],
        })
        
        return plan
    
    def _identify_risks(
        self,
        context: DecisionContext,
        option: DecisionOption,
        use_ai: bool
    ) -> List[Dict]:
        """Identify risks and mitigation strategies"""
        
        risks = []
        
        # High complexity risk
        if option.complexity > 0.7:
            risks.append({
                "risk": "High implementation complexity",
                "likelihood": "Medium",
                "impact": "High",
                "mitigation": "Engage experienced architects, phased rollout",
            })
        
        # Cost overrun risk
        if option.cost > 500000:
            risks.append({
                "risk": "Budget overrun",
                "likelihood": "Medium",
                "impact": "High",
                "mitigation": "Detailed cost estimation, regular reviews",
            })
        
        # Technical risk
        if option.technical_fit < 0.6:
            risks.append({
                "risk": "Technical fit concerns",
                "likelihood": "Medium",
                "impact": "Medium",
                "mitigation": "Proof of concept, technical validation",
            })
        
        return risks
    
    def _determine_approvals(
        self,
        context: DecisionContext,
        option: DecisionOption
    ) -> List[str]:
        """Determine required approvals"""
        
        approvals = ["Enterprise Architect"]
        
        # Cost-based approvals
        if option.cost > 100000:
            approvals.append("CFO")
        
        # Strategic approvals
        if context.decision_type == DecisionType.STRATEGIC:
            approvals.extend(["CTO", "CEO"])
        
        # Governance approvals
        if context.decision_type == DecisionType.GOVERNANCE:
            approvals.append("Architecture Board")
        
        # Risk-based approvals
        if option.risk_level > 0.7:
            approvals.append("Risk Management")
        
        return list(set(approvals))  # Remove duplicates
    
    def _create_comparison_matrix(
        self,
        options: List[DecisionOption]
    ) -> Dict[str, Any]:
        """Create comparison matrix for options"""
        
        matrix = {
            "options": [opt.name for opt in options],
            "criteria": {
                "feasibility": [opt.feasibility for opt in options],
                "cost": [opt.cost for opt in options],
                "risk": [opt.risk_level for opt in options],
                "strategic_alignment": [opt.strategic_alignment for opt in options],
                "technical_fit": [opt.technical_fit for opt in options],
            }
        }
        
        return matrix
    
    def _define_success_criteria(
        self,
        context: DecisionContext,
        option: DecisionOption
    ) -> List[str]:
        """Define success criteria for decision"""
        
        criteria = [
            "Implementation completed on time and budget",
            "All stakeholders satisfied with outcome",
            "Technical objectives achieved",
            "No critical issues post-implementation",
        ]
        
        # Add context-specific criteria
        if context.decision_type == DecisionType.TECHNICAL:
            criteria.append("System performance meets SLAs")
        
        if context.decision_type == DecisionType.GOVERNANCE:
            criteria.append("Compliance requirements satisfied")
        
        return criteria
    
    def _define_governance_checkpoints(
        self,
        context: DecisionContext
    ) -> List[Dict]:
        """Define governance checkpoints"""
        
        checkpoints = [
            {
                "checkpoint": "Architecture Board Review",
                "timing": "Before implementation",
                "criteria": ["Architecture alignment", "Standards compliance"],
            },
            {
                "checkpoint": "Mid-Implementation Review",
                "timing": "50% complete",
                "criteria": ["Progress on track", "Issues identified"],
            },
            {
                "checkpoint": "Final Review",
                "timing": "Post-implementation",
                "criteria": ["Success criteria met", "Lessons learned"],
            },
        ]
        
        return checkpoints
    
    def _identify_compliance_requirements(
        self,
        context: DecisionContext
    ) -> List[str]:
        """Identify compliance requirements"""
        
        requirements = []
        
        # Extract from context
        for constraint in context.constraints:
            if "compliance" in constraint.lower():
                requirements.append(constraint)
        
        # Add standard requirements
        requirements.extend([
            "Data protection regulations",
            "Security standards",
            "Industry regulations",
        ])
        
        return requirements
    
    def _define_kpis(
        self,
        context: DecisionContext,
        option: DecisionOption
    ) -> List[Dict]:
        """Define KPIs for monitoring decision"""
        
        kpis = [
            {
                "name": "Implementation Progress",
                "target": "100%",
                "frequency": "Weekly",
            },
            {
                "name": "Budget Variance",
                "target": "<10%",
                "frequency": "Monthly",
            },
            {
                "name": "Stakeholder Satisfaction",
                "target": ">80%",
                "frequency": "Monthly",
            },
        ]
        
        return kpis
    
    def _determine_review_schedule(
        self,
        context: DecisionContext
    ) -> str:
        """Determine when to review decision"""
        
        if context.urgency == DecisionPriority.CRITICAL:
            return "Weekly during implementation, monthly post-implementation"
        elif context.urgency == DecisionPriority.HIGH:
            return "Bi-weekly during implementation, quarterly post-implementation"
        else:
            return "Monthly during implementation, annually post-implementation"
    
    def _create_analysis_prompt(
        self,
        context: DecisionContext,
        options: List[DecisionOption]
    ) -> str:
        """Create prompt for AI analysis"""
        
        prompt = f"""Analyze the following architecture decision:

Context:
- TOGAF Phase: {context.togaf_phase}
- ArchiMate Layer: {context.archimate_layer}
- Decision Type: {context.decision_type.value}
- Scope: {context.decision_scope}

Options:
"""
        for i, opt in enumerate(options, 1):
            prompt += f"\n{i}. {opt.name}: {opt.description}\n"
        
        prompt += "\nProvide detailed analysis of each option considering feasibility, cost, risk, and strategic alignment."
        
        return prompt
    
    def get_decision_history(
        self,
        filter_by: Optional[Dict] = None
    ) -> List[DecisionResult]:
        """Get decision history with optional filtering"""
        
        if not filter_by:
            return self.decision_history
        
        # Filter decisions
        filtered = self.decision_history
        
        if "togaf_phase" in filter_by:
            filtered = [
                d for d in filtered
                if d.context.togaf_phase == filter_by["togaf_phase"]
            ]
        
        if "decision_type" in filter_by:
            filtered = [
                d for d in filtered
                if d.context.decision_type == filter_by["decision_type"]
            ]
        
        return filtered
    
    def export_decision(
        self,
        decision: DecisionResult,
        format: str = "json"
    ) -> str:
        """Export decision to specified format"""
        
        if format == "json":
            # Convert to dict (simplified)
            decision_dict = {
                "decision_id": decision.decision_id,
                "timestamp": decision.timestamp.isoformat(),
                "recommended_option": decision.recommended_option.name,
                "confidence": decision.confidence.value,
                "reasoning": decision.reasoning,
            }
            return json.dumps(decision_dict, indent=2)
        
        return str(decision)
