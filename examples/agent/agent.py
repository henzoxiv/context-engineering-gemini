"""
Example agent implementation showing patterns for creating
specialized AI agents with specific capabilities.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum
import asyncio
import logging

logger = logging.getLogger(__name__)


class AgentStatus(Enum):
    """Agent execution status."""
    IDLE = "idle"
    BUSY = "busy"
    ERROR = "error"
    OFFLINE = "offline"


@dataclass
class AgentCapability:
    """Represents a capability that an agent can perform."""
    name: str
    description: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]


@dataclass
class TaskResult:
    """Result of a task execution."""
    success: bool
    data: Any
    error_message: Optional[str] = None
    execution_time: Optional[float] = None


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    
    This shows the pattern for creating specialized agents
    with consistent interfaces and error handling.
    """
    
    def __init__(self, agent_id: str, name: str):
        self.agent_id = agent_id
        self.name = name
        self.status = AgentStatus.IDLE
        self.capabilities: List[AgentCapability] = []
        self._register_capabilities()
    
    @abstractmethod
    def _register_capabilities(self) -> None:
        """Register the capabilities this agent supports."""
        pass
    
    @abstractmethod
    async def execute_task(self, task_type: str, parameters: Dict[str, Any]) -> TaskResult:
        """Execute a specific task."""
        pass
    
    def get_capabilities(self) -> List[AgentCapability]:
        """Return list of capabilities this agent supports."""
        return self.capabilities.copy()
    
    def can_handle_task(self, task_type: str) -> bool:
        """Check if this agent can handle a specific task type."""
        return any(cap.name == task_type for cap in self.capabilities)
    
    async def health_check(self) -> bool:
        """Perform a health check on the agent."""
        try:
            # Basic health check - override in subclasses for specific checks
            return self.status != AgentStatus.OFFLINE
        except Exception as e:
            logger.error(f"Health check failed for agent {self.agent_id}: {e}")
            return False


class CodeAnalysisAgent(BaseAgent):
    """
    Example specialized agent for code analysis tasks.
    Shows patterns for implementing specific agent functionality.
    """
    
    def _register_capabilities(self) -> None:
        """Register code analysis capabilities."""
        self.capabilities = [
            AgentCapability(
                name="analyze_complexity",
                description="Analyze code complexity metrics",
                input_schema={
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "language": {"type": "string"}
                    },
                    "required": ["file_path"]
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "cyclomatic_complexity": {"type": "number"},
                        "lines_of_code": {"type": "integer"},
                        "function_count": {"type": "integer"}
                    }
                }
            )
        ]
    
    async def execute_task(self, task_type: str, parameters: Dict[str, Any]) -> TaskResult:
        """Execute code analysis tasks."""
        
        if not self.can_handle_task(task_type):
            return TaskResult(
                success=False,
                data=None,
                error_message=f"Agent {self.agent_id} cannot handle task type: {task_type}"
            )
        
        self.status = AgentStatus.BUSY
        
        try:
            if task_type == "analyze_complexity":
                result = await self._analyze_complexity(parameters)
            else:
                raise ValueError(f"Unknown task type: {task_type}")
            
            self.status = AgentStatus.IDLE
            return TaskResult(success=True, data=result)
            
        except Exception as e:
            logger.error(f"Task execution failed: {e}")
            self.status = AgentStatus.ERROR
            return TaskResult(
                success=False,
                data=None,
                error_message=str(e)
            )
    
    async def _analyze_complexity(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze code complexity (mock implementation)."""
        file_path = parameters["file_path"]
        
        # Simulate async analysis work
        await asyncio.sleep(0.1)
        
        # Mock complexity analysis results
        return {
            "cyclomatic_complexity": 3.2,
            "lines_of_code": 156,
            "function_count": 8,
            "file_path": file_path
        }


if __name__ == '__main__':
    # Example usage
    pass
