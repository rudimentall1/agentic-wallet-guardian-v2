"""
Guardian Threat Simulation Engine v1

Creates realistic AI agent attack scenarios
for ChainHack demonstration.
"""


def malicious_agent_attack():

    return {

        "agent":
            "drainer-agent-777",


        "wallet":
            "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",


        "action":
            "transfer",


        "amount":
            500,


        "target_contract":
            "0xBAD0000000000000000000000000000000000001"

    }



def suspicious_agent_attack():

    return {

        "agent":
            "unknown-agent-x",


        "wallet":
            "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",


        "action":
            "transfer",


        "amount":
            100,


        "target_contract":
            "0xUNKNOWN00000000000000000000000000000001"

    }



def safe_agent_action():

    return {

        "agent":
            "trusted-trading-agent",


        "wallet":
            "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",


        "action":
            "swap",


        "amount":
            10,


        "target_contract":
            "known-dex"

    }
