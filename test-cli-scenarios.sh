#!/bin/bash
# ArchiAgents CLI - Real-World Business Scenarios
# End-to-End Testing Scripts

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print section headers
print_section() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_step() {
    echo -e "${GREEN}➜ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Set up Python environment
print_section "SETTING UP ENVIRONMENT"
print_step "Activating Python environment..."
cd "$(dirname "$0")"

# Add to Python path
export PYTHONPATH="${PWD}:${PWD}/togaf_framework:${PYTHONPATH}"

print_step "Environment ready!"

# Scenario 1: Digital Banking Transformation
print_section "SCENARIO 1: Digital Banking Transformation"
echo "Company: GlobalBank International"
echo "Challenge: Modernize legacy banking systems"
echo "Timeline: 18 months | Budget: \$15M"
echo ""

print_step "Step 1: Initialize project"
python -m togaf_framework.cli.main project init \
    --name "Digital Banking Modernization" \
    --enterprise "GlobalBank International" \
    --description "Complete digital transformation of retail banking platform" \
    --budget 15000000 \
    --timeline "18 months" \
    --output-format json

print_step "Step 2: Configure AI provider (using Ollama for FREE local inference)"
python -m togaf_framework.cli.main ai configure \
    --provider ollama \
    --model llama3.1 \
    --temperature 0.7

print_step "Step 3: Execute Phase A - Architecture Vision"
python -m togaf_framework.cli.main phase run phase-a \
    --project "Digital Banking Modernization" \
    --use-ai \
    --scope "Retail banking digital transformation" \
    --stakeholders "CEO, CTO, CFO, Head of Digital, Customers" \
    --objectives "50% cost reduction, 3x customer growth, 90% satisfaction"

print_step "Step 4: Generate stakeholder map"
python -m togaf_framework.cli.main model generate \
    --type archimate-motivation \
    --name "Stakeholder Value Map" \
    --description "Key stakeholders and their concerns" \
    --format mermaid

print_step "Step 5: Execute Phase B - Business Architecture"
python -m togaf_framework.cli.main phase run phase-b \
    --project "Digital Banking Modernization" \
    --use-ai \
    --capabilities "Mobile Banking, Digital Onboarding, AI-Powered Advisory" \
    --processes "Account Opening, Loan Processing, Customer Service"

print_step "Step 6: Generate business process model"
python -m togaf_framework.cli.main model generate \
    --type bpmn-process \
    --name "Digital Account Opening" \
    --description "End-to-end digital account opening process" \
    --format mermaid

print_step "Step 7: Execute Phase C - Information Systems Architecture"
python -m togaf_framework.cli.main phase run phase-c \
    --project "Digital Banking Modernization" \
    --applications "Mobile App, Web Portal, Core Banking, CRM" \
    --data-entities "Customer, Account, Transaction, Product"

print_step "Step 8: Generate application landscape"
python -m togaf_framework.cli.main model generate \
    --type archimate-application \
    --name "Application Architecture" \
    --description "Current and target application landscape" \
    --format mermaid

print_step "Step 9: Execute Phase D - Technology Architecture"
python -m togaf_framework.cli.main phase run phase-d \
    --project "Digital Banking Modernization" \
    --cloud-strategy "hybrid" \
    --platforms "AWS, Azure" \
    --technologies "Kubernetes, Microservices, API Gateway"

print_step "Step 10: Analyze architecture health"
python -m togaf_framework.cli.main intelligence health \
    --project "Digital Banking Modernization" \
    --analyze-gaps \
    --analyze-risks

print_step "Step 11: Execute Phase E - Opportunities & Solutions"
python -m togaf_framework.cli.main phase run phase-e \
    --project "Digital Banking Modernization" \
    --work-packages "Mobile App Development, Core Modernization, Data Migration" \
    --evaluate-options

print_step "Step 12: Execute Phase F - Migration Planning"
python -m togaf_framework.cli.main phase run phase-f \
    --project "Digital Banking Modernization" \
    --migration-strategy "phased" \
    --phases "3" \
    --duration "18 months"

print_step "Step 13: Generate comprehensive report"
python -m togaf_framework.cli.main report generate \
    --type comprehensive \
    --project "Digital Banking Modernization" \
    --format pdf \
    --include-diagrams \
    --include-metrics

print_step "Step 14: Validate architecture"
python -m togaf_framework.cli.main validate architecture \
    --standard togaf \
    --standard archimate \
    --project "Digital Banking Modernization"

print_step "Step 15: Export to Archi format"
python -m togaf_framework.cli.main export to-archi \
    --project "Digital Banking Modernization" \
    --output "./exports/digital-banking-archi.xml"

echo -e "\n${GREEN}✓ Digital Banking Transformation scenario completed!${NC}\n"

# Scenario 2: Cloud Migration - E-Commerce Platform
print_section "SCENARIO 2: E-Commerce Platform Cloud Migration"
echo "Company: TechRetail Corp"
echo "Challenge: Migrate on-premise infrastructure to cloud"
echo "Timeline: 12 months | Budget: \$8M"
echo ""

print_step "Step 1: Initialize cloud migration project"
python -m togaf_framework.cli.main project init \
    --name "E-Commerce Cloud Migration" \
    --enterprise "TechRetail Corp" \
    --description "Migrate legacy e-commerce platform to AWS" \
    --budget 8000000 \
    --timeline "12 months"

print_step "Step 2: Run pre-built cloud migration scenario"
python -m togaf_framework.cli.main scenario run cloud-migration \
    --enterprise "TechRetail Corp" \
    --source-environment "On-Premise Data Center" \
    --target-cloud "AWS" \
    --migration-strategy "lift-and-shift" \
    --workloads "Web Servers, Database, Cache, Storage"

print_step "Step 3: Generate technology architecture model"
python -m togaf_framework.cli.main model generate \
    --type archimate-technology \
    --name "Cloud Infrastructure Architecture" \
    --description "Target AWS infrastructure" \
    --format mermaid

print_step "Step 4: Analyze migration risks"
python -m togaf_framework.cli.main intelligence analyze \
    --project "E-Commerce Cloud Migration" \
    --analyze-risks \
    --analyze-dependencies \
    --recommend-solutions

print_step "Step 5: Generate migration roadmap"
python -m togaf_framework.cli.main model generate \
    --type archimate-implementation \
    --name "Cloud Migration Roadmap" \
    --description "Phased migration approach" \
    --format mermaid

print_step "Step 6: Validate cloud architecture"
python -m togaf_framework.cli.main validate quality \
    --project "E-Commerce Cloud Migration" \
    --check-consistency \
    --check-completeness

echo -e "\n${GREEN}✓ Cloud Migration scenario completed!${NC}\n"

# Scenario 3: Healthcare Digital Transformation (Saudi NORA Compliance)
print_section "SCENARIO 3: Healthcare Digital Transformation (Saudi NORA)"
echo "Company: HealthCare Plus (Saudi Arabia)"
echo "Challenge: Digital health platform with NORA compliance"
echo "Timeline: 24 months | Budget: \$20M"
echo ""

print_step "Step 1: Initialize healthcare project"
python -m togaf_framework.cli.main project init \
    --name "Digital Health Platform" \
    --enterprise "HealthCare Plus KSA" \
    --description "National health information exchange platform" \
    --budget 20000000 \
    --timeline "24 months" \
    --compliance "NORA, PDPL, HIPAA"

print_step "Step 2: Configure AI with Arabic language support"
python -m togaf_framework.cli.main ai configure \
    --provider openai \
    --model gpt-4 \
    --language ar \
    --region "Middle East"

print_step "Step 3: Execute Phase A with NORA compliance"
python -m togaf_framework.cli.main phase run phase-a \
    --project "Digital Health Platform" \
    --use-ai \
    --compliance-frameworks "NORA, PDPL" \
    --scope "National health information exchange" \
    --vision "Vision 2030 aligned digital health services"

print_step "Step 4: Generate NORA-compliant architecture"
python -m togaf_framework.cli.main model generate \
    --type archimate-strategy \
    --name "NORA Strategic Architecture" \
    --description "Saudi Digital Government Authority alignment" \
    --format mermaid

print_step "Step 5: Validate NORA compliance"
python -m togaf_framework.cli.main validate architecture \
    --standard nora \
    --project "Digital Health Platform" \
    --check-data-sovereignty \
    --check-arabic-support

print_step "Step 6: Generate compliance report"
python -m togaf_framework.cli.main report generate \
    --type compliance \
    --project "Digital Health Platform" \
    --standards "NORA, PDPL, HIPAA" \
    --format pdf

echo -e "\n${GREEN}✓ Healthcare Digital Transformation scenario completed!${NC}\n"

# Scenario 4: Microservices Modernization
print_section "SCENARIO 4: Monolith to Microservices Modernization"
echo "Company: FinTech Innovations"
echo "Challenge: Break down monolithic application"
echo "Timeline: 15 months | Budget: \$10M"
echo ""

print_step "Step 1: Initialize modernization project"
python -m togaf_framework.cli.main project init \
    --name "Microservices Modernization" \
    --enterprise "FinTech Innovations" \
    --description "Transform monolithic payment platform to microservices"

print_step "Step 2: AI-powered architecture analysis"
python -m togaf_framework.cli.main intelligence analyze \
    --project "Microservices Modernization" \
    --current-architecture "Monolithic Java application" \
    --target-architecture "Microservices on Kubernetes" \
    --recommend-decomposition

print_step "Step 3: Generate service decomposition model"
python -m togaf_framework.cli.main model generate \
    --type archimate-application \
    --name "Microservices Architecture" \
    --description "Decomposed service boundaries and APIs" \
    --format mermaid

print_step "Step 4: Generate API catalog"
python -m togaf_framework.cli.main model generate \
    --type uml-component \
    --name "API Gateway & Services" \
    --description "RESTful API specifications" \
    --format kroki

print_step "Step 5: Autonomous decision on migration strategy"
python -m togaf_framework.cli.main intelligence decide \
    --project "Microservices Modernization" \
    --decision-type "migration-strategy" \
    --options "Strangler Fig, Big Bang, Incremental" \
    --criteria "Risk, Cost, Time, Business Continuity"

echo -e "\n${GREEN}✓ Microservices Modernization scenario completed!${NC}\n"

# Scenario 5: IoT Smart City Platform
print_section "SCENARIO 5: Smart City IoT Platform"
echo "Company: Smart City Solutions"
echo "Challenge: City-wide IoT infrastructure"
echo "Timeline: 36 months | Budget: \$50M"
echo ""

print_step "Step 1: Initialize smart city project"
python -m togaf_framework.cli.main project init \
    --name "Smart City IoT Platform" \
    --enterprise "Smart City Solutions" \
    --description "Integrated IoT platform for urban management"

print_step "Step 2: Execute comprehensive TOGAF phases"
python -m togaf_framework.cli.main phase run phase-a \
    --project "Smart City IoT Platform" \
    --use-ai \
    --scope "Traffic, Energy, Waste, Public Safety" \
    --stakeholders "City Council, Citizens, Vendors, Operators"

python -m togaf_framework.cli.main phase run phase-b \
    --project "Smart City IoT Platform" \
    --capabilities "Real-time Monitoring, Predictive Analytics, Citizen Engagement"

python -m togaf_framework.cli.main phase run phase-c \
    --project "Smart City IoT Platform" \
    --applications "IoT Gateway, Analytics Engine, Citizen Portal, Control Center"

python -m togaf_framework.cli.main phase run phase-d \
    --project "Smart City IoT Platform" \
    --technologies "LoRaWAN, 5G, Edge Computing, Cloud Platform, AI/ML"

print_step "Step 3: Generate physical architecture"
python -m togaf_framework.cli.main model generate \
    --type archimate-physical \
    --name "IoT Infrastructure" \
    --description "Sensors, gateways, edge devices, data centers" \
    --format mermaid

print_step "Step 4: Generate data architecture"
python -m togaf_framework.cli.main model generate \
    --type archimate-data \
    --name "Smart City Data Architecture" \
    --description "Real-time data flows and storage" \
    --format mermaid

print_step "Step 5: Compare baseline vs target architecture"
python -m togaf_framework.cli.main report compare-architectures \
    --project "Smart City IoT Platform" \
    --baseline "Current City Systems" \
    --target "Integrated IoT Platform" \
    --dimensions "Cost, Performance, Scalability, Citizen Satisfaction"

echo -e "\n${GREEN}✓ Smart City IoT Platform scenario completed!${NC}\n"

# Scenario 6: Rapid AI Integration
print_section "SCENARIO 6: AI-Driven Decision Making (Autonomous Mode)"
echo "Scenario: AI agents make architecture decisions autonomously"
echo ""

print_step "Step 1: Test multi-provider AI capabilities"
python -m togaf_framework.cli.main ai list-models

print_step "Step 2: Configure multiple AI providers"
python -m togaf_framework.cli.main ai configure --provider openai --model gpt-4o
python -m togaf_framework.cli.main ai configure --provider anthropic --model claude-3-5-sonnet
python -m togaf_framework.cli.main ai configure --provider google --model gemini-pro

print_step "Step 3: Test AI agent collaboration"
python -m togaf_framework.cli.main ai run-task \
    --task "Design microservices architecture for real-time payment system" \
    --agents "solution-architect, security-architect, data-architect" \
    --collaboration-mode "debate"

print_step "Step 4: Autonomous architecture generation"
python -m togaf_framework.cli.main intelligence decide \
    --decision-type "architecture-pattern" \
    --context "High-traffic e-commerce platform, 10M users, global presence" \
    --autonomous-mode \
    --confidence-threshold 0.85

echo -e "\n${GREEN}✓ AI-Driven Decision Making scenario completed!${NC}\n"

# Scenario 7: Import/Export Interoperability
print_section "SCENARIO 7: Tool Interoperability"
echo "Scenario: Import from Archi, modify, export to multiple formats"
echo ""

print_step "Step 1: Import existing architecture from Archi"
python -m togaf_framework.cli.main import from-archi \
    --file "./sample-data/existing-architecture.xml" \
    --project "Legacy System Architecture"

print_step "Step 2: Validate imported architecture"
python -m togaf_framework.cli.main validate completeness \
    --project "Legacy System Architecture" \
    --check-relationships \
    --check-views

print_step "Step 3: Enhance with AI analysis"
python -m togaf_framework.cli.main intelligence analyze \
    --project "Legacy System Architecture" \
    --identify-gaps \
    --recommend-improvements

print_step "Step 4: Export to multiple formats"
python -m togaf_framework.cli.main export batch \
    --project "Legacy System Architecture" \
    --formats "archi,mermaid,gojs,ea" \
    --output-dir "./exports/multi-format"

echo -e "\n${GREEN}✓ Tool Interoperability scenario completed!${NC}\n"

# Summary
print_section "TEST SCENARIOS SUMMARY"
echo "✓ Scenario 1: Digital Banking Transformation - COMPLETE"
echo "✓ Scenario 2: E-Commerce Cloud Migration - COMPLETE"
echo "✓ Scenario 3: Healthcare Digital (NORA) - COMPLETE"
echo "✓ Scenario 4: Microservices Modernization - COMPLETE"
echo "✓ Scenario 5: Smart City IoT Platform - COMPLETE"
echo "✓ Scenario 6: AI-Driven Decision Making - COMPLETE"
echo "✓ Scenario 7: Tool Interoperability - COMPLETE"
echo ""
echo -e "${GREEN}All 7 real-world business scenarios executed successfully!${NC}"
echo ""
echo "Generated artifacts:"
echo "  - Architecture models (ArchiMate, BPMN, UML)"
echo "  - Comprehensive reports (PDF, HTML)"
echo "  - Diagrams (Mermaid, Kroki)"
echo "  - Export files (Archi, Enterprise Architect, GoJS)"
echo "  - Compliance reports (TOGAF, NORA)"
echo ""
echo "Next steps:"
echo "  1. Review generated models in ./models/"
echo "  2. Check reports in ./reports/"
echo "  3. Validate exports in ./exports/"
echo "  4. Review AI agent logs in ./logs/"
