from dataclasses import dataclass

@dataclass
class DisasterState:

    severity: int
    people_affected: int
    resources_available: int


class EmergencyAgent:

    def __init__(self):
        self.trace = []

    def decide(self, state):

        self.trace.append(
            f"Severity={state.severity}"
        )

        if state.severity >= 8:

            self.trace.append(
                "Immediate Rescue Selected"
            )

            return "Immediate Rescue"

        elif state.severity >= 5:

            self.trace.append(
                "Priority Response Selected"
            )

            return "Priority Response"

        self.trace.append(
            "Monitor Situation Selected"
        )

        return "Monitor Situation"

    def get_trace(self):

        return self.trace


if __name__ == "__main__":

    state = DisasterState(
        severity=9,
        people_affected=50,
        resources_available=10
    )

    agent = EmergencyAgent()

    print(agent.decide(state))

    print(agent.get_trace())