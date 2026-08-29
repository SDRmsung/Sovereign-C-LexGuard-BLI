---
id: a50.dorahacks.bli_legal_tech_hackathon_2
title: "[[README|⚖️ BLI Legal Tech Hackathon 2 (Sovereign LexGuard) 專屬戰略工作區]]"
aliases:
  - BLI_Legal_Tech_Hackathon_2
  - Sovereign_LexGuard
  - BLI法規黑客松工作區
description: "A50|DORAHACKS|BLI-LEGAL-TECH-HACKATHON-2|SOVEREIGN_LEXGUARD|README"
type: competition_workspace
domain: sys
tags:
  - a50
  - dorahacks
  - buidl
  - hackathon
  - legaltech
  - regtech
  - rwa
  - smart-contracts
  - formal-verification
compiler_status: active
created: "2026-08-27"
updated: "2026-08-27"
parent: ["[[m.A50.02_DORAHACKS_L2]]"]
related:
  - "[[01_BLI_Legal_Tech_2_Master_Spec|01_BLI 賽事詳細規格與作戰規劃]]"
  - "[[02_BLI_Hackers_and_BUIDLs_Reconnaissance|02_BLI 對手與黑客陣容偵察]]"
  - "[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/15-DoraHacks_Ongoing_Competitions_Audit|15 大 DoraHacks 賽事審計報告]]"
  - "[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/m.A50.10_SHARED_ARSENAL|A50 共享軍火庫 MOC]]"
---

# ⚖️ Sovereign LexGuard (BLI Legal Tech Hackathon 2)

> **AI-TRIZ Sovereign DoraHacks Pipeline | BUIDL 專案工廠 ✕ 形式化法律 SAT 審計 ✕ 鏈上 EIP-712 防禦**  
> 官方競賽：[BLI Legal Tech Hackathon 2 on DoraHacks](https://dorahacks.io/hackathon/legal-hack-2026)  
> 主辦機構：**Blockchain Legal Institute (BLI)** ✕ DoraHacks  
> 總獎金池：**~$50,000 USD** | 截止日期：`2026-11-01 01:01 UTC`  
> 開源許可：**Apache 2.0**

---

## 🌟 專案簡介 (Project Overview)

**Sovereign LexGuard** 是全球首個結合 **命題邏輯 SAT 形式化求解器 (DPLL)** 與 **Solidity 鏈上原子互鎖守衛 (EIP-712)** 的法律科技 (LegalTech / RegTech) 基礎設施。  
徹底解決傳統大模型法律問答的「法律幻覺（Legal Hallucination）」與「鏈下法律意見無法在鏈上原子執行」的行業致命痛點！

```
  【自然語言法律條款】 ──► [LegalDSLCompiler] ──(CNF)──► [DPLL SAT 求解器]
                                                              │
                                                    (零死鎖數學證明)
                                                              ▼
  【Solidity 智能合約】 ◄──(違法交易原子 Revert)── [LexGuardCore.sol (EIP-712)]
```

---

## 📁 完整工程目錄結構 (Repository Blueprint)

```
BLI-Legal-Tech-Hackathon-2/
├── 📄 README.md                            # 專案首頁與快速上手指南 (SSOT)
├── 📄 LICENSE                              # Apache 2.0 開源協議
├── 📄 pyproject.toml                       # Python 套件規格與 CLI 入口
├── 📄 01_BLI_Legal_Tech_2_Master_Spec.md   # 賽事完整規格手冊
├── 📄 02_BLI_Hackers_and_BUIDLs_Recon...   # 對手軍情深度偵察
│
├── 📦 src/                                 # 核心工程源碼 (純 Python 零依賴)
│   ├── 🐍 cli.py                           # 終端命令列工具 (`lexguard audit`)
│   ├── 🐍 compiler.py                      # 法律條款 ➔ CNF 子句編譯器
│   ├── 🐍 sat_verifier.py                  # 純 Python DPLL 形式化約束滿足引擎
│   ├── 🐍 sufield_causal.py                # 物場因果分析信用與清算路徑模型
│   │
│   └── 📦 contracts/                       # 鏈上防禦合約 (Solidity 0.8.20)
│       ├── 📜 ILexGuard.sol                # 標準守衛介面
│       ├── 📜 LexGuardCore.sol             # EIP-712 密碼學驗章與違法交易攔截
│       └── 📜 MockLendingProtocol.sol      # RWA 借貸合約調用範例
│
├── 📦 tests/                               # 一鍵驗證測試集
│   └── 🐍 run_all_checks.py                # 評審一鍵無腦跑測腳本 (4/4 綠燈通過)
│
└── 📦 docs/                                # DoraHacks 投遞證物
    ├── 📄 BUIDL_SUBMISSION_WHITEPAPER.md   # 完整官方投遞白皮書
    └── 📄 90_SEC_DEMO_SCRIPT.md            # 90 秒演示影片分鏡腳本
```

---

## ⚡ 快速上手與一鍵驗證 (Quick Start)

### 1. 評審一鍵端到端驗證 (One-Click Verification)
無需安裝繁複依賴，純標準函式庫秒級跑測：
```bash
python tests/run_all_checks.py
```
*實測輸出：`🎉 ALL TESTS PASSED (100% GREEN) in 2.01 ms!`*

### 2. 使用 LexGuard CLI 審計自訂法律條款
```bash
python src/cli.py audit contract_rules.json -o proof.json
```

---

## 🔗 雙向拓撲支撐節點
* DoraHacks 專屬分池：[[m.A50.02_DORAHACKS_L2|🏆 DoraHacks 專屬戰場 L2 MOC]]
* 15 大賽事審計報告：[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/15-DoraHacks_Ongoing_Competitions_Audit|📊 DoraHacks 15 大進行中賽事第三方審計報告]]
* A50 共享軍火庫：[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/m.A50.10_SHARED_ARSENAL|🎯 A50 共享軍火庫 MOC]]
* 投遞白皮書：[[docs/BUIDL_SUBMISSION_WHITEPAPER|📜 官方投遞白皮書]]
