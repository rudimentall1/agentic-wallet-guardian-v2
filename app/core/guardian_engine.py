from app.analyzer import analyze
from app.policy_engine import evaluate_policy


def evaluate_action(request):

    reasons = []

    wallet_result = None


    #
    # Wallet Intelligence
    #

    if request.get("wallet"):

        try:

            wallet_result = analyze(
                request["wallet"]
            )

        except Exception as e:

            wallet_result = {
                "error": str(e)
            }



    #
    # Extract wallet trust score
    #

    wallet_score = None


    if isinstance(wallet_result, dict):

        wallet_score = wallet_result.get(
            "trust_score"
        )



    #
    # Policy evaluation
    #

    policy_result = evaluate_policy(

        amount=request.get(
            "amount"
        ),

        contract=request.get(
            "target_contract"
        ),

        wallet_risk=wallet_score,

        action=request.get(
            "action"
        )

    )


    reasons.extend(
        policy_result.get(
            "policy_reasons",
            []
        )
    )



    #
    # Final decision fusion
    #

    decision = policy_result.get(
        "policy_decision",
        "ALLOW"
    )


    risk_score = policy_result.get(
        "policy_risk_score",
        0
    )



    #
    # Wallet Risk influence
    #

    if wallet_score is not None:


        if wallet_score < 30:

            decision = "BLOCK"

            risk_score = max(
                risk_score,
                90
            )

            reasons.append(
                "Wallet trust score critically low"
            )


        elif wallet_score < 50:

            if decision == "ALLOW":

                decision = "WARN"


            risk_score = max(
                risk_score,
                60
            )

            reasons.append(
                "Wallet trust score requires review"
            )



    #
    # Guardian action
    #

    actions = {

        "ALLOW":
            "Execution allowed",

        "WARN":
            "User confirmation required",

        "BLOCK":
            "Execution blocked"

    }


    return {

        "guardian":
            "Agentic Wallet Guardian",


        "decision":
            decision,


        "risk_score":
            min(
                risk_score,
                100
            ),


        "reasons":
            reasons,


        "wallet_analysis":
            wallet_result,


        "guardian_action":
            actions.get(
                decision
            )

    }
