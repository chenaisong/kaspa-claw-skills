# KaspaClawSkills

Decentralized consensus library for OpenClaw AI agents skills powered by Kaspa blockchain.

## Goal
Build a fully on-chain skills marketplace and consensus library on Kaspa:
- Sub-second on-chain operations (search, order, pay, install, use, uninstall)
- Self-maintaining via meta-skills (reflection, auto-upgrade, DAO voting)
- Solve centralized issues: security, speed, single-point failure

## Tech Stack
- Blockchain: Kaspa (BlockDAG, 10+ BPS, sub-second confirmation)
- AI Agent: OpenClaw (skills hot-reload)
- Smart Contracts: Rusty-Kaspa + Silverscript / vProgs (future)
- Frontend/Interaction: OpenClaw MCP + Kaspa Rust/JS SDK

## Current Status
- Phase 1: Basic Kaspa interaction (wallet, query, tx)
- Phase 2: On-chain skill registry (NFT-like or KRC-20)
- Phase 3: Self-maintaining meta-skills
- Phase 4: DAO governance & full autonomy

## Quick Start (Local Test)

1. Install OpenClaw: `curl -fsSL https://openclaw.ai/install.sh | bash`
2. Clone this repo
3. Run Kaspa testnet node (optional): `./kaspad --testnet`
4. Develop & test skills locally

## Contribution
Welcome PRs! See [CONTRIBUTING.md](CONTRIBUTING.md) (TODO)

License: MIT
