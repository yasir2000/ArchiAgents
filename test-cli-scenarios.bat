@echo off
REM ArchiAgents CLI - Real-World Business Scenarios
REM Windows PowerShell/CMD Version

setlocal enabledelayedexpansion

REM Colors for output (Windows 10+)
set "GREEN=[92m"
set "BLUE=[94m"
set "YELLOW=[93m"
set "RED=[91m"
set "NC=[0m"

echo.
echo %BLUE%========================================%NC%
echo %BLUE%ArchiAgents CLI - Real-World Test Scenarios%NC%
echo %BLUE%========================================%NC%
echo.

REM Set up Python environment
echo %GREEN%Setting up environment...%NC%
cd /d "%~dp0"
set PYTHONPATH=%CD%;%CD%\togaf_framework;%PYTHONPATH%

echo %GREEN%Environment ready!%NC%
echo.

REM ============================================================
REM SCENARIO 1: Digital Banking Transformation
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 1: Digital Banking Transformation%NC%
echo %BLUE%========================================%NC%
echo Company: GlobalBank International
echo Challenge: Modernize legacy banking systems
echo Timeline: 18 months ^| Budget: $15M
echo.

echo %GREEN%Step 1: Initialize project%NC%
python -m togaf_framework.cli.main project init --name "Digital Banking Modernization" --enterprise "GlobalBank International" --description "Complete digital transformation" --budget 15000000 --timeline "18 months"

echo %GREEN%Step 2: Configure AI (Ollama - FREE local)%NC%
python -m togaf_framework.cli.main ai configure --provider ollama --model llama3.1

echo %GREEN%Step 3: Execute Phase A - Architecture Vision%NC%
python -m togaf_framework.cli.main phase run phase-a --project "Digital Banking Modernization" --use-ai

echo %GREEN%Step 4: Generate stakeholder map%NC%
python -m togaf_framework.cli.main model generate --type archimate-motivation --name "Stakeholder Map" --format mermaid

echo %GREEN%Step 5: Execute Phase B - Business Architecture%NC%
python -m togaf_framework.cli.main phase run phase-b --project "Digital Banking Modernization"

echo %GREEN%Step 6: Generate business process model%NC%
python -m togaf_framework.cli.main model generate --type bpmn-process --name "Digital Account Opening" --format mermaid

echo %GREEN%Step 7: Execute Phase C - Information Systems%NC%
python -m togaf_framework.cli.main phase run phase-c --project "Digital Banking Modernization"

echo %GREEN%Step 8: Generate application landscape%NC%
python -m togaf_framework.cli.main model generate --type archimate-application --name "App Architecture" --format mermaid

echo %GREEN%Step 9: Execute Phase D - Technology%NC%
python -m togaf_framework.cli.main phase run phase-d --project "Digital Banking Modernization"

echo %GREEN%Step 10: Analyze architecture health%NC%
python -m togaf_framework.cli.main intelligence health --project "Digital Banking Modernization"

echo %GREEN%Step 11: Execute Phase E - Opportunities%NC%
python -m togaf_framework.cli.main phase run phase-e --project "Digital Banking Modernization"

echo %GREEN%Step 12: Execute Phase F - Migration Planning%NC%
python -m togaf_framework.cli.main phase run phase-f --project "Digital Banking Modernization"

echo %GREEN%Step 13: Generate comprehensive report%NC%
python -m togaf_framework.cli.main report generate --type comprehensive --project "Digital Banking Modernization" --format pdf

echo %GREEN%Step 14: Validate architecture%NC%
python -m togaf_framework.cli.main validate architecture --standard togaf --project "Digital Banking Modernization"

echo.
echo %GREEN%Digital Banking Transformation - COMPLETE!%NC%
echo.

REM ============================================================
REM SCENARIO 2: Cloud Migration
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 2: E-Commerce Cloud Migration%NC%
echo %BLUE%========================================%NC%
echo Company: TechRetail Corp
echo Challenge: Migrate to AWS
echo.

echo %GREEN%Step 1: Initialize project%NC%
python -m togaf_framework.cli.main project init --name "E-Commerce Cloud Migration" --enterprise "TechRetail Corp"

echo %GREEN%Step 2: Run cloud migration scenario%NC%
python -m togaf_framework.cli.main scenario run cloud-migration --enterprise "TechRetail Corp" --target-cloud "AWS"

echo %GREEN%Step 3: Generate cloud architecture%NC%
python -m togaf_framework.cli.main model generate --type archimate-technology --name "AWS Infrastructure" --format mermaid

echo %GREEN%Step 4: Analyze risks%NC%
python -m togaf_framework.cli.main intelligence analyze --project "E-Commerce Cloud Migration" --analyze-risks

echo.
echo %GREEN%Cloud Migration - COMPLETE!%NC%
echo.

REM ============================================================
REM SCENARIO 3: Healthcare NORA Compliance
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 3: Healthcare (Saudi NORA)%NC%
echo %BLUE%========================================%NC%
echo Company: HealthCare Plus KSA
echo Compliance: NORA, PDPL
echo.

echo %GREEN%Step 1: Initialize healthcare project%NC%
python -m togaf_framework.cli.main project init --name "Digital Health Platform" --enterprise "HealthCare Plus KSA" --compliance "NORA,PDPL"

echo %GREEN%Step 2: Execute with NORA compliance%NC%
python -m togaf_framework.cli.main phase run phase-a --project "Digital Health Platform" --compliance-frameworks "NORA,PDPL"

echo %GREEN%Step 3: Validate NORA compliance%NC%
python -m togaf_framework.cli.main validate architecture --standard nora --project "Digital Health Platform"

echo %GREEN%Step 4: Generate compliance report%NC%
python -m togaf_framework.cli.main report generate --type compliance --project "Digital Health Platform" --standards "NORA,PDPL"

echo.
echo %GREEN%Healthcare NORA - COMPLETE!%NC%
echo.

REM ============================================================
REM SCENARIO 4: Microservices Modernization
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 4: Microservices Modernization%NC%
echo %BLUE%========================================%NC%
echo Company: FinTech Innovations
echo Challenge: Monolith to Microservices
echo.

echo %GREEN%Step 1: Initialize project%NC%
python -m togaf_framework.cli.main project init --name "Microservices Modernization" --enterprise "FinTech Innovations"

echo %GREEN%Step 2: AI analysis%NC%
python -m togaf_framework.cli.main intelligence analyze --project "Microservices Modernization" --recommend-decomposition

echo %GREEN%Step 3: Generate microservices model%NC%
python -m togaf_framework.cli.main model generate --type archimate-application --name "Microservices" --format mermaid

echo %GREEN%Step 4: Autonomous decision%NC%
python -m togaf_framework.cli.main intelligence decide --decision-type "migration-strategy"

echo.
echo %GREEN%Microservices Modernization - COMPLETE!%NC%
echo.

REM ============================================================
REM SCENARIO 5: Smart City IoT
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 5: Smart City IoT Platform%NC%
echo %BLUE%========================================%NC%
echo Company: Smart City Solutions
echo Scale: City-wide IoT
echo.

echo %GREEN%Step 1: Initialize smart city%NC%
python -m togaf_framework.cli.main project init --name "Smart City IoT" --enterprise "Smart City Solutions"

echo %GREEN%Step 2: Execute all phases%NC%
python -m togaf_framework.cli.main phase run phase-a --project "Smart City IoT"
python -m togaf_framework.cli.main phase run phase-b --project "Smart City IoT"
python -m togaf_framework.cli.main phase run phase-c --project "Smart City IoT"
python -m togaf_framework.cli.main phase run phase-d --project "Smart City IoT"

echo %GREEN%Step 3: Generate IoT architecture%NC%
python -m togaf_framework.cli.main model generate --type archimate-physical --name "IoT Infrastructure" --format mermaid

echo %GREEN%Step 4: Compare architectures%NC%
python -m togaf_framework.cli.main report compare-architectures --project "Smart City IoT"

echo.
echo %GREEN%Smart City IoT - COMPLETE!%NC%
echo.

REM ============================================================
REM SCENARIO 6: AI-Driven Decisions
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 6: AI-Driven Decision Making%NC%
echo %BLUE%========================================%NC%
echo.

echo %GREEN%Step 1: List AI models%NC%
python -m togaf_framework.cli.main ai list-models

echo %GREEN%Step 2: Configure providers%NC%
python -m togaf_framework.cli.main ai configure --provider openai --model gpt-4o

echo %GREEN%Step 3: AI agent collaboration%NC%
python -m togaf_framework.cli.main ai run-task --task "Design payment microservices" --agents "solution-architect,security-architect"

echo %GREEN%Step 4: Autonomous decisions%NC%
python -m togaf_framework.cli.main intelligence decide --decision-type "architecture-pattern" --autonomous-mode

echo.
echo %GREEN%AI Decision Making - COMPLETE!%NC%
echo.

REM ============================================================
REM SCENARIO 7: Interoperability
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%SCENARIO 7: Tool Interoperability%NC%
echo %BLUE%========================================%NC%
echo.

echo %GREEN%Step 1: Import from Archi%NC%
python -m togaf_framework.cli.main import from-archi --file "sample.xml" --project "Legacy"

echo %GREEN%Step 2: Validate%NC%
python -m togaf_framework.cli.main validate completeness --project "Legacy"

echo %GREEN%Step 3: Export to multiple formats%NC%
python -m togaf_framework.cli.main export batch --project "Legacy" --formats "archi,mermaid,gojs"

echo.
echo %GREEN%Tool Interoperability - COMPLETE!%NC%
echo.

REM ============================================================
REM Summary
REM ============================================================
echo.
echo %BLUE%========================================%NC%
echo %BLUE%TEST SCENARIOS SUMMARY%NC%
echo %BLUE%========================================%NC%
echo.
echo %GREEN%All 7 real-world scenarios executed!%NC%
echo.
echo Scenarios completed:
echo   1. Digital Banking Transformation
echo   2. E-Commerce Cloud Migration
echo   3. Healthcare NORA Compliance
echo   4. Microservices Modernization
echo   5. Smart City IoT Platform
echo   6. AI-Driven Decision Making
echo   7. Tool Interoperability
echo.
echo Generated artifacts in:
echo   - ./models/
echo   - ./reports/
echo   - ./exports/
echo   - ./logs/
echo.
pause
