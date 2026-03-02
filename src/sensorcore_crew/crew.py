import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.mcp import MCPServerHTTP


@CrewBase
class SensorCoreCrew:
    """SensorCore Analytics Crew — AI-powered product analytics.

    This crew connects to your SensorCore project via MCP and runs
    a comprehensive analysis: health monitoring, growth opportunities,
    and bug investigation. Results are saved to `report.md`.
    """

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def _mcp_servers(self):
        """Build MCP server list for SensorCore."""
        api_key = os.environ.get("SENSORCORE_API_KEY", "")
        base_url = os.environ.get(
            "SENSORCORE_MCP_URL", "https://api.sensorcore.dev/api/mcp/sse"
        )
        return [
            MCPServerHTTP(
                url=base_url,
                headers={"x-api-key": api_key},
            )
        ]

    # ── Agents ──────────────────────────────────────────────

    @agent
    def health_monitor(self) -> Agent:
        return Agent(
            config=self.agents_config["health_monitor"],  # type: ignore[index]
            verbose=True,
            mcps=self._mcp_servers(),
        )

    @agent
    def growth_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["growth_analyst"],  # type: ignore[index]
            verbose=True,
            mcps=self._mcp_servers(),
        )

    @agent
    def bug_detective(self) -> Agent:
        return Agent(
            config=self.agents_config["bug_detective"],  # type: ignore[index]
            verbose=True,
            mcps=self._mcp_servers(),
        )

    # ── Tasks ───────────────────────────────────────────────

    @task
    def health_check(self) -> Task:
        return Task(config=self.tasks_config["health_check"])  # type: ignore[index]

    @task
    def conversion_analysis(self) -> Task:
        return Task(config=self.tasks_config["conversion_analysis"])  # type: ignore[index]

    @task
    def bug_investigation(self) -> Task:
        return Task(config=self.tasks_config["bug_investigation"])  # type: ignore[index]

    @task
    def executive_summary(self) -> Task:
        return Task(config=self.tasks_config["executive_summary"])  # type: ignore[index]

    # ── Crew ────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # type: ignore[attr-defined]
            tasks=self.tasks,  # type: ignore[attr-defined]
            process=Process.sequential,
            verbose=True,
        )

