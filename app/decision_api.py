from pydantic import BaseModel

from app.core.guardian_engine import evaluate_action as guardian_evaluate


class DecisionRequest(BaseModel):

    agent: str

    action: str

    wallet: str

    target_contract: str | None = None

    token: str | None = None

    amount: float | None = None



def evaluate_action(request: DecisionRequest):


    request_data = {

        "agent": request.agent,

        "action": request.action,

        "wallet": request.wallet,

        "target_contract":
            request.target_contract,

        "token":
            request.token,

        "amount":
            request.amount

    }


    result = guardian_evaluate(
        request_data
    )


    result["request"] = request_data


    return result
