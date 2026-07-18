from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import analyze_wallet
from app.decision_api import DecisionRequest, evaluate_action
from app.core.demo_engine import create_simulation
from app.core.threat_simulation import malicious_agent_attack
from app.core.demo_scenarios import seed_malicious_agent


app = FastAPI(
    title="Agentic Wallet Guardian",
    description="AI security decision agent that helps autonomous agents evaluate Web3 wallet and transaction risks.",
    version="2.1.0"
)


class WalletRequest(BaseModel):
    address: str


class SimulationRequest(BaseModel):
    scenario: str



@app.get("/")
def home():

    return {
        "agent": "Agentic Wallet Guardian",
        "status": "online",
        "version": "2.1.0",
        "type": "ASP"
    }



@app.get("/health")
def health():

    return {
        "status": "healthy",
        "agent": "Agentic Wallet Guardian"
    }



@app.get("/capabilities")
def capabilities():

    return {
        "agent": "Agentic Wallet Guardian",
        "type": "ASP",
        "capabilities": [
            "wallet security analysis",
            "transaction risk evaluation",
            "token and contract risk analysis",
            "approval security analysis",
            "explainable AI security decisions",
            "AI agent reputation analysis",
            "autonomous agent threat simulation"
        ]
    }



@app.post("/analyze")
def analyze(request: WalletRequest):

    return analyze_wallet(
        request.address
    )



@app.post("/agent")
def agent_request(request: WalletRequest):

    result = analyze_wallet(
        request.address
    )

    return {
        "service": "web3_security_decision",
        "agent": "Agentic Wallet Guardian",
        "description": "AI security layer for Web3 interactions",
        "result": result
    }



@app.post("/decision")
def decision(request: DecisionRequest):

    return evaluate_action(
        request
    )



@app.post("/simulate")
def simulate(request: SimulationRequest):

    if request.scenario == "malicious_agent":

        seed_malicious_agent()


        attack_request = malicious_agent_attack()


        decision_request = DecisionRequest(
            **attack_request
        )


        result = evaluate_action(
            decision_request
        )


        return create_simulation(

            attack_request,

            result

        )


    return {

        "error":
            "unknown scenario",

        "available_scenarios":
            [
                "malicious_agent"
            ]

    }
