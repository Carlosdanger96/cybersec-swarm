from agency_swarm import Agent, ModelSettings
from openai.types.shared import Reasoning
from dotenv import load_dotenv

from config import get_default_model, is_openai_provider

load_dotenv()


def create_orchestrator() -> Agent:
    return Agent(
        name="Cybersec Orchestrator",
        description=(
            "Primary coordinator for defensive cybersecurity workflows. Routes requests to scope, "
            "threat modeling, research, code review, log analysis, MCP tool-safety, governance, "
            "docs, slides, and data specialists without performing specialist work directly."
        ),
        instructions="./instructions.md",
        model=get_default_model(),
        model_settings=ModelSettings(
            reasoning=Reasoning(effort="medium", summary="auto") if is_openai_provider() else None,
        ),
        conversation_starters=[
            "Create a threat model for my local MCP gateway.",
            "Review this uploaded code for security issues.",
            "Analyze these synthetic SIEM logs and build an incident timeline.",
            "Create a governance package for LLM tool-safety and prompt-injection testing.",
        ],
    )


if __name__ == "__main__":
    from agency_swarm import Agency
    Agency(create_orchestrator()).terminal_demo()
