"""
Guardian Demo Engine v1

Creates human-readable
security simulation output.
"""


def create_simulation(
    request,
    decision_result
):

    decision = decision_result.get(
        "decision"
    )

    risk_score = decision_result.get(
        "risk_score"
    )


    explanation = decision_result.get(
        "explanation",
        {}
    )


    wallet = request.get(
        "wallet"
    )

    agent = request.get(
        "agent"
    )

    action = request.get(
        "action"
    )

    amount = request.get(
        "amount"
    )


    return {

        "simulation":
            "complete",


        "agent_request": {

            "agent":
                agent,

            "action":
                action,

            "amount":
                amount,

            "wallet":
                wallet

        },


        "guardian_analysis": {

            "risk_score":
                risk_score,

            "decision":
                decision

        },


        "security_explanation":

            explanation,


        "final_message":

            explanation.get(
                "agent_message"
            )

    }
