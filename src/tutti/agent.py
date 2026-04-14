"""Agent — the primary interface for running Tutti AI agents."""

from tutti.types import AgentConfig


class Agent:
    """A Tutti AI agent.

    See https://github.com/tuttiai/tutti-python for documentation.
    """

    def __init__(self, config: AgentConfig) -> None:
        self.config = config

    def run(self, input: str) -> str:
        """Run the agent synchronously."""
        raise NotImplementedError(
            "Agent.run() is not yet implemented. "
            "Track progress at https://github.com/tuttiai/tutti-python"
        )

    async def run_async(self, input: str) -> str:
        """Run the agent asynchronously."""
        raise NotImplementedError(
            "Agent.run_async() is not yet implemented. "
            "Track progress at https://github.com/tuttiai/tutti-python"
        )
