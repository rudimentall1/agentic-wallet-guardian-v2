"""
Guardian Demo Scenarios v1

Creates fake attack history
for ChainHack demonstrations.
"""

from app.core.memory_engine import save_decision


def seed_malicious_agent():

    agent = "drainer-agent-777"

    wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"


    history = [

        {
            "decision": "WARN",
            "risk_score": 40
        },

        {
            "decision": "WARN",
            "risk_score": 50
        },

        {
            "decision": "WARN",
            "risk_score": 60
        },

        {
            "decision": "BLOCK",
            "risk_score": 90
        },

        {
            "decision": "BLOCK",
            "risk_score": 95
        }

    ]


    for item in history:

        save_decision(

            agent=agent,

            wallet=wallet,

            action="transfer",

            decision=item["decision"],

            risk_score=item["risk_score"]

        )


    return {

        "agent": agent,

        "history_added": len(history)

    }
