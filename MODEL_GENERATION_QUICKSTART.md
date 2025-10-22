# Model Generation Quick Start Guide

## 📊 ArchiAgents Model Generation System

The ArchiAgents Model Generation System provides AI-powered creation of enterprise architecture models with support for **21 model types** across **3 standards** (ArchiMate 3.0, BPMN 2.0, UML 2.0) and export to **6 different formats** (Text, Mermaid, Kroki, Archi, GoJS, Enterprise Architect).

## Quick Examples

### Generate ArchiMate Business Layer Model

```bash
archiagents model generate \
  --type archimate-business \
  --name "Customer Management" \
  --format mermaid archi ea \
  --use-ai
```

**Output:**
- `models/customer-management/model.json` - Core model data
- `models/customer-management/customer-management.md` - Markdown documentation
- `models/customer-management/customer-management.mermaid` - Mermaid diagram
- `models/customer-management/customer-management.archi` - Archi tool XML
- `models/customer-management/customer-management.xmi` - Enterprise Architect XMI

### Generate BPMN Process Model

```bash
archiagents model generate \
  --type bpmn-process \
  --name "Order Fulfillment" \
  --format mermaid kroki \
  --use-ai
```

**Generates:**
- Complete BPMN process with pools, lanes, tasks, events, gateways
- Mermaid flowchart syntax
- PlantUML format for Kroki rendering

### Generate UML Class Diagram

```bash
archiagents model generate \
  --type uml-class \
  --name "Domain Model" \
  --format mermaid ea gojs \
  --use-ai
```

**Creates:**
- Full class diagram with attributes and methods
- Mermaid class diagram syntax
- Enterprise Architect XMI format
- GoJS interactive web visualization JSON

### Generate Complete Multi-Layer Enterprise Model

```bash
archiagents model generate \
  --type archimate-multi-layer \
  --name "Enterprise Architecture" \
  --format text mermaid archi ea \
  --use-ai
```

**Produces:**
- Strategy, Business, Application, Technology, Physical, Implementation layers
- Cross-layer relationships and traceability
- Complete documentation in all formats

## Model Management

### List All Generated Models

```bash
# Table format (default)
archiagents model list --format table

# JSON format
archiagents model list --format json

# Tree structure
archiagents model list --format tree
```

### Validate Model Compliance

```bash
# Validate against ArchiMate and TOGAF standards
archiagents model validate <model-id> --standards archimate togaf

# UML validation
archiagents model validate <model-id> --standards uml
```

**Output:**
- Compliance score (0-100)
- Issues with severity levels (error, warning, info)
- Fix suggestions for each issue

### Export to Different Format

```bash
# Export to Enterprise Architect XMI
archiagents model export <model-id> --format ea --output model.xmi

# Export to Archi XML
archiagents model export <model-id> --format archi --output model.archi

# Export to Mermaid
archiagents model export <model-id> --format mermaid
```

### Get AI Improvement Suggestions

```bash
archiagents model improve <model-id>
```

**Analyzes:**
- Model completeness
- Relationship quality
- Best practices adherence
- Naming conventions
- Structural optimization

## Supported Model Types

### ArchiMate 3.0 (7 types)
- `archimate-strategy` - Strategy layer (capabilities, goals, value streams)
- `archimate-business` - Business layer (processes, functions, services)
- `archimate-application` - Application layer (components, services, data)
- `archimate-technology` - Technology layer (nodes, devices, software)
- `archimate-physical` - Physical layer (equipment, facilities, networks)
- `archimate-implementation` - Implementation layer (work packages, deliverables)
- `archimate-multi-layer` - Complete multi-layer enterprise model

### BPMN 2.0 (3 types)
- `bpmn-process` - Process model with pools, lanes, tasks
- `bpmn-collaboration` - Collaboration between multiple participants
- `bpmn-choreography` - Message choreography between participants

### UML 2.0 (12 types)
- `uml-class` - Class diagram
- `uml-sequence` - Sequence diagram
- `uml-use-case` - Use case diagram
- `uml-activity` - Activity diagram
- `uml-state-machine` - State machine diagram
- `uml-component` - Component diagram
- `uml-deployment` - Deployment diagram
- `uml-object` - Object diagram
- `uml-package` - Package diagram
- `uml-timing` - Timing diagram
- `uml-communication` - Communication diagram
- `uml-interaction-overview` - Interaction overview diagram

## Output Formats

1. **text** - Markdown documentation with full details
2. **mermaid** - GitHub/GitLab compatible diagrams
3. **kroki** - PlantUML for Kroki rendering service
4. **archi** - Archi tool XML format (import via File → Open → Exchange File)
5. **gojs** - GoJS JSON for interactive web visualization
6. **ea** - Sparx Enterprise Architect XMI format (import via Project → Import/Export → Import Package from XMI)

## Enterprise Architect Integration

### Export Model to EA

```bash
archiagents model generate \
  --type uml-class \
  --name "System Architecture" \
  --format ea \
  --use-ai
```

### Import into Enterprise Architect

1. Open Sparx Enterprise Architect
2. Navigate to **Project → Import/Export → Import Package from XMI**
3. Select the generated `.xmi` file
4. Choose import options
5. Click **Import**

## Archi Tool Integration

### Export Model to Archi

```bash
archiagents model generate \
  --type archimate-business \
  --name "Business Model" \
  --format archi \
  --use-ai
```

### Import into Archi

1. Open Archi tool
2. Navigate to **File → Open → Exchange File**
3. Select the generated `.archi` file
4. Model loads with complete structure and relationships

## AI-Powered Generation

### Enable AI Generation (Recommended)

```bash
archiagents model generate \
  --type archimate-application \
  --name "Microservices Architecture" \
  --format mermaid archi ea \
  --use-ai  # Uses LLM for intelligent generation
```

**AI Capabilities:**
- Context-aware element creation from TOGAF phases
- Intelligent relationship generation
- Pattern recognition and application
- Best practices enforcement
- Standards compliance validation

### Template-Based Generation (No AI)

```bash
archiagents model generate \
  --type bpmn-process \
  --name "Standard Process" \
  --format mermaid \
  --no-ai  # Uses predefined templates
```

## Complete Workflows

### TOGAF Phase B: Business Architecture

```bash
# Generate business capability model
archiagents model generate \
  --type archimate-strategy \
  --name "Business Capabilities" \
  --format mermaid archi \
  --use-ai

# Generate business process model
archiagents model generate \
  --type bpmn-process \
  --name "Core Processes" \
  --format mermaid kroki \
  --use-ai

# Generate business layer architecture
archiagents model generate \
  --type archimate-business \
  --name "Business Architecture" \
  --format mermaid archi ea \
  --use-ai

# Validate all models
archiagents model list
archiagents model validate <model-id> --standards archimate togaf
```

### Software Design Documentation

```bash
# Generate domain model
archiagents model generate \
  --type uml-class \
  --name "Domain Model" \
  --format mermaid ea \
  --use-ai

# Generate sequence diagrams
archiagents model generate \
  --type uml-sequence \
  --name "User Authentication Flow" \
  --format mermaid ea \
  --use-ai

# Generate component architecture
archiagents model generate \
  --type uml-component \
  --name "System Components" \
  --format mermaid ea gojs \
  --use-ai

# Generate deployment architecture
archiagents model generate \
  --type uml-deployment \
  --name "Production Deployment" \
  --format mermaid ea \
  --use-ai
```

### Complete Enterprise Architecture

```bash
# Generate complete multi-layer model
archiagents model generate \
  --type archimate-multi-layer \
  --name "Enterprise Architecture 2024" \
  --format text mermaid archi ea \
  --use-ai \
  --output-dir ./enterprise-models

# Validate compliance
archiagents model validate <model-id> --standards archimate togaf

# Get improvement suggestions
archiagents model improve <model-id>

# Export to Enterprise Architect for detailed work
archiagents model export <model-id> --format ea --output EA-Import.xmi
```

## Benefits

- **10x Faster:** Generate complete models in minutes vs. days of manual work
- **AI-Powered:** Intelligent generation based on enterprise context and best practices
- **Standards Compliant:** ArchiMate 3.0, TOGAF 10, UML 2.0, BPMN 2.0
- **Multi-Format:** Single generation, multiple output formats
- **Tool Integration:** Direct import into Enterprise Architect and Archi
- **Quality Assured:** Validation and improvement suggestions built-in
- **Documentation:** Complete Markdown documentation auto-generated

## Next Steps

For complete documentation with 30+ examples:
- See [`MODEL_GENERATION_GUIDE.md`](MODEL_GENERATION_GUIDE.md)
- Run example scripts: `bash model_examples.sh`

For implementation details:
- See [`MODEL_GENERATION_IMPLEMENTATION_SUMMARY.md`](MODEL_GENERATION_IMPLEMENTATION_SUMMARY.md)

---

**ArchiAgents - Enterprise Architecture Made Intelligent** 🚀
