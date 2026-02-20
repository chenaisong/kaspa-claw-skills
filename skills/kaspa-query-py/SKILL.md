---
name: kaspa-query-py
description: 当用户询问 Kaspa 区块链、DAG 信息、节点状态、测试网数据时，必须调用此 skill。关键词：Kaspa、DAG、节点、测试网、区块。
version: 0.1.0
author: chenaisong
language: python
triggers:
  - "查询 Kaspa"
  - "Kaspa 状态"
  - "Kaspa DAG"
  - "Kaspa 节点"
  - "Kaspa network"
examples:
  - "查询 Kaspa DAG 信息"
  - "Kaspa 测试网现在怎么样？"
  - "Kaspa 节点是否同步"
tools:
  - subprocess
---

## 使用说明 / Usage

这个 skill 通过调用本地 Rust 二进制工具查询 Kaspa 测试网实时数据，并返回自然语言总结。
This skill calls a local Rust binary to query real-time Kaspa testnet data and returns a natural language summary.

支持的查询类型：
- dag-info：DAG 网络信息（区块数、DAA 分数等）
- node-info：节点状态（版本、是否同步）

示例对话：
用户：查询 Kaspa DAG
代理：Kaspa 测试网当前区块总数 xxx，虚拟 DAA 分数 yyy，网络状态正常。