from .agent import (
    EmergencyAgent,
    DisasterState
)

from .bayes import (
    flood_probability,
    cyclone_probability
)

from .utility import (
    rescue_priority
)


class HybridDecisionEngine:

    def __init__(self):

        self.trace = []

    def evaluate(
            self,
            rainfall,
            river_level,
            wind_speed,
            severity,
            people_affected,
            distance,
            resources_available):

        # -------------------------
        # Step 1: Risk Prediction
        # -------------------------

        flood_risk = flood_probability(
            rainfall,
            river_level
        )

        cyclone_risk = cyclone_probability(
            wind_speed
        )

        self.trace.append(
            f"Flood Risk = {flood_risk}"
        )

        self.trace.append(
            f"Cyclone Risk = {cyclone_risk}"
        )

        # -------------------------
        # Step 2: Agent Decision
        # -------------------------

        state = DisasterState(
            severity=severity,
            people_affected=people_affected,
            resources_available=resources_available
        )

        agent = EmergencyAgent()

        action = agent.decide(
            state
        )

        self.trace.extend(
            agent.get_trace()
        )

        # -------------------------
        # Step 3: Utility Score
        # -------------------------

        priority_score = rescue_priority(
            severity,
            people_affected,
            distance
        )

        self.trace.append(
            f"Priority Score = {priority_score}"
        )

        # -------------------------
        # Step 4: Final Recommendation
        # -------------------------

        if flood_risk >= 0.8:

            recommendation = (
                "Deploy Flood Rescue Teams"
            )

        elif cyclone_risk >= 0.8:

            recommendation = (
                "Deploy Cyclone Response Teams"
            )

        elif priority_score >= 100:

            recommendation = (
                "Immediate Emergency Response"
            )

        else:

            recommendation = (
                "Monitor Situation"
            )

        self.trace.append(
            f"Recommendation = {recommendation}"
        )

        return {
            "flood_risk": flood_risk,
            "cyclone_risk": cyclone_risk,
            "action": action,
            "priority_score": priority_score,
            "recommendation": recommendation,
            "trace": self.trace
        }

    def print_trace(self):

        print("\n--- Decision Trace ---")

        for step in self.trace:

            print(step)


# -----------------------------
# Testing
# -----------------------------

if __name__ == "__main__":

    engine = HybridDecisionEngine()

    result = engine.evaluate(
        rainfall=120,
        river_level=90,
        wind_speed=130,
        severity=9,
        people_affected=50,
        distance=15,
        resources_available=20
    )

    print("\n=== Hybrid AI Result ===")

    print(
        f"Flood Risk: "
        f"{result['flood_risk']}"
    )

    print(
        f"Cyclone Risk: "
        f"{result['cyclone_risk']}"
    )

    print(
        f"Action: "
        f"{result['action']}"
    )

    print(
        f"Priority Score: "
        f"{result['priority_score']}"
    )

    print(
        f"Recommendation: "
        f"{result['recommendation']}"
    )

    engine.print_trace()