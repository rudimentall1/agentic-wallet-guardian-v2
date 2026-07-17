from app.analyzer import analyze
from app.policy_engine import evaluate_policy


def evaluate_action(request):

    policy_result = evaluate_policy(
        request
    )

    wallet_result = None

    if request.get("wallet"):

        try:
            wallet_result = analyze(
                request["wallet"]
            )

        except Exception as e:
            wallet_result = {
                "error": str(e)
            }


    risk_score = policy_result.get(
        "policy_risk_score",
        0
    )

    decision = policy_result.get(
        "policy_decision",
        "ALLOW"
    )

    reasons = []

    reasons.extend(
        policy_result.get(
            "policy_reasons",
            []
        )
    )


    if wallet_result:

        if isinstance(wallet_result, dict):

            analysis = wallet_result.get(
                "analysis",
                {}
            )

            wallet_score = analysis.get(
                "trust_score"
            )

            if wallet_score is not None:

                if wallet_score < 50:

                    decision = "WARN"

                    risk_score = max(
                        risk_score,
                        60
                    )

                    reasons.append(
                        "Wallet trust score is low"
                    )


    return {
        "guardian": "Agentic Wallet Guardian",
        "decision": decision,
        "risk_score": risk_score,
        "reasons": reasons,
        "analysis": wallet_result
    }
