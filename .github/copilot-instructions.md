# Copilot Instructions for Enterprise Architecture Project

## Project Overview
This is a comprehensive Enterprise Architecture project implementing **TOGAF 10 ADM methodology**, **ArchiMate 3.2 modeling standards**, and **Saudi National Overall Reference Architecture (NORA)** compliance. The project delivers a complete EA blueprint supporting digital transformation and Vision 2030 strategic objectives.

## Architecture Framework & Structure

### TOGAF 8-Phase Implementation
The project follows TOGAF ADM phases organized as:
- `Phase-A-Architecture-Vision/` - Strategic direction and stakeholder alignment
- `Phase-B-Business-Architecture/` - Process optimization and organizational design  
- `Phase-C-Information-Systems/` - Application and data architecture
- `Phase-D-Technology-Architecture/` - Cloud infrastructure and platform strategy
- `Phase-E-Opportunities-Solutions/` - Solution alternatives and recommendations
- `Phase-F-Migration-Planning/` - Detailed transformation roadmap
- `Phase-G-Implementation-Governance/` - Project oversight and compliance
- `Phase-H-Architecture-Change-Management/` - Continuous architecture evolution

### ArchiMate Layer Structure
Models are organized by architectural layers in `ArchiMate-Models/`:
- **Strategy Layer** - Goals, capabilities, value streams
- **Business Layer** - Processes, functions, services
- **Application Layer** - Microservices, APIs, data flows
- **Technology Layer** - Cloud infrastructure, security, DevOps
- **Physical Layer** - Data centers, network, IoT, edge computing
- **Implementation Layer** - Current/target state, transformation roadmaps

## Key Patterns & Conventions

### Documentation Structure
- Each phase contains `Strategic-Deliverables/` and `Governance-Deliverables/` subdirectories
- Documents follow standardized templates from `Templates/` directory
- All diagrams use Mermaid syntax with consistent styling classes
- Cross-references between documents use relative paths

### Mermaid Diagram Standards
Use predefined CSS classes from `Templates/Mermaid-Diagram-Templates.md`:
```
classDef startEnd fill:#90EE90
classDef decision fill:#FFE4B5  
classDef process fill:#87CEEB
classDef exception fill:#FFB6C1
```

### Cross-Cutting Concerns
Enterprise-wide frameworks in `Cross-Cutting-Concerns/`:
- `Governance-Frameworks.md` - Decision rights, accountability structures
- `Integration-Patterns.md` - API management, event-driven architecture
- `Security-Patterns.md` - Zero-trust architecture, identity management
- `Performance-Monitoring-Framework.md` - Observability, metrics, SLA management

### Performance Targets (Key Metrics)
- System Availability: 99.9% (target from current 99.5%)
- API Response Time: <100ms (target from current 200ms)
- Process Automation: 70% (target from current 45%)
- Data Processing: 10M events/hour (target from current 1M)

## Technology Stack & Architecture Decisions

### Primary Platforms
- **Primary Cloud**: Microsoft Azure (multi-region)
- **Secondary Cloud**: AWS (resilience and specialized services)
- **Monitoring**: Prometheus/Grafana, ELK Stack, Jaeger tracing
- **Security**: Zero Trust, SSO, RBAC

### Architecture Patterns
- Microservices with domain-driven design
- API-First (RESTful and GraphQL)
- Event-driven architecture for real-time processing
- Cloud-native with serverless and container orchestration

## Governance & Compliance Requirements

### Decision Framework
Reference `Cross-Cutting-Concerns/Governance-Frameworks.md` for:
- Three-tier governance: Executive → Operational → Working Groups
- Architecture Board composition and responsibilities
- Change Advisory Board (CAB) approval processes

### Compliance Standards
- **TOGAF 10** - Architecture Development Method compliance
- **ArchiMate 3.2** - Modeling language standards
- **Saudi NORA** - National architecture requirements
- **ISO 27001, SOC 2, GDPR, PCI DSS** - Security and privacy standards

## Working with This Codebase

### When Adding New Documents
1. Use appropriate template from `Templates/` directory
2. Follow TOGAF phase-specific folder structure
3. Include required governance sections and compliance mappings
4. Add Mermaid diagrams using standardized CSS classes
5. Update parent README files with navigation links

### When Modifying Architecture Models
1. Maintain ArchiMate 3.2 layer consistency
2. Ensure cross-layer traceability and relationships
3. Update both current-state and target-state models
4. Document architecture decisions and rationale

### Integration Points
- All integration patterns documented in `Cross-Cutting-Concerns/Integration-Patterns.md`
- API standards and governance in Phase-C Information Systems
- Security patterns apply across all architectural layers
- Performance monitoring framework spans all technology components

This is a formal enterprise architecture repository requiring adherence to established frameworks, standards, and governance processes.