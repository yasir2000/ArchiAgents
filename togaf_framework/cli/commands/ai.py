"""
AI Agent Configuration and Management Commands

Provides commands for configuring and running AI agents with multiple LLM providers.
"""
import click
import os
import json
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from cli.config import ProjectConfig
from cli.utils import ConsoleColors, OutputFormatter


@click.command(name='configure')
@click.option('--provider', type=click.Choice([
    'openai', 'anthropic', 'google', 'azure', 'mistral', 'ollama'
]), required=True, help='LLM provider')
@click.option('--model', help='Model name (e.g., gpt-4, claude-3, llama3.1)')
@click.option('--api-key', help='API key for cloud providers')
@click.option('--endpoint', help='Custom endpoint URL')
@click.option('--temperature', type=float, default=0.7, help='Temperature (0.0-1.0)')
@click.option('--max-tokens', type=int, default=4000, help='Maximum tokens')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.pass_context
def configure_ai(ctx, provider, model, api_key, endpoint, temperature, max_tokens, project):
    """
    Configure AI provider and model settings
    
    \b
    Examples:
      # Configure OpenAI
      archiagents ai configure --provider openai --model gpt-4 --api-key sk-...
      
      # Configure local Ollama
      archiagents ai configure --provider ollama --model llama3.1
      
      # Configure Anthropic Claude
      archiagents ai configure --provider anthropic --model claude-3-opus-20240229
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config_file = project_path / '.archiagents' / 'project.yaml'
    
    if not config_file.exists():
        click.echo(ConsoleColors.error("❌ Not an ArchiAgents project directory"), err=True)
        raise click.Abort()
    
    config = ProjectConfig(str(project_path))
    
    # Update AI configuration
    config.set('ai.enabled', True)
    config.set('ai.provider', provider)
    
    if model:
        config.set('ai.model', model)
    
    if api_key:
        config.set('ai.api_key', api_key)
    
    if endpoint:
        config.set('ai.endpoint', endpoint)
    
    config.set('ai.temperature', temperature)
    config.set('ai.max_tokens', max_tokens)
    
    config.save()
    
    click.echo(ConsoleColors.success("\n✅ AI configuration updated successfully!"))
    click.echo(f"\n{ConsoleColors.CYAN}Configuration:{ConsoleColors.END}")
    click.echo(f"  Provider: {provider}")
    click.echo(f"  Model: {model or 'default'}")
    click.echo(f"  Temperature: {temperature}")
    click.echo(f"  Max Tokens: {max_tokens}")
    
    if provider == 'ollama':
        click.echo(f"\n{ConsoleColors.info('ℹ️  Ollama requires local installation:')}")
        click.echo("  https://ollama.ai")
        click.echo(f"  Pull model: ollama pull {model or 'llama3.1'}")


@click.command(name='test')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--prompt', default='Explain TOGAF ADM in one sentence', help='Test prompt')
@click.pass_context
def test_ai(ctx, project, prompt):
    """
    Test AI provider connection and response
    
    \b
    Example:
      archiagents ai test --prompt "What is enterprise architecture?"
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    if not config.get('ai.enabled', False):
        click.echo(ConsoleColors.error("❌ AI is not configured. Run 'archiagents ai configure' first."), err=True)
        raise click.Abort()
    
    provider = config.get('ai.provider')
    model = config.get('ai.model')
    
    click.echo(f"\n{ConsoleColors.HEADER}Testing AI Connection{ConsoleColors.END}")
    click.echo(f"Provider: {provider}")
    click.echo(f"Model: {model}")
    click.echo(f"Prompt: {prompt}\n")
    
    try:
        from ai_agents.llm_providers import LLMProviderFactory
        
        # Create LLM instance
        llm = LLMProviderFactory.create_llm(
            provider=provider,
            model=model,
            temperature=config.get('ai.temperature', 0.7),
            max_tokens=config.get('ai.max_tokens', 4000),
            api_key=config.get('ai.api_key')
        )
        
        click.echo(ConsoleColors.info("🔄 Sending test request..."))
        
        # Send test prompt
        response = llm.invoke(prompt)
        
        click.echo(ConsoleColors.success("\n✅ Connection successful!\n"))
        click.echo(f"{ConsoleColors.CYAN}Response:{ConsoleColors.END}")
        click.echo(f"{response.content}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Test failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='list-models')
@click.option('--provider', type=click.Choice([
    'openai', 'anthropic', 'google', 'azure', 'mistral', 'ollama'
]), help='Filter by provider')
@click.pass_context
def list_models(ctx, provider):
    """
    List available models for each provider
    
    \b
    Example:
      archiagents ai list-models
      archiagents ai list-models --provider openai
    """
    
    models_info = {
        'openai': {
            'name': 'OpenAI',
            'models': [
                {'name': 'gpt-4-turbo', 'description': 'Most capable, latest GPT-4 Turbo', 'cost': '$$$$'},
                {'name': 'gpt-4', 'description': 'High-quality reasoning and analysis', 'cost': '$$$'},
                {'name': 'gpt-3.5-turbo', 'description': 'Fast and cost-effective', 'cost': '$'},
            ]
        },
        'anthropic': {
            'name': 'Anthropic Claude',
            'models': [
                {'name': 'claude-3-opus-20240229', 'description': 'Most powerful, best for complex tasks', 'cost': '$$$$'},
                {'name': 'claude-3-sonnet-20240229', 'description': 'Balanced performance and cost', 'cost': '$$'},
                {'name': 'claude-3-haiku-20240307', 'description': 'Fastest, most affordable', 'cost': '$'},
            ]
        },
        'google': {
            'name': 'Google Gemini',
            'models': [
                {'name': 'gemini-1.5-pro', 'description': 'Most capable, 1M context', 'cost': '$$$'},
                {'name': 'gemini-1.5-flash', 'description': 'Fast and efficient', 'cost': '$'},
            ]
        },
        'ollama': {
            'name': 'Ollama (Local)',
            'models': [
                {'name': 'llama3.1', 'description': 'Meta Llama 3.1 (8B-405B)', 'cost': 'FREE'},
                {'name': 'mistral', 'description': 'Mistral 7B', 'cost': 'FREE'},
                {'name': 'mixtral', 'description': 'Mixtral 8x7B MoE', 'cost': 'FREE'},
                {'name': 'phi-2', 'description': 'Microsoft Phi-2 (2.7B)', 'cost': 'FREE'},
                {'name': 'codellama', 'description': 'Code Llama for coding', 'cost': 'FREE'},
            ]
        },
        'mistral': {
            'name': 'Mistral AI',
            'models': [
                {'name': 'mistral-large', 'description': 'Most capable Mistral model', 'cost': '$$$'},
                {'name': 'mistral-medium', 'description': 'Balanced performance', 'cost': '$$'},
                {'name': 'mistral-small', 'description': 'Cost-effective', 'cost': '$'},
            ]
        },
        'azure': {
            'name': 'Azure OpenAI',
            'models': [
                {'name': 'gpt-4', 'description': 'GPT-4 on Azure', 'cost': '$$$'},
                {'name': 'gpt-35-turbo', 'description': 'GPT-3.5 Turbo on Azure', 'cost': '$'},
            ]
        }
    }
    
    providers_to_show = [provider] if provider else models_info.keys()
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Available AI Models{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    for prov in providers_to_show:
        info = models_info.get(prov, {})
        if not info:
            continue
        
        click.echo(f"{ConsoleColors.CYAN}{info['name']}{ConsoleColors.END}")
        click.echo(f"{'-' * len(info['name'])}")
        
        for model in info['models']:
            cost_color = ConsoleColors.GREEN if model['cost'] == 'FREE' else ConsoleColors.YELLOW
            click.echo(f"  • {ConsoleColors.BOLD}{model['name']}{ConsoleColors.END}")
            click.echo(f"    {model['description']}")
            click.echo(f"    Cost: {cost_color}{model['cost']}{ConsoleColors.END}")
        
        click.echo()


@click.command(name='agents')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--format', type=click.Choice(['table', 'json', 'tree']), default='table')
@click.pass_context
def list_agents(ctx, project, format):
    """
    List all available AI agent roles and capabilities
    
    \b
    Example:
      archiagents ai agents
      archiagents ai agents --format json
    """
    
    agents = [
        {
            'role': 'chief_architect',
            'name': 'Chief Enterprise Architect',
            'capabilities': ['Strategic planning', 'Stakeholder alignment', 'Vision development'],
            'phases': ['Preliminary', 'Phase A']
        },
        {
            'role': 'business_architect',
            'name': 'Business Architect',
            'capabilities': ['Process modeling', 'Value stream mapping', 'Capability mapping'],
            'phases': ['Phase B']
        },
        {
            'role': 'data_architect',
            'name': 'Data Architect',
            'capabilities': ['Data modeling', 'Information architecture', 'Data governance'],
            'phases': ['Phase C']
        },
        {
            'role': 'application_architect',
            'name': 'Application Architect',
            'capabilities': ['Application portfolio', 'Integration patterns', 'API design'],
            'phases': ['Phase C']
        },
        {
            'role': 'infrastructure_architect',
            'name': 'Infrastructure Architect',
            'capabilities': ['Cloud architecture', 'Network design', 'Infrastructure automation'],
            'phases': ['Phase D']
        },
        {
            'role': 'security_architect',
            'name': 'Security Architect',
            'capabilities': ['Security patterns', 'Threat modeling', 'Compliance'],
            'phases': ['All phases']
        },
        {
            'role': 'solution_architect',
            'name': 'Solution Architect',
            'capabilities': ['Solution design', 'Technology selection', 'Implementation planning'],
            'phases': ['Phase E']
        },
        {
            'role': 'migration_specialist',
            'name': 'Migration Specialist',
            'capabilities': ['Migration planning', 'Risk assessment', 'Roadmap development'],
            'phases': ['Phase F']
        },
        {
            'role': 'governance_specialist',
            'name': 'Governance Specialist',
            'capabilities': ['Governance frameworks', 'Compliance monitoring', 'Change control'],
            'phases': ['Phase G', 'Phase H']
        },
        {
            'role': 'requirements_analyst',
            'name': 'Requirements Analyst',
            'capabilities': ['Requirements elicitation', 'Stakeholder analysis', 'Documentation'],
            'phases': ['All phases']
        }
    ]
    
    if format == 'json':
        click.echo(json.dumps(agents, indent=2))
        return
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}AI Agent Roles & Capabilities{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    for agent in agents:
        click.echo(f"{ConsoleColors.CYAN}● {agent['name']}{ConsoleColors.END}")
        click.echo(f"  Role: {agent['role']}")
        click.echo(f"  Capabilities: {', '.join(agent['capabilities'])}")
        click.echo(f"  TOGAF Phases: {', '.join(agent['phases'])}")
        click.echo()


@click.command(name='run')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--task', required=True, help='Task description for AI agents')
@click.option('--use-langgraph', is_flag=True, default=True, help='Use LangGraph workflows')
@click.option('--use-crewai', is_flag=True, default=True, help='Use CrewAI teams')
@click.option('--agent-role', type=click.Choice([
    'chief_architect', 'business_architect', 'data_architect', 'application_architect',
    'infrastructure_architect', 'security_architect', 'solution_architect'
]), help='Specific agent role to use')
@click.option('--output', type=click.Path(), help='Output file for results')
@click.pass_context
def run_ai_task(ctx, project, task, use_langgraph, use_crewai, agent_role, output):
    """
    Run a specific task with AI agents
    
    \b
    Examples:
      archiagents ai run --task "Analyze current business processes"
      archiagents ai run --task "Design cloud migration strategy" --agent-role solution_architect
      archiagents ai run --task "Assess security posture" --agent-role security_architect --output results.json
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    if not config.get('ai.enabled', False):
        click.echo(ConsoleColors.error("❌ AI is not configured. Run 'archiagents ai configure' first."), err=True)
        raise click.Abort()
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}AI Task Execution{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Task:{ConsoleColors.END} {task}")
    click.echo(f"{ConsoleColors.CYAN}Project:{ConsoleColors.END} {config.get('project.name')}")
    if agent_role:
        click.echo(f"{ConsoleColors.CYAN}Agent Role:{ConsoleColors.END} {agent_role}")
    click.echo()
    
    try:
        from ai_agents import AIAgentOrchestrator
        
        orchestrator = AIAgentOrchestrator(
            enterprise_name=config.get('project.enterprise'),
            project_name=config.get('project.name'),
            architecture_scope=config.get('project.scope')
        )
        
        click.echo(ConsoleColors.info("🤖 Initializing AI agents..."))
        click.echo(ConsoleColors.info(f"🔄 Executing task..."))
        
        context = {
            'task': task,
            'project': config.get('project.name'),
            'enterprise': config.get('project.enterprise'),
            'scope': config.get('project.scope')
        }
        
        # Execute task
        if agent_role:
            # Single agent execution
            result = orchestrator.execute_with_specific_agent(agent_role, task, context)
        else:
            # Multi-agent execution
            result = orchestrator.execute_task(
                task=task,
                context=context,
                use_langgraph=use_langgraph,
                use_crewai=use_crewai
            )
        
        click.echo(ConsoleColors.success("\n✅ Task completed!"))
        
        # Display results
        if isinstance(result, dict):
            click.echo(f"\n{ConsoleColors.CYAN}Results:{ConsoleColors.END}")
            
            if result.get('output'):
                click.echo(result['output'])
            
            if result.get('recommendations'):
                click.echo(f"\n{ConsoleColors.BOLD}Recommendations:{ConsoleColors.END}")
                for i, rec in enumerate(result['recommendations'][:5], 1):
                    click.echo(f"  {i}. {rec}")
            
            if result.get('metrics'):
                click.echo(f"\n{ConsoleColors.BOLD}Metrics:{ConsoleColors.END}")
                for key, value in result['metrics'].items():
                    click.echo(f"  {key}: {value}")
        
        # Save results if output specified
        if output:
            output_path = Path(output)
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2, default=str)
            click.echo(f"\n{ConsoleColors.CYAN}Results saved to:{ConsoleColors.END} {output_path}")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Task execution failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()
