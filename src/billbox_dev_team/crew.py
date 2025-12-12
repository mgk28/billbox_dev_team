from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.tools import tool
from pathlib import Path
import yaml

from billbox_dev_team.tools.fs_tools import read_file, write_file, list_tree, apply_patch
from billbox_dev_team.tools.cmd_tools import run_cmd
from billbox_dev_team.tools.git_tools import git_status, git_commit, git_push, ensure_gh_auth

# Convertir les fonctions en outils CrewAI
@tool("Read a file from the filesystem")
def read_file_tool(path: str) -> str:
    """Read a file from the filesystem"""
    return read_file(path)

@tool("Write content to a file")
def write_file_tool(path: str, content: str) -> str:
    """Write content to a file"""
    return write_file(path, content)

@tool("List directory tree structure")
def list_tree_tool(path: str = ".", max_depth: int = 4) -> str:
    """List directory tree structure"""
    return list_tree(path, max_depth)

@tool("Apply a git-style patch to a file")
def apply_patch_tool(patch: str) -> str:
    """Apply a git-style patch to a file"""
    return apply_patch(patch)

@tool("Run a shell command safely")
def run_cmd_tool(cmd: str, cwd: str = ".", timeout: int = 900) -> str:
    """Run a shell command safely"""
    return run_cmd(cmd, cwd, timeout)

@tool("Get git status")
def git_status_tool() -> str:
    """Get git status"""
    return git_status()

@tool("Create a git commit")
def git_commit_tool(message: str) -> str:
    """Create a git commit"""
    return git_commit(message)

@tool("Push to git remote")
def git_push_tool(branch: str = "main") -> str:
    """Push to git remote"""
    return git_push(branch)

@tool("Ensure GitHub authentication")
def ensure_gh_auth_tool() -> str:
    """Ensure GitHub authentication"""
    return ensure_gh_auth()

@CrewBase
class BillboxDevTeamCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    def _load_config_file(self, config_path: str):
        """Charge un fichier YAML de configuration"""
        path = Path(__file__).parent / config_path
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _get_agent_config(self, agent_key: str):
        """Récupère la configuration d'un agent depuis le fichier YAML"""
        # Si agents_config est déjà un dict (chargé par CrewAI), l'utiliser
        if isinstance(self.agents_config, dict):
            config_dict = self.agents_config
        else:
            # Sinon, charger depuis le fichier
            config_dict = self._load_config_file(self.agents_config)
        
        # Essayer d'abord avec la clé de niveau supérieur "agents"
        if isinstance(config_dict, dict) and "agents" in config_dict:
            agent_config = config_dict["agents"].get(agent_key)
            if agent_config and isinstance(agent_config, dict):
                return agent_config
        # Sinon, chercher directement
        if isinstance(config_dict, dict):
            agent_config = config_dict.get(agent_key)
            if agent_config and isinstance(agent_config, dict):
                return agent_config
        return None
    
    def _get_task_config(self, task_key: str):
        """Récupère la configuration d'une tâche depuis le fichier YAML"""
        # Si tasks_config est déjà un dict (chargé par CrewAI), l'utiliser
        if isinstance(self.tasks_config, dict):
            config_dict = self.tasks_config
        else:
            # Sinon, charger depuis le fichier
            config_dict = self._load_config_file(self.tasks_config)
        
        # Essayer d'abord avec la clé de niveau supérieur "tasks"
        if isinstance(config_dict, dict) and "tasks" in config_dict:
            task_config = config_dict["tasks"].get(task_key)
            if task_config and isinstance(task_config, dict):
                return task_config
        # Sinon, chercher directement
        if isinstance(config_dict, dict):
            task_config = config_dict.get(task_key)
            if task_config and isinstance(task_config, dict):
                return task_config
        return None

    # --- AGENTS ---
    @agent
    def pm_agent(self) -> Agent:
        config_dict = self._get_agent_config("pm_agent")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for agent 'pm_agent'")
        # Passer les paramètres individuellement pour éviter les problèmes de sérialisation
        return Agent(
            role=config_dict.get("role", ""),
            goal=config_dict.get("goal", ""),
            backstory=config_dict.get("backstory", ""),
            allow_delegation=config_dict.get("allow_delegation", False),
            tools=[read_file_tool, write_file_tool, list_tree_tool]
        )

    @agent
    def tech_lead_agent(self) -> Agent:
        config_dict = self._get_agent_config("tech_lead_agent")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for agent 'tech_lead_agent'")
        return Agent(
            role=config_dict.get("role", ""),
            goal=config_dict.get("goal", ""),
            backstory=config_dict.get("backstory", ""),
            allow_delegation=config_dict.get("allow_delegation", False),
            tools=[read_file_tool, write_file_tool, list_tree_tool, apply_patch_tool, run_cmd_tool]
        )

    @agent
    def backend_dev_agent(self) -> Agent:
        config_dict = self._get_agent_config("backend_dev_agent")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for agent 'backend_dev_agent'")
        return Agent(
            role=config_dict.get("role", ""),
            goal=config_dict.get("goal", ""),
            backstory=config_dict.get("backstory", ""),
            allow_delegation=config_dict.get("allow_delegation", False),
            tools=[read_file_tool, write_file_tool, list_tree_tool, apply_patch_tool, run_cmd_tool]
        )

    @agent
    def frontend_dev_agent(self) -> Agent:
        config_dict = self._get_agent_config("frontend_dev_agent")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for agent 'frontend_dev_agent'")
        return Agent(
            role=config_dict.get("role", ""),
            goal=config_dict.get("goal", ""),
            backstory=config_dict.get("backstory", ""),
            allow_delegation=config_dict.get("allow_delegation", False),
            tools=[read_file_tool, write_file_tool, list_tree_tool, apply_patch_tool, run_cmd_tool]
        )

    @agent
    def mobile_dev_agent(self) -> Agent:
        config_dict = self._get_agent_config("mobile_dev_agent")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for agent 'mobile_dev_agent'")
        return Agent(
            role=config_dict.get("role", ""),
            goal=config_dict.get("goal", ""),
            backstory=config_dict.get("backstory", ""),
            allow_delegation=config_dict.get("allow_delegation", False),
            tools=[read_file_tool, write_file_tool, list_tree_tool, apply_patch_tool, run_cmd_tool]
        )

    @agent
    def qa_release_agent(self) -> Agent:
        config_dict = self._get_agent_config("qa_release_agent")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for agent 'qa_release_agent'")
        return Agent(
            role=config_dict.get("role", ""),
            goal=config_dict.get("goal", ""),
            backstory=config_dict.get("backstory", ""),
            allow_delegation=config_dict.get("allow_delegation", False),
            tools=[
                read_file_tool, write_file_tool, list_tree_tool, run_cmd_tool,
                ensure_gh_auth_tool, git_status_tool, git_commit_tool, git_push_tool
            ]
        )

    # Helper pour obtenir l'agent par son nom
    def _get_agent_by_name(self, agent_name: str):
        """Récupère un agent par son nom en appelant la méthode correspondante"""
        agent_method = getattr(self, agent_name, None)
        if agent_method and callable(agent_method):
            return agent_method()
        return None
    
    # Helper pour obtenir les tâches de contexte
    def _get_context_tasks(self, context_names: list):
        """Récupère les tâches de contexte par leurs noms"""
        context_tasks = []
        for ctx_name in context_names:
            task_method = getattr(self, ctx_name, None)
            if task_method and callable(task_method):
                context_tasks.append(task_method())
        return context_tasks if context_tasks else None

    # --- TASKS ---
    @task
    def spec_task(self) -> Task:
        config_dict = self._get_task_config("spec_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'spec_task'")
        agent_name = config_dict.get("agent", "pm_agent")
        agent = self._get_agent_by_name(agent_name)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent
        )

    @task
    def plan_task(self) -> Task:
        config_dict = self._get_task_config("plan_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'plan_task'")
        agent_name = config_dict.get("agent", "tech_lead_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @task
    def implement_backend_task(self) -> Task:
        config_dict = self._get_task_config("implement_backend_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'implement_backend_task'")
        agent_name = config_dict.get("agent", "backend_dev_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @task
    def implement_web_task(self) -> Task:
        config_dict = self._get_task_config("implement_web_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'implement_web_task'")
        agent_name = config_dict.get("agent", "frontend_dev_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @task
    def implement_mobile_task(self) -> Task:
        config_dict = self._get_task_config("implement_mobile_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'implement_mobile_task'")
        agent_name = config_dict.get("agent", "mobile_dev_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @task
    def test_task(self) -> Task:
        config_dict = self._get_task_config("test_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'test_task'")
        agent_name = config_dict.get("agent", "qa_release_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @task
    def commit_push_task(self) -> Task:
        config_dict = self._get_task_config("commit_push_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'commit_push_task'")
        agent_name = config_dict.get("agent", "qa_release_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @task
    def deploy_task(self) -> Task:
        config_dict = self._get_task_config("deploy_task")
        if not config_dict or not isinstance(config_dict, dict):
            raise ValueError(f"Configuration not found for task 'deploy_task'")
        agent_name = config_dict.get("agent", "qa_release_agent")
        agent = self._get_agent_by_name(agent_name)
        context_names = config_dict.get("context", [])
        context_tasks = self._get_context_tasks(context_names)
        return Task(
            description=config_dict.get("description", ""),
            expected_output=config_dict.get("expected_output", ""),
            agent=agent,
            context=context_tasks
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
