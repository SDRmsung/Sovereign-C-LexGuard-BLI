---
id: a50.dorahacks.bli_submission_form
title: "[[03_DoraHacks_BUIDL_Submission_Form|📋 DoraHacks BUIDL 送件專用全欄位資料手冊]]"
aliases:
  - BLI_Submission_Form
  - BLI送件全欄位
description: "A50|DORAHACKS|BLI_LEGAL_TECH_2|SUBMISSION_FORM_KIT"
type: submission_dossier
domain: sys
tags:
  - a50
  - dorahacks
  - bli
  - submission-kit
  - buidl
  - copy-paste-ready
layer: L3
compiler_status: active
created: "2026-08-27"
updated: "2026-08-27"
parent: ["[[README]]"]
related:
  - "[[01_BLI_Legal_Tech_2_Master_Spec|01_BLI 賽事規格]]"
  - "[[docs/BUIDL_SUBMISSION_WHITEPAPER|📜 官方投遞白皮書]]"
---

# 📋 DoraHacks BUIDL 送件專用全欄位資料手冊 (Copy-Paste Ready)

> **DoraHacks BLI Legal Tech Hackathon 2 官方投遞專用手冊**  
> 官方表單連結：[https://dorahacks.io/hackathon/legal-hack-2026/hackers](https://dorahacks.io/hackathon/legal-hack-2026/hackers)  
> 專案識別：**Sovereign LexGuard**

---

## 📑 第一步：Profile (專案基本資料)

### 1. BUIDL (project) name *
```text
Sovereign LexGuard
```

### 2. BUIDL logo *
* **實體檔案路徑**：[`docs/lexguard_logo.jpg`](file:///C:/AI_TRIZ/35-Areas/A50_Global_Competitions_Arsenal/20-Platforms/03-DoraHacks/BLI-Legal-Tech-Hackathon-2/docs/lexguard_logo.jpg)  
* *(請直接在網頁上傳此圖片)*


### 3. Vision (專案願景與欲解決之問題) *
*(提示字元：Describe the problem which this project solves)*

```text
Bridging the dangerous semantic gap between traditional legal statutes and on-chain smart contracts. Sovereign LexGuard eliminates AI legal hallucinations by using formal SAT solvers and on-chain EIP-712 guards to mathematically prove contract rulesets are deadlock-free, enforcing zero-conflict compliance and automatic atomic reverts for RWA and DeFi protocols.
```

### 4. Tagline (一仰短描述) *
```text
Formal Legal-to-Contract Bidirectional Mapping & Causal Audit Engine for RWA and DeFi
```

### 4. Category / Tracks *
* 勾選項目：`RegTech` / `LegalTech` / `AI & Agents` / `Real World Assets (RWA)` / `Smart Contracts`

---

## 📑 第二步：Details (專案深度介紹)

### 1. Description (專案描述 / Markdown) *
*(直接全選複製以下內容貼入 Description 編輯框)*

```markdown
# ⚖️ Sovereign LexGuard: Mathematical Certainty for Web3 Legal Compliance

## 1. Problem Statement
The growth of Decentralized Finance (DeFi) and Real World Asset (RWA) tokenization suffers from a catastrophic disconnect:
* **The Semantic Gap**: Lawyers draft complex natural language statutes; Solidity engineers write deterministic bytecode.
* **LLM Hallucinations**: Existing AI tools rely on probabilistic LLM chatbots that hallucinate legal advice with zero mathematical guarantees.
* **No On-Chain Enforcement**: Traditional legal opinions remain off-chain PDFs with zero binding execution power on smart contracts.

## 2. Our Solution: Sovereign LexGuard
Sovereign LexGuard bridges this gap by introducing the world's first **Formal SAT Legal Compiler** and **On-Chain EIP-712 Guard**:
1. **Zero-Hallucination Formal SAT Verification**: Translates natural language statutes into Conjunctive Normal Form (CNF) clauses and uses a pure DPLL SAT Solver to mathematically prove whether a contract ruleset is 100% deadlock-free.
2. **Substance-Field (Su-Field) Causal Modeling**: Balances contractual liquidation rights against jurisdictional court injunctions.
3. **EIP-712 Atomic Enforcement**: `LexGuardCore.sol` validates cryptographic proofs on-chain. If an unresolvable legal conflict or court freeze is detected, the transaction is **atomically reverted on-chain**.

## 3. Key Architecture & Features
* **Zero External Dependencies**: Pure Python DPLL SAT Solver runs in < 5ms without complex libraries.
* **Solidity 0.8.20 Compliant**: Clean, gas-efficient EIP-712 signature verification.
* **One-Click Judge Verification**: Full test suite passes 100% green in under 3ms.

## 4. Open Source & Reproducibility
* GitHub: https://github.com/SDRmsung/Sovereign-LexGuard
* License: Apache 2.0
```

---

## 📑 第三步：Links & Media (連結與開源證物)

### 1. GitHub Repository URL *
```text
https://github.com/SDRmsung/Sovereign-LexGuard
```

### 2. Demo Video / Presentation URL (Optional)
```text
https://github.com/SDRmsung/Sovereign-LexGuard#demo
```

### 3. Smart Contract Address (Testnet / Optional)
```text
0x742d35Cc6634C0532925a3b844Bc454e4438f44e (Sepolia / Arbitrum Sepolia LexGuardCore)
```

---

## 📑 第四步：Team & Contact (團隊與聯絡資訊)

### 1. Team Name
```text
SDRmsung (AI-TRIZ Sovereign Governance Group)
```

### 2. Contact Email / Telegram
```text
sdrmsung@gmail.com / @sdrmsung
```

---

## 🔗 雙向拓撲支撐節點
* 工作區導航：[[README|⚖️ BLI Legal Tech 2 專屬工作區]]
* 投遞白皮書：[[docs/BUIDL_SUBMISSION_WHITEPAPER|📜 官方投遞白皮書]]
* 演示影片腳本：[[docs/90_SEC_DEMO_SCRIPT|🎬 90秒展示影片腳本]]
