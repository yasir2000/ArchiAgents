"""
Model Generation Engine

Core engine for generating various architecture models using AI agents.
Supports TOGAF phases and ArchiMate layers.
"""

import json
from typing import Dict, List, Any, Optional
from enum import Enum
from datetime import datetime


class ModelType(Enum):
    """Supported model types"""
    # ArchiMate 3.0
    ARCHIMATE_STRATEGY = "archimate_strategy"
    ARCHIMATE_BUSINESS = "archimate_business"
    ARCHIMATE_APPLICATION = "archimate_application"
    ARCHIMATE_TECHNOLOGY = "archimate_technology"
    ARCHIMATE_PHYSICAL = "archimate_physical"
    ARCHIMATE_IMPLEMENTATION = "archimate_implementation"
    ARCHIMATE_MOTIVATION = "archimate_motivation"
    
    # BPMN 2.0
    BPMN_PROCESS = "bpmn_process"
    BPMN_COLLABORATION = "bpmn_collaboration"
    BPMN_CHOREOGRAPHY = "bpmn_choreography"
    
    # UML 2.0 (12 diagram types)
    UML_CLASS = "uml_class"
    UML_USE_CASE = "uml_use_case"
    UML_SEQUENCE = "uml_sequence"
    UML_ACTIVITY = "uml_activity"
    UML_STATE_MACHINE = "uml_state_machine"
    UML_COMPONENT = "uml_component"
    UML_DEPLOYMENT = "uml_deployment"
    UML_OBJECT = "uml_object"
    UML_PACKAGE = "uml_package"
    UML_TIMING = "uml_timing"
    UML_COMMUNICATION = "uml_communication"
    UML_INTERACTION_OVERVIEW = "uml_interaction_overview"


class ArchitectureLayer(Enum):
    """ArchiMate architecture layers"""
    STRATEGY = "strategy"
    BUSINESS = "business"
    APPLICATION = "application"
    TECHNOLOGY = "technology"
    PHYSICAL = "physical"
    IMPLEMENTATION = "implementation"


class ModelGenerationEngine:
    """
    Core engine for generating architecture models.
    
    Features:
    - AI-driven model generation
    - Multiple model types (ArchiMate, BPMN, UML)
    - Multiple output formats
    - TOGAF phase integration
    - Enterprise Architect integration
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the model generation engine.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.models: Dict[str, Dict[str, Any]] = {}
        
    def generate_archimate_model(
        self,
        layer: ArchitectureLayer,
        context: Dict[str, Any],
        use_ai: bool = True
    ) -> Dict[str, Any]:
        """
        Generate ArchiMate 3.0 model for specified layer.
        
        Args:
            layer: ArchiMate layer (strategy, business, application, etc.)
            context: Context information from TOGAF phases
            use_ai: Whether to use AI for intelligent generation
            
        Returns:
            ArchiMate model dictionary
        """
        model = {
            "id": f"archimate_{layer.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": f"archimate_{layer.value}",
            "layer": layer.value,
            "name": f"{layer.value.title()} Layer Model",
            "created": datetime.now().isoformat(),
            "elements": [],
            "relationships": [],
            "metadata": context
        }
        
        # Generate elements based on layer
        if layer == ArchitectureLayer.STRATEGY:
            model["elements"] = self._generate_strategy_elements(context, use_ai)
        elif layer == ArchitectureLayer.BUSINESS:
            model["elements"] = self._generate_business_elements(context, use_ai)
        elif layer == ArchitectureLayer.APPLICATION:
            model["elements"] = self._generate_application_elements(context, use_ai)
        elif layer == ArchitectureLayer.TECHNOLOGY:
            model["elements"] = self._generate_technology_elements(context, use_ai)
        elif layer == ArchitectureLayer.PHYSICAL:
            model["elements"] = self._generate_physical_elements(context, use_ai)
        elif layer == ArchitectureLayer.IMPLEMENTATION:
            model["elements"] = self._generate_implementation_elements(context, use_ai)
        
        # Generate relationships
        model["relationships"] = self._generate_relationships(model["elements"], use_ai)
        
        # Store model
        self.models[model["id"]] = model
        
        return model
    
    def generate_bpmn_model(
        self,
        process_name: str,
        context: Dict[str, Any],
        model_type: str = "process",
        use_ai: bool = True
    ) -> Dict[str, Any]:
        """
        Generate BPMN 2.0 process model.
        
        Args:
            process_name: Name of the process
            context: Context information
            model_type: Type of BPMN model (process, collaboration, choreography)
            use_ai: Whether to use AI for intelligent generation
            
        Returns:
            BPMN model dictionary
        """
        model = {
            "id": f"bpmn_{process_name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": f"bpmn_{model_type}",
            "name": process_name,
            "created": datetime.now().isoformat(),
            "pools": [],
            "lanes": [],
            "tasks": [],
            "gateways": [],
            "events": [],
            "flows": [],
            "metadata": context
        }
        
        # Generate BPMN elements
        if use_ai:
            model.update(self._generate_bpmn_with_ai(process_name, context, model_type))
        else:
            model.update(self._generate_bpmn_basic(process_name, context, model_type))
        
        # Store model
        self.models[model["id"]] = model
        
        return model
    
    def generate_uml_model(
        self,
        diagram_type: ModelType,
        name: str,
        context: Dict[str, Any],
        use_ai: bool = True
    ) -> Dict[str, Any]:
        """
        Generate UML 2.0 diagram.
        
        Args:
            diagram_type: UML diagram type (class, sequence, use case, etc.)
            name: Diagram name
            context: Context information
            use_ai: Whether to use AI for intelligent generation
            
        Returns:
            UML model dictionary
        """
        model = {
            "id": f"uml_{diagram_type.value}_{name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": diagram_type.value,
            "name": name,
            "created": datetime.now().isoformat(),
            "elements": [],
            "relationships": [],
            "metadata": context
        }
        
        # Generate UML elements based on diagram type
        if diagram_type == ModelType.UML_CLASS:
            model["elements"] = self._generate_class_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_SEQUENCE:
            model["elements"] = self._generate_sequence_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_USE_CASE:
            model["elements"] = self._generate_use_case_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_ACTIVITY:
            model["elements"] = self._generate_activity_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_STATE_MACHINE:
            model["elements"] = self._generate_state_machine_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_COMPONENT:
            model["elements"] = self._generate_component_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_DEPLOYMENT:
            model["elements"] = self._generate_deployment_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_OBJECT:
            model["elements"] = self._generate_object_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_PACKAGE:
            model["elements"] = self._generate_package_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_TIMING:
            model["elements"] = self._generate_timing_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_COMMUNICATION:
            model["elements"] = self._generate_communication_diagram(context, use_ai)
        elif diagram_type == ModelType.UML_INTERACTION_OVERVIEW:
            model["elements"] = self._generate_interaction_overview_diagram(context, use_ai)
        
        # Store model
        self.models[model["id"]] = model
        
        return model
    
    def generate_multi_layer_model(
        self,
        layers: List[ArchitectureLayer],
        context: Dict[str, Any],
        use_ai: bool = True
    ) -> Dict[str, Any]:
        """
        Generate comprehensive multi-layer ArchiMate model.
        
        Args:
            layers: List of layers to include
            context: Context information
            use_ai: Whether to use AI for intelligent generation
            
        Returns:
            Multi-layer model dictionary
        """
        model = {
            "id": f"archimate_multi_layer_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": "archimate_multi_layer",
            "name": "Enterprise Architecture Model",
            "created": datetime.now().isoformat(),
            "layers": {},
            "cross_layer_relationships": [],
            "metadata": context
        }
        
        # Generate each layer
        for layer in layers:
            layer_model = self.generate_archimate_model(layer, context, use_ai)
            model["layers"][layer.value] = layer_model
        
        # Generate cross-layer relationships
        model["cross_layer_relationships"] = self._generate_cross_layer_relationships(
            model["layers"], use_ai
        )
        
        # Store model
        self.models[model["id"]] = model
        
        return model
    
    def get_model(self, model_id: str) -> Optional[Dict[str, Any]]:
        """Get a stored model by ID"""
        return self.models.get(model_id)
    
    def list_models(self) -> List[Dict[str, Any]]:
        """List all generated models"""
        return [
            {
                "id": model_id,
                "type": model["type"],
                "name": model["name"],
                "created": model["created"]
            }
            for model_id, model in self.models.items()
        ]
    
    # Private methods for element generation
    
    def _generate_strategy_elements(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate strategy layer elements (resources, capabilities, value streams)"""
        elements = []
        
        # Capabilities
        capabilities = context.get("capabilities", [
            "Digital Transformation",
            "Customer Experience Management",
            "Data Analytics",
            "Process Automation"
        ])
        
        for cap in capabilities:
            elements.append({
                "id": f"cap_{cap.lower().replace(' ', '_')}",
                "type": "capability",
                "name": cap,
                "description": f"Enterprise capability: {cap}"
            })
        
        # Goals
        goals = context.get("goals", [
            "Increase customer satisfaction by 30%",
            "Reduce operational costs by 25%",
            "Improve time-to-market by 50%"
        ])
        
        for i, goal in enumerate(goals):
            elements.append({
                "id": f"goal_{i+1}",
                "type": "goal",
                "name": f"Goal {i+1}",
                "description": goal
            })
        
        # Value streams
        value_streams = context.get("value_streams", [
            "Customer Acquisition",
            "Order Fulfillment",
            "Customer Support"
        ])
        
        for vs in value_streams:
            elements.append({
                "id": f"vs_{vs.lower().replace(' ', '_')}",
                "type": "value_stream",
                "name": vs,
                "description": f"Value stream: {vs}"
            })
        
        return elements
    
    def _generate_business_elements(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate business layer elements (actors, processes, services)"""
        elements = []
        
        # Business actors
        actors = context.get("actors", [
            "Customer",
            "Sales Representative",
            "Operations Manager",
            "IT Administrator"
        ])
        
        for actor in actors:
            elements.append({
                "id": f"actor_{actor.lower().replace(' ', '_')}",
                "type": "business_actor",
                "name": actor,
                "description": f"Business actor: {actor}"
            })
        
        # Business processes
        processes = context.get("processes", [
            "Lead Management",
            "Order Processing",
            "Customer Onboarding",
            "Service Delivery"
        ])
        
        for process in processes:
            elements.append({
                "id": f"process_{process.lower().replace(' ', '_')}",
                "type": "business_process",
                "name": process,
                "description": f"Business process: {process}"
            })
        
        # Business services
        services = context.get("services", [
            "Customer Portal",
            "Sales Support",
            "Order Tracking",
            "Help Desk"
        ])
        
        for service in services:
            elements.append({
                "id": f"service_{service.lower().replace(' ', '_')}",
                "type": "business_service",
                "name": service,
                "description": f"Business service: {service}"
            })
        
        return elements
    
    def _generate_application_elements(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate application layer elements (applications, services, interfaces)"""
        elements = []
        
        # Application components
        applications = context.get("applications", [
            "CRM System",
            "ERP System",
            "Customer Portal",
            "Analytics Platform",
            "Mobile App"
        ])
        
        for app in applications:
            elements.append({
                "id": f"app_{app.lower().replace(' ', '_')}",
                "type": "application_component",
                "name": app,
                "description": f"Application: {app}"
            })
        
        # Application services
        app_services = context.get("application_services", [
            "Customer Data Service",
            "Order Management Service",
            "Payment Processing Service",
            "Notification Service"
        ])
        
        for svc in app_services:
            elements.append({
                "id": f"app_svc_{svc.lower().replace(' ', '_')}",
                "type": "application_service",
                "name": svc,
                "description": f"Application service: {svc}"
            })
        
        # Data objects
        data_objects = context.get("data_objects", [
            "Customer",
            "Order",
            "Product",
            "Invoice"
        ])
        
        for obj in data_objects:
            elements.append({
                "id": f"data_{obj.lower()}",
                "type": "data_object",
                "name": obj,
                "description": f"Data object: {obj}"
            })
        
        return elements
    
    def _generate_technology_elements(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate technology layer elements (nodes, devices, networks)"""
        elements = []
        
        # Technology services
        tech_services = context.get("technology_services", [
            "Database Service",
            "API Gateway",
            "Message Queue",
            "Cache Service"
        ])
        
        for svc in tech_services:
            elements.append({
                "id": f"tech_svc_{svc.lower().replace(' ', '_')}",
                "type": "technology_service",
                "name": svc,
                "description": f"Technology service: {svc}"
            })
        
        # Nodes
        nodes = context.get("nodes", [
            "Web Server",
            "Application Server",
            "Database Server",
            "Message Broker"
        ])
        
        for node in nodes:
            elements.append({
                "id": f"node_{node.lower().replace(' ', '_')}",
                "type": "node",
                "name": node,
                "description": f"Technology node: {node}"
            })
        
        # System software
        software = context.get("system_software", [
            "Linux OS",
            "PostgreSQL",
            "Redis",
            "Kubernetes"
        ])
        
        for sw in software:
            elements.append({
                "id": f"sw_{sw.lower().replace(' ', '_')}",
                "type": "system_software",
                "name": sw,
                "description": f"System software: {sw}"
            })
        
        return elements
    
    def _generate_physical_elements(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate physical layer elements (equipment, facilities, networks)"""
        elements = []
        
        # Equipment
        equipment = context.get("equipment", [
            "Server Rack",
            "Network Switch",
            "Load Balancer",
            "Storage Array"
        ])
        
        for eq in equipment:
            elements.append({
                "id": f"equipment_{eq.lower().replace(' ', '_')}",
                "type": "equipment",
                "name": eq,
                "description": f"Physical equipment: {eq}"
            })
        
        # Facilities
        facilities = context.get("facilities", [
            "Primary Data Center",
            "Backup Data Center",
            "Office Location"
        ])
        
        for facility in facilities:
            elements.append({
                "id": f"facility_{facility.lower().replace(' ', '_')}",
                "type": "facility",
                "name": facility,
                "description": f"Facility: {facility}"
            })
        
        # Communication networks
        networks = context.get("networks", [
            "Corporate WAN",
            "Internet Connection",
            "VPN"
        ])
        
        for network in networks:
            elements.append({
                "id": f"network_{network.lower().replace(' ', '_')}",
                "type": "communication_network",
                "name": network,
                "description": f"Network: {network}"
            })
        
        return elements
    
    def _generate_implementation_elements(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate implementation layer elements (work packages, deliverables)"""
        elements = []
        
        # Work packages
        work_packages = context.get("work_packages", [
            "Phase 1: Foundation",
            "Phase 2: Core Systems",
            "Phase 3: Integration",
            "Phase 4: Optimization"
        ])
        
        for wp in work_packages:
            elements.append({
                "id": f"wp_{wp.lower().replace(' ', '_').replace(':', '')}",
                "type": "work_package",
                "name": wp,
                "description": f"Work package: {wp}"
            })
        
        # Deliverables
        deliverables = context.get("deliverables", [
            "Architecture Document",
            "Design Specifications",
            "Implementation Plan",
            "Test Results"
        ])
        
        for deliverable in deliverables:
            elements.append({
                "id": f"deliverable_{deliverable.lower().replace(' ', '_')}",
                "type": "deliverable",
                "name": deliverable,
                "description": f"Deliverable: {deliverable}"
            })
        
        return elements
    
    def _generate_relationships(self, elements: List[Dict[str, Any]], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate relationships between elements"""
        relationships = []
        
        # Generate basic relationships based on element types
        for i, elem1 in enumerate(elements):
            for elem2 in elements[i+1:]:
                # Create some logical relationships
                if self._should_relate(elem1, elem2):
                    relationships.append({
                        "id": f"rel_{elem1['id']}_{elem2['id']}",
                        "type": self._determine_relationship_type(elem1, elem2),
                        "source": elem1["id"],
                        "target": elem2["id"]
                    })
        
        return relationships
    
    def _should_relate(self, elem1: Dict[str, Any], elem2: Dict[str, Any]) -> bool:
        """Determine if two elements should be related"""
        # Simple heuristic: relate elements of complementary types
        complementary_pairs = [
            ("business_process", "business_service"),
            ("business_actor", "business_process"),
            ("application_component", "application_service"),
            ("application_service", "data_object"),
            ("node", "system_software"),
            ("capability", "business_process")
        ]
        
        elem1_type = elem1.get("type", "")
        elem2_type = elem2.get("type", "")
        
        return (elem1_type, elem2_type) in complementary_pairs or \
               (elem2_type, elem1_type) in complementary_pairs
    
    def _determine_relationship_type(self, elem1: Dict[str, Any], elem2: Dict[str, Any]) -> str:
        """Determine the type of relationship between elements"""
        type_map = {
            ("business_process", "business_service"): "realizes",
            ("business_actor", "business_process"): "assigned_to",
            ("application_component", "application_service"): "realizes",
            ("application_service", "data_object"): "accesses",
            ("node", "system_software"): "assigned_to",
            ("capability", "business_process"): "realizes"
        }
        
        elem1_type = elem1.get("type", "")
        elem2_type = elem2.get("type", "")
        
        return type_map.get((elem1_type, elem2_type), 
                          type_map.get((elem2_type, elem1_type), "associated_with"))
    
    def _generate_cross_layer_relationships(
        self,
        layers: Dict[str, Dict[str, Any]],
        use_ai: bool
    ) -> List[Dict[str, Any]]:
        """Generate relationships across architectural layers"""
        relationships = []
        
        # Business to Application
        if "business" in layers and "application" in layers:
            business_services = [e for e in layers["business"]["elements"] 
                               if e["type"] == "business_service"]
            app_services = [e for e in layers["application"]["elements"] 
                          if e["type"] == "application_service"]
            
            for bs in business_services[:2]:  # Limit for demo
                for apps in app_services[:2]:
                    relationships.append({
                        "id": f"rel_{bs['id']}_{apps['id']}",
                        "type": "serves",
                        "source": apps["id"],
                        "target": bs["id"],
                        "layer_source": "application",
                        "layer_target": "business"
                    })
        
        # Application to Technology
        if "application" in layers and "technology" in layers:
            app_components = [e for e in layers["application"]["elements"] 
                            if e["type"] == "application_component"]
            tech_nodes = [e for e in layers["technology"]["elements"] 
                        if e["type"] == "node"]
            
            for app in app_components[:2]:
                for node in tech_nodes[:2]:
                    relationships.append({
                        "id": f"rel_{app['id']}_{node['id']}",
                        "type": "assigned_to",
                        "source": app["id"],
                        "target": node["id"],
                        "layer_source": "application",
                        "layer_target": "technology"
                    })
        
        return relationships
    
    def _generate_bpmn_with_ai(
        self,
        process_name: str,
        context: Dict[str, Any],
        model_type: str
    ) -> Dict[str, Any]:
        """Generate BPMN model using AI"""
        # Placeholder for AI-generated BPMN
        return self._generate_bpmn_basic(process_name, context, model_type)
    
    def _generate_bpmn_basic(
        self,
        process_name: str,
        context: Dict[str, Any],
        model_type: str
    ) -> Dict[str, Any]:
        """Generate basic BPMN model"""
        return {
            "pools": [{"id": "pool_1", "name": process_name, "lanes": ["lane_1"]}],
            "lanes": [{"id": "lane_1", "name": "Main Process", "pool": "pool_1"}],
            "events": [
                {"id": "start_1", "type": "start", "name": "Start"},
                {"id": "end_1", "type": "end", "name": "End"}
            ],
            "tasks": [
                {"id": "task_1", "type": "task", "name": "Process Request", "lane": "lane_1"},
                {"id": "task_2", "type": "task", "name": "Validate Data", "lane": "lane_1"},
                {"id": "task_3", "type": "task", "name": "Complete Process", "lane": "lane_1"}
            ],
            "gateways": [
                {"id": "gateway_1", "type": "exclusive", "name": "Valid?"}
            ],
            "flows": [
                {"id": "flow_1", "source": "start_1", "target": "task_1"},
                {"id": "flow_2", "source": "task_1", "target": "task_2"},
                {"id": "flow_3", "source": "task_2", "target": "gateway_1"},
                {"id": "flow_4", "source": "gateway_1", "target": "task_3", "condition": "Yes"},
                {"id": "flow_5", "source": "gateway_1", "target": "task_1", "condition": "No"},
                {"id": "flow_6", "source": "task_3", "target": "end_1"}
            ]
        }
    
    # UML diagram generators
    
    def _generate_class_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML class diagram"""
        return [
            {
                "id": "class_customer",
                "type": "class",
                "name": "Customer",
                "attributes": ["id: string", "name: string", "email: string"],
                "methods": ["getOrders(): Order[]", "createOrder(order: Order): void"]
            },
            {
                "id": "class_order",
                "type": "class",
                "name": "Order",
                "attributes": ["id: string", "customerId: string", "total: number"],
                "methods": ["calculate(): number", "validate(): boolean"]
            },
            {
                "id": "class_product",
                "type": "class",
                "name": "Product",
                "attributes": ["id: string", "name: string", "price: number"],
                "methods": ["getDetails(): ProductDetails"]
            }
        ]
    
    def _generate_sequence_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML sequence diagram"""
        return [
            {"id": "actor_user", "type": "actor", "name": "User"},
            {"id": "obj_ui", "type": "object", "name": "UI", "class": "UserInterface"},
            {"id": "obj_controller", "type": "object", "name": "Controller", "class": "OrderController"},
            {"id": "obj_service", "type": "object", "name": "Service", "class": "OrderService"},
            {"id": "msg_1", "type": "message", "from": "actor_user", "to": "obj_ui", "message": "createOrder()"},
            {"id": "msg_2", "type": "message", "from": "obj_ui", "to": "obj_controller", "message": "processOrder()"},
            {"id": "msg_3", "type": "message", "from": "obj_controller", "to": "obj_service", "message": "saveOrder()"},
            {"id": "msg_4", "type": "return", "from": "obj_service", "to": "obj_controller", "message": "orderId"},
            {"id": "msg_5", "type": "return", "from": "obj_controller", "to": "obj_ui", "message": "success"},
            {"id": "msg_6", "type": "return", "from": "obj_ui", "to": "actor_user", "message": "confirmation"}
        ]
    
    def _generate_use_case_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML use case diagram"""
        return [
            {"id": "actor_customer", "type": "actor", "name": "Customer"},
            {"id": "actor_admin", "type": "actor", "name": "Administrator"},
            {"id": "uc_browse", "type": "use_case", "name": "Browse Products"},
            {"id": "uc_order", "type": "use_case", "name": "Place Order"},
            {"id": "uc_manage", "type": "use_case", "name": "Manage Products"},
            {"id": "uc_track", "type": "use_case", "name": "Track Order"}
        ]
    
    def _generate_activity_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML activity diagram"""
        return [
            {"id": "start", "type": "initial_node", "name": "Start"},
            {"id": "act_1", "type": "activity", "name": "Receive Request"},
            {"id": "act_2", "type": "activity", "name": "Validate Input"},
            {"id": "dec_1", "type": "decision_node", "name": "Valid?"},
            {"id": "act_3", "type": "activity", "name": "Process Request"},
            {"id": "act_4", "type": "activity", "name": "Send Error"},
            {"id": "end", "type": "final_node", "name": "End"}
        ]
    
    def _generate_state_machine_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML state machine diagram"""
        return [
            {"id": "state_new", "type": "state", "name": "New"},
            {"id": "state_processing", "type": "state", "name": "Processing"},
            {"id": "state_completed", "type": "state", "name": "Completed"},
            {"id": "state_cancelled", "type": "state", "name": "Cancelled"},
            {"id": "trans_1", "type": "transition", "from": "state_new", "to": "state_processing", "trigger": "submit"},
            {"id": "trans_2", "type": "transition", "from": "state_processing", "to": "state_completed", "trigger": "complete"},
            {"id": "trans_3", "type": "transition", "from": "state_processing", "to": "state_cancelled", "trigger": "cancel"}
        ]
    
    def _generate_component_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML component diagram"""
        return [
            {"id": "comp_ui", "type": "component", "name": "UI Component"},
            {"id": "comp_api", "type": "component", "name": "API Gateway"},
            {"id": "comp_service", "type": "component", "name": "Business Services"},
            {"id": "comp_data", "type": "component", "name": "Data Access Layer"}
        ]
    
    def _generate_deployment_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML deployment diagram"""
        return [
            {"id": "node_web", "type": "node", "name": "Web Server"},
            {"id": "node_app", "type": "node", "name": "Application Server"},
            {"id": "node_db", "type": "node", "name": "Database Server"},
            {"id": "artifact_ui", "type": "artifact", "name": "web.war", "deployed_on": "node_web"},
            {"id": "artifact_api", "type": "artifact", "name": "api.jar", "deployed_on": "node_app"}
        ]
    
    def _generate_object_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML object diagram"""
        return [
            {"id": "obj_customer1", "type": "object", "name": "customer1", "class": "Customer", 
             "attributes": {"id": "C001", "name": "John Doe"}},
            {"id": "obj_order1", "type": "object", "name": "order1", "class": "Order",
             "attributes": {"id": "O001", "customerId": "C001", "total": 150.00}}
        ]
    
    def _generate_package_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML package diagram"""
        return [
            {"id": "pkg_ui", "type": "package", "name": "ui"},
            {"id": "pkg_business", "type": "package", "name": "business"},
            {"id": "pkg_data", "type": "package", "name": "data"},
            {"id": "pkg_common", "type": "package", "name": "common"}
        ]
    
    def _generate_timing_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML timing diagram"""
        return [
            {"id": "lifeline_user", "type": "lifeline", "name": "User"},
            {"id": "lifeline_system", "type": "lifeline", "name": "System"},
            {"id": "state_1", "type": "state", "lifeline": "lifeline_system", "name": "Idle", "duration": 2},
            {"id": "state_2", "type": "state", "lifeline": "lifeline_system", "name": "Processing", "duration": 5},
            {"id": "state_3", "type": "state", "lifeline": "lifeline_system", "name": "Complete", "duration": 1}
        ]
    
    def _generate_communication_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML communication diagram"""
        return [
            {"id": "obj_client", "type": "object", "name": "client", "class": "Client"},
            {"id": "obj_server", "type": "object", "name": "server", "class": "Server"},
            {"id": "link_1", "type": "link", "from": "obj_client", "to": "obj_server"},
            {"id": "msg_1", "type": "message", "link": "link_1", "sequence": 1, "text": "request()"},
            {"id": "msg_2", "type": "message", "link": "link_1", "sequence": 2, "text": "response()"}
        ]
    
    def _generate_interaction_overview_diagram(self, context: Dict[str, Any], use_ai: bool) -> List[Dict[str, Any]]:
        """Generate UML interaction overview diagram"""
        return [
            {"id": "start", "type": "initial_node"},
            {"id": "interaction_1", "type": "interaction", "name": "User Login"},
            {"id": "interaction_2", "type": "interaction", "name": "Process Request"},
            {"id": "decision", "type": "decision_node"},
            {"id": "interaction_3", "type": "interaction", "name": "Handle Error"},
            {"id": "end", "type": "final_node"}
        ]
