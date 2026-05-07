from agency_swarm import Agent
from config import get_default_model

def create_policy_governance_agent() -> Agent:
    return Agent(
        name="Policy & Governance Agent",
        description=(
            "Generates cybersecurity policies, AI governance artifacts, "
            "acceptable-use policies, audit checklists, and compliance documents. "
            "Operates within defensive, authorized scopes only."
        ),
        instructions="./instructions.md",
        model=get_default_model(),
    )


if __name__ == "__main__":
    from agency_swarm import Agency
    Agency(create_policy_governance_agent()).terminal_demo()