"""Core type definitions for Tutti AI."""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Tool:
    """A tool that an agent can invoke."""

    name: str
    description: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    handler: Optional[Callable[..., Any]] = None


@dataclass
class Voice:
    """A voice persona that shapes agent behaviour."""

    name: str
    system: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChatMessage:
    """A single message in a conversation."""

    role: str  # "user" | "assistant" | "system"
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentConfig:
    """Configuration for an Agent instance."""

    name: str
    model: str = "claude-sonnet-4-6"
    system: Optional[str] = None
    voices: List[Voice] = field(default_factory=list)
    max_turns: int = 10
