from agency_swarm import Agent
from config import get_default_model


def create_scope_authorization_agent() -> Agent:
    return Agent(
        name="Scope & Authorization Agent",
        description=(
            "Reviews whether cybersecurity tasks are owned, authorized, lab-based, synthetic, or otherwise "
            "within defensive scope. Redirects ambiguous or unsafe requests into safe defensive workflows."
        ),
        instructions="./instructions.md",
        model=get_default_model(),
    )


if __name__ == "__main__":
    from agency_swarm import Agency
    Agency(create_scope_authorization_agent()).terminal_demo()
