"""
AI Modeling Agent

Uses LLM AI agents to intelligently generate architecture models based on:
- TOGAF phase context
- Enterprise requirements
- Best practices and patterns
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime


class AIModelingAgent:
    """
    AI-powered modeling agent for intelligent model generation.
    
    Leverages LLM capabilities to:
    - Analyze enterprise context
    - Generate appropriate model elements
    - Suggest relationships and patterns
    - Apply architecture best practices
    """
    
    def __init__(self, llm_provider: Optional[Any] = None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize AI modeling agent.
        
        Args:
            llm_provider: LLM provider instance (OpenAI, Anthropic, etc.)
            config: Configuration dictionary
        """
        self.llm_provider = llm_provider
        self.config = config or {}
        self.context_history: List[Dict[str, Any]] = []
    
    def generate_archimate_model_with_ai(
        self,
        layer: str,
        togaf_phase: str,
        enterprise_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate ArchiMate model using AI based on TOGAF phase and context.
        
        Args:
            layer: ArchiMate layer (strategy, business, application, technology)
            togaf_phase: Current TOGAF phase (phase-a, phase-b, etc.)
            enterprise_context: Enterprise-specific context and requirements
            
        Returns:
            AI-generated ArchiMate model
        """
        prompt = self._build_archimate_prompt(layer, togaf_phase, enterprise_context)
        
        if self.llm_provider:
            ai_response = self._query_llm(prompt)
            model_data = self._parse_ai_response(ai_response)
        else:
            # Fallback to template-based generation
            model_data = self._generate_template_model(layer, enterprise_context)
        
        return model_data
    
    def generate_bpmn_process_with_ai(
        self,
        process_name: str,
        process_description: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate BPMN process model using AI.
        
        Args:
            process_name: Name of the process
            process_description: Description of what the process does
            context: Additional context (stakeholders, constraints, etc.)
            
        Returns:
            AI-generated BPMN model
        """
        prompt = self._build_bpmn_prompt(process_name, process_description, context)
        
        if self.llm_provider:
            ai_response = self._query_llm(prompt)
            model_data = self._parse_bpmn_response(ai_response)
        else:
            model_data = self._generate_template_bpmn(process_name, context)
        
        return model_data
    
    def generate_uml_diagram_with_ai(
        self,
        diagram_type: str,
        purpose: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate UML diagram using AI.
        
        Args:
            diagram_type: Type of UML diagram (class, sequence, use case, etc.)
            purpose: Purpose and scope of the diagram
            context: Additional context (requirements, constraints, etc.)
            
        Returns:
            AI-generated UML diagram
        """
        prompt = self._build_uml_prompt(diagram_type, purpose, context)
        
        if self.llm_provider:
            ai_response = self._query_llm(prompt)
            model_data = self._parse_uml_response(ai_response, diagram_type)
        else:
            model_data = self._generate_template_uml(diagram_type, context)
        
        return model_data
    
    def suggest_model_improvements(self, model: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Analyze existing model and suggest improvements using AI.
        
        Args:
            model: Existing model to analyze
            
        Returns:
            List of improvement suggestions
        """
        prompt = self._build_improvement_prompt(model)
        
        if self.llm_provider:
            ai_response = self._query_llm(prompt)
            suggestions = self._parse_suggestions(ai_response)
        else:
            suggestions = self._generate_basic_suggestions(model)
        
        return suggestions
    
    def validate_model_compliance(
        self,
        model: Dict[str, Any],
        standards: List[str]
    ) -> Dict[str, Any]:
        """
        Validate model against architecture standards.
        
        Args:
            model: Model to validate
            standards: List of standards to check (ArchiMate, TOGAF, etc.)
            
        Returns:
            Validation results with compliance score and issues
        """
        prompt = self._build_validation_prompt(model, standards)
        
        if self.llm_provider:
            ai_response = self._query_llm(prompt)
            validation_results = self._parse_validation_response(ai_response)
        else:
            validation_results = self._perform_basic_validation(model, standards)
        
        return validation_results
    
    # Private methods for prompt building
    
    def _build_archimate_prompt(
        self,
        layer: str,
        togaf_phase: str,
        context: Dict[str, Any]
    ) -> str:
        """Build prompt for ArchiMate model generation"""
        return f"""
You are an expert enterprise architect creating an ArchiMate 3.0 model.

**Task:** Generate a comprehensive {layer} layer model for TOGAF {togaf_phase}.

**Enterprise Context:**
- Industry: {context.get('industry', 'General')}
- Organization Size: {context.get('organization_size', 'Medium')}
- Strategic Goals: {', '.join(context.get('goals', ['Digital transformation', 'Process optimization']))}
- Key Challenges: {', '.join(context.get('challenges', ['Legacy systems', 'Integration complexity']))}

**Requirements:**
1. Generate appropriate ArchiMate elements for the {layer} layer
2. Ensure alignment with TOGAF {togaf_phase} deliverables
3. Include realistic relationships between elements
4. Follow ArchiMate 3.0 metamodel rules
5. Consider both current-state and target-state architecture

**Output Format (JSON):**
{{
  "elements": [
    {{
      "id": "unique_id",
      "type": "archimate_element_type",
      "name": "Element Name",
      "description": "Element description"
    }}
  ],
  "relationships": [
    {{
      "id": "rel_id",
      "type": "relationship_type",
      "source": "source_element_id",
      "target": "target_element_id"
    }}
  ]
}}

Generate a model with 8-12 elements and appropriate relationships.
"""
    
    def _build_bpmn_prompt(
        self,
        process_name: str,
        description: str,
        context: Dict[str, Any]
    ) -> str:
        """Build prompt for BPMN generation"""
        return f"""
You are an expert business process analyst creating a BPMN 2.0 process model.

**Process Name:** {process_name}

**Description:** {description}

**Context:**
- Process Owner: {context.get('owner', 'Business Operations')}
- Frequency: {context.get('frequency', 'Daily')}
- Average Duration: {context.get('duration', '1-2 hours')}
- Key Stakeholders: {', '.join(context.get('stakeholders', ['Customer', 'Sales', 'Operations']))}

**Requirements:**
1. Create a complete BPMN process flow
2. Include start and end events
3. Add appropriate tasks and activities
4. Include decision gateways where needed
5. Ensure process is executable and follows best practices

**Output Format (JSON):**
{{
  "pools": [{{"id": "pool_1", "name": "{process_name}", "lanes": ["lane_1"]}}],
  "lanes": [{{"id": "lane_1", "name": "Main Process", "pool": "pool_1"}}],
  "events": [
    {{"id": "start_1", "type": "start", "name": "Start"}},
    {{"id": "end_1", "type": "end", "name": "End"}}
  ],
  "tasks": [
    {{"id": "task_1", "type": "task", "name": "Task Name", "lane": "lane_1"}}
  ],
  "gateways": [
    {{"id": "gw_1", "type": "exclusive", "name": "Decision Point"}}
  ],
  "flows": [
    {{"id": "flow_1", "source": "start_1", "target": "task_1"}}
  ]
}}

Create a realistic process with 5-8 tasks and 1-2 gateways.
"""
    
    def _build_uml_prompt(
        self,
        diagram_type: str,
        purpose: str,
        context: Dict[str, Any]
    ) -> str:
        """Build prompt for UML diagram generation"""
        return f"""
You are an expert software architect creating a UML 2.0 {diagram_type} diagram.

**Purpose:** {purpose}

**Context:**
- System Type: {context.get('system_type', 'Enterprise Application')}
- Architecture Style: {context.get('architecture_style', 'Microservices')}
- Technology Stack: {context.get('tech_stack', 'Java, Spring Boot, PostgreSQL')}
- Key Requirements: {', '.join(context.get('requirements', ['Scalability', 'Security', 'Performance']))}

**Requirements:**
1. Create a comprehensive {diagram_type} diagram
2. Follow UML 2.0 notation and best practices
3. Include appropriate elements and relationships
4. Ensure clarity and readability
5. Apply software engineering principles

**Output Format:** JSON structure appropriate for {diagram_type} diagram

Generate a detailed and realistic model.
"""
    
    def _build_improvement_prompt(self, model: Dict[str, Any]) -> str:
        """Build prompt for model improvement suggestions"""
        return f"""
You are an expert enterprise architect reviewing an architecture model.

**Current Model:**
{json.dumps(model, indent=2)}

**Task:** Analyze the model and provide improvement suggestions.

**Analysis Areas:**
1. Completeness - Are all necessary elements present?
2. Relationships - Are relationships appropriate and complete?
3. Best Practices - Does it follow ArchiMate/UML best practices?
4. Naming Conventions - Are elements well-named?
5. Structure - Is the model well-organized?

**Output Format (JSON):**
{{
  "suggestions": [
    {{
      "category": "completeness|relationships|best_practices|naming|structure",
      "severity": "high|medium|low",
      "description": "Detailed description of the issue",
      "recommendation": "Specific recommendation for improvement"
    }}
  ]
}}

Provide 3-5 actionable suggestions.
"""
    
    def _build_validation_prompt(
        self,
        model: Dict[str, Any],
        standards: List[str]
    ) -> str:
        """Build prompt for model validation"""
        return f"""
You are an expert architecture validator checking model compliance.

**Model to Validate:**
{json.dumps(model, indent=2)}

**Standards to Check:**
{', '.join(standards)}

**Validation Criteria:**
1. Metamodel compliance (correct element types and relationships)
2. Naming conventions
3. Relationship validity
4. Layer separation (for ArchiMate)
5. Best practices adherence

**Output Format (JSON):**
{{
  "compliance_score": 0-100,
  "issues": [
    {{
      "standard": "standard_name",
      "severity": "error|warning|info",
      "element": "element_id or relationship_id",
      "description": "Issue description",
      "fix": "How to fix"
    }}
  ],
  "summary": "Overall assessment"
}}

Perform thorough validation.
"""
    
    def _query_llm(self, prompt: str) -> str:
        """Query the LLM provider"""
        if not self.llm_provider:
            return "{}"
        
        try:
            # This would call the actual LLM provider
            # For now, return empty response
            response = self.llm_provider.query(prompt)
            return response
        except Exception as e:
            print(f"LLM query failed: {e}")
            return "{}"
    
    def _parse_ai_response(self, response: str) -> Dict[str, Any]:
        """Parse AI response into model data"""
        try:
            return json.loads(response)
        except:
            return {"elements": [], "relationships": []}
    
    def _parse_bpmn_response(self, response: str) -> Dict[str, Any]:
        """Parse BPMN AI response"""
        try:
            return json.loads(response)
        except:
            return {
                "pools": [],
                "lanes": [],
                "events": [],
                "tasks": [],
                "gateways": [],
                "flows": []
            }
    
    def _parse_uml_response(self, response: str, diagram_type: str) -> Dict[str, Any]:
        """Parse UML AI response"""
        try:
            return json.loads(response)
        except:
            return {"elements": [], "relationships": []}
    
    def _parse_suggestions(self, response: str) -> List[Dict[str, Any]]:
        """Parse improvement suggestions"""
        try:
            data = json.loads(response)
            return data.get("suggestions", [])
        except:
            return []
    
    def _parse_validation_response(self, response: str) -> Dict[str, Any]:
        """Parse validation response"""
        try:
            return json.loads(response)
        except:
            return {
                "compliance_score": 0,
                "issues": [],
                "summary": "Validation failed"
            }
    
    # Template-based fallback methods
    
    def _generate_template_model(
        self,
        layer: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate template-based model (fallback)"""
        return {
            "elements": [
                {
                    "id": f"{layer}_elem_1",
                    "type": f"{layer}_element",
                    "name": f"Sample {layer.title()} Element",
                    "description": f"Template-generated {layer} element"
                }
            ],
            "relationships": []
        }
    
    def _generate_template_bpmn(
        self,
        process_name: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate template BPMN (fallback)"""
        return {
            "pools": [{"id": "pool_1", "name": process_name}],
            "lanes": [],
            "events": [
                {"id": "start_1", "type": "start", "name": "Start"},
                {"id": "end_1", "type": "end", "name": "End"}
            ],
            "tasks": [
                {"id": "task_1", "type": "task", "name": "Process Task"}
            ],
            "gateways": [],
            "flows": [
                {"id": "flow_1", "source": "start_1", "target": "task_1"},
                {"id": "flow_2", "source": "task_1", "target": "end_1"}
            ]
        }
    
    def _generate_template_uml(
        self,
        diagram_type: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate template UML (fallback)"""
        return {
            "elements": [
                {
                    "id": "elem_1",
                    "type": diagram_type,
                    "name": f"Sample {diagram_type.title()} Element"
                }
            ],
            "relationships": []
        }
    
    def _generate_basic_suggestions(self, model: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate basic improvement suggestions"""
        suggestions = []
        
        # Check for missing descriptions
        elements_without_desc = [
            e for e in model.get("elements", [])
            if not e.get("description")
        ]
        
        if elements_without_desc:
            suggestions.append({
                "category": "completeness",
                "severity": "medium",
                "description": f"{len(elements_without_desc)} elements are missing descriptions",
                "recommendation": "Add descriptions to all elements for better documentation"
            })
        
        # Check relationship count
        elem_count = len(model.get("elements", []))
        rel_count = len(model.get("relationships", []))
        
        if elem_count > 3 and rel_count < elem_count * 0.5:
            suggestions.append({
                "category": "relationships",
                "severity": "high",
                "description": "Model has few relationships compared to elements",
                "recommendation": "Review and add missing relationships between elements"
            })
        
        return suggestions
    
    def _perform_basic_validation(
        self,
        model: Dict[str, Any],
        standards: List[str]
    ) -> Dict[str, Any]:
        """Perform basic validation"""
        issues = []
        score = 100
        
        # Check for required fields
        if not model.get("elements"):
            issues.append({
                "standard": "general",
                "severity": "error",
                "element": "model",
                "description": "Model has no elements",
                "fix": "Add at least one element to the model"
            })
            score -= 50
        
        # Check element IDs are unique
        element_ids = [e.get("id") for e in model.get("elements", [])]
        if len(element_ids) != len(set(element_ids)):
            issues.append({
                "standard": "general",
                "severity": "error",
                "element": "elements",
                "description": "Duplicate element IDs found",
                "fix": "Ensure all element IDs are unique"
            })
            score -= 30
        
        return {
            "compliance_score": max(0, score),
            "issues": issues,
            "summary": f"Found {len(issues)} issues" if issues else "Model passed basic validation"
        }
