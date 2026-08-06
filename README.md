# Agentic Wallet Guardian v2

Security-oriented decision infrastructure for evaluating blockchain wallets before an AI agent interacts with them.

## Problem

Autonomous Web3 agents need a way to assess wallet activity and risk before proceeding with an interaction. A raw wallet score is not enough; the system should combine signals and explain the resulting decision.

## Solution

Version 2 implements a wallet-centric intelligence pipeline combining:

- wallet intelligence
- risk fusion
- explainable decisions
- agent reputation
- policy rules
- security memory
- FastAPI API
- demonstration UI

The core v2 model is:

```text
Wallet
  |
  v
Wallet Intelligence
  |
  v
Policy + Reputation
  |
  v
Risk Fusion
  |
  v
Explainable Decision
```

## Key Design Principle

Risk signals are combined into an explainable result rather than exposing a score without context.

## Stack

- Python
- FastAPI
- Web3 / EVM data sources
- REST API
- Linux / Docker-compatible deployment workflow

## Status

MVP / earlier architecture iteration.

The project is retained as the v2 reference point for the evolution toward the action-centric architecture in Agentic Wallet Guardian v3.
