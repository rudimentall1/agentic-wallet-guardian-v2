# Agentic Wallet Guardian

AI-powered Web3 security decision agent for autonomous AI agents.

## Status

✅ Agent Service Provider (ASP)  
✅ REST API  
✅ Ethereum Wallet Intelligence  
✅ Explainable Risk Decisions


## Overview

Agentic Wallet Guardian is an Agent Service Provider (ASP) that helps AI agents make safer blockchain decisions.

Before an autonomous agent interacts with a wallet, token, or smart contract, Wallet Guardian evaluates security risks and provides an explainable decision:

- ALLOW
- ALLOW_WITH_LIMITATIONS
- WARN
- BLOCK

The goal is to provide a trust layer between AI agents and Web3.


## Problem

AI agents are becoming capable of executing blockchain actions.

However, autonomous transactions create a new security challenge:

> How can an AI agent know whether a wallet interaction is safe?


## Solution

Agentic Wallet Guardian analyzes:

- wallet behavior
- transaction history
- wallet age
- token intelligence
- smart contract risks
- approval security

and generates:

- trust score
- risk level
- confidence score
- explainable reasoning
- recommended action


## Architecture

```text
AI Agent
    |
    v
Agentic Wallet Guardian ASP
    |
    +-- Wallet Intelligence
    |
    +-- Token Intelligence
    |
    +-- Contract Intelligence
    |
    +-- Approval Security
    |
    +-- Risk Fusion Engine
    |
    v
ALLOW / WARN / BLOCK
```


## Demo Scenario

An AI trading agent wants to execute a Web3 transaction.

Before execution:

```text
AI Agent
    |
    v
Agentic Wallet Guardian
    |
    v
Security Decision
```

Example result:

```text
Decision:
ALLOW_WITH_LIMITATIONS

Trust Score:
94/100

Risk Level:
LOW
```

Reasoning:

- Long wallet history
- Large transaction activity
- No critical threats detected
- Approval intelligence limited


## API

### Analyze Wallet

POST:

```
/agent
```

Request:

```json
{
  "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
}
```

Response:

```json
{
  "service": "web3_security_decision",
  "agent": "Agentic Wallet Guardian",
  "result": {
    "risk_level": "LOW",
    "trust_score": 94,
    "decision": "ALLOW_WITH_LIMITATIONS",
    "confidence": 1.0
  }
}
```


## Available Skills

### Wallet Security Analysis

Analyzes wallet behavior and blockchain activity.


### Token Risk Analysis

Evaluates token-related risk signals.


### Contract Intelligence

Checks smart contract interaction risks.


### Approval Security

Analyzes approval-related security concerns.


## Tech Stack

- Python 3.10
- FastAPI
- Ethereum RPC
- AI Agent Architecture
- Risk Fusion Engine


## Vision

As autonomous AI agents begin interacting with digital assets, they need security and trust layers.

Agentic Wallet Guardian provides an intelligent security decision layer before Web3 actions are executed.
