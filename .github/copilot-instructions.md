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
- **Saudi NORA** - National architecture requirements (see detailed section below)
- **ISO 27001, SOC 2, GDPR, PCI DSS** - Security and privacy standards

## Saudi NORA-Specific Requirements

### Vision 2030 Digital Government Targets
- 90% of government services digital by 2030
- 80% citizen satisfaction with digital services
- 100% government entities on unified platform
- 95% automated government processes
- Top 5 global ranking in digital government maturity

### Mandatory Compliance Patterns

#### Arabic-First Design Requirements
- All interfaces must prioritize Arabic language (RTL design)
- Arabic natural language processing for document handling
- Cultural considerations in UX/UI design patterns
- WCAG 2.1 AA + Saudi accessibility standards compliance

#### Data Sovereignty & PDPL Compliance
- **Data Localization**: Personal data must be stored within Saudi Arabia
- **Consent Management**: Explicit consent for all personal data collection
- **Data Minimization**: Collect only necessary data for specified purposes
- **Breach Notification**: 72-hour reporting requirement to authorities
- **Individual Rights**: Access, correction, deletion, and portability rights

#### Government Platform Integration
- **Absher Platform**: Integration with unified government services
- **National Single Sign-On (NSSO)**: Mandatory for government applications
- **DGA API Standards**: Compliance with Digital Government Authority APIs
- **Government Service Bus**: Connectivity for cross-entity communication

### Performance & Service Standards
- Response Time: <3 seconds for simple transactions
- Availability: 99.9% uptime for citizen services
- Mobile-First: All services must be mobile-responsive
- Multi-Modal: Support for web, mobile, and emerging channels

### National Cybersecurity Framework
- Essential Cybersecurity Controls (ECC) implementation
- National Cybersecurity Authority (NCA) compliance
- Threat intelligence sharing with government entities
- Incident response coordination with national CERT

### Documentation Requirements
Reference `NORA-Compliance/` directory for:
- `Saudi-NORA-Framework-Implementation-Guide.md` - Detailed implementation patterns
- `NORA-Compliance-Assessment-Report.md` - Current compliance status and gaps

## Working with This Codebase

### When Adding New Documents
1. Use appropriate template from `Templates/` directory
2. Follow TOGAF phase-specific folder structure
3. Include required governance sections and compliance mappings
4. Add Mermaid diagrams using standardized CSS classes
5. Update parent README files with navigation links
6. **NORA Compliance**: Include Saudi DGA standards alignment section
7. **Arabic Language**: Ensure Arabic language considerations are documented

### When Modifying Architecture Models
1. Maintain ArchiMate 3.2 layer consistency
2. Ensure cross-layer traceability and relationships
3. Update both current-state and target-state models
4. Document architecture decisions and rationale
5. **NORA Assessment**: Evaluate against Saudi government standards
6. **Data Sovereignty**: Verify data localization requirements compliance

### Saudi NORA Working Patterns
- Include Vision 2030 alignment in strategic documents
- Document Arabic-first design decisions in UX/UI specifications
- Map compliance levels (1-4) for each NORA domain in assessments
- Reference DGA standards in all government-facing architecture decisions
- Include cybersecurity controls mapping to NCA framework

### Integration Points
- All integration patterns documented in `Cross-Cutting-Concerns/Integration-Patterns.md`
- API standards and governance in Phase-C Information Systems
- Security patterns apply across all architectural layers
- Performance monitoring framework spans all technology components

This is a formal enterprise architecture repository requiring adherence to established frameworks, standards, and governance processes.