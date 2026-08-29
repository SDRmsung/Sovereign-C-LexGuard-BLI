---
id: a50.dorahacks.bli_legal_hack_spec
title: "[[01_BLI_Legal_Tech_2_Master_Spec|📜 BLI Legal Tech Hackathon 2 賽事完整規格與 AI-TRIZ 破局戰略]]"
aliases:
  - BLI_Master_Spec
  - BLI詳細資料
description: "A50|DORAHACKS|BLI_LEGAL_TECH_2|MASTER_SPEC|STRATEGY"
type: competition_spec
domain: sys
tags:
  - a50
  - dorahacks
  - bli
  - legaltech
  - regtech
  - rwa
  - smart-contracts
  - ai-triz-spec
layer: L3
compiler_status: active
created: "2026-08-27"
updated: "2026-08-27"
parent: ["[[README]]"]
related:
  - "[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/15-DoraHacks_Ongoing_Competitions_Audit|15 大賽事審計報告]]"
  - "[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/m.A50.10_SHARED_ARSENAL|A50 共享軍火庫 MOC]]"
---

# 📜 BLI Legal Tech Hackathon 2 賽事完整規格與 AI-TRIZ 破局戰略

> **SOCO (Shell + Ollama CLI + Obsidian) 地端情資鏈**  
> 來源分析：[BLI Legal Tech Hackathon 2 on DoraHacks](https://dorahacks.io/hackathon/legal-hack-2026)  
> 主辦方：**Blockchain Legal Institute (BLI)**  

---

## 📊 一、 賽事實體基本面 (Fundamentals)

* **官方全名**：BLI Legal Tech Hackathon 2
* **平台**：DoraHacks (Global Online Hackathon)
* **主辦機構**：Blockchain Legal Institute (BLI) ✕ 加密法學社群 ✕ 加速器聯盟
* **競賽時程**：
  * **開賽日期**：`2026-05-15 12:01 UTC`
  * **截止日期**：`2026-11-01 01:01 UTC`（剩餘約 65 天，充裕期）
* **總獎金池**：**~$50,000 USD**（涵蓋各贊助商專項 Bounties、生態 Grants、Demo Day 宣傳與孵化器扶持）
* **賽事定位**：第二屆全球法律科技黑客松，聚焦於解決 Web3、數字資產與實體法律體系融合的痛點。

---

## 🎯 二、 核心賽道與專題範疇 (Hackathon Tracks)

1. **📜 智能合約形式化驗證與法規合規 (RegTech / Smart Contract Compliance)**：
   * 將傳統法律條款（條例、免責聲明、合規檢查）轉化為可執行的代碼 (Law as Code)。
   * 形式化驗證智能合約中的法律漏洞與邏輯矛盾。
2. **🏢 實體世界資產 (RWA) 鏈上法律穿透與確權**：
   * 房地產、債券、碳權等 RWA 代幣化過程中的所有權結構、跨國司法管轄權穿透與防暴雷清算機制。
3. **🤖 法律科技智慧體 (Legal-AI Agent & Copilot)**：
   * 智慧法律檢索（Case Law & Statues）、自動化爭議仲裁（Decentralized Arbitration）、跨法域合規審查。
4. **🔐 去中心化身分 (DID) 與隱私保護法律架構**：
   * 符合 GDPR / 隱私法規的零知識證明 (ZKP) 身分驗證。

---

## ⚔️ 三、 AI-TRIZ 破局戰略：Sovereign LexGuard (BUIDL 規劃)

### 1. 核心產品定位：`Sovereign LexGuard: 形式化法律-合約雙向映射與因果審計引擎`
* **痛點**：法律人不懂 Solidity，程式設計師不懂跨國法規合規，導致 RWA 與 DeFi 頻發法律硬分叉與監管死鎖。
* **破局機制**：
  * 自然語言法律條款 ➔ AI-TRIZ 物場因果解析 ➔ SAT 邏輯不變量約束 ➔ Solidity 合規 Guards 合約
* **技術底座調用**：
  1. **符號約束求解器 (`04_sat_constraint_solver.py`)**：將法規條款轉為 CNF 子句，以 DPLL/WalkSAT 檢驗合約邏輯是否有違法或衝突條款。
  2. **物場信用引擎 (`sufield_credit_engine.py`)**：建立合約違約與鏈上資產扣押的因果物場模型。
  3. **Attestcoin 鏈上驗證合約**：直接複用 `BUIDL-CTC-2026-Fall` 的 EIP-712 / ecrecover 防重放合規驗證邏輯。

---

## 📅 四、 參賽工程里程碑 (Milestones Roadmap)

| 階段 | 時間週期 | 核心交付目標 | 交付物路徑 |
| :--- | :---: | :--- | :--- |
| **Phase 1: 規格與原型** | 2026-08-28 ~ 09-15 | 完成 Legal-DSL 語意編譯器與 SAT 驗證器原型 | `src/lexguard_compiler.py` |
| **Phase 2: 合約與前端 Demo** | 2026-09-16 ~ 10-10 | 撰寫 Solidity 合規 Guard 模組與測試網部署 | `src/contracts/LexGuard.sol` |
| **Phase 3: 白皮書與 90s 演示** | 2026-10-11 ~ 10-25 | 輸出投遞白皮書與 DoraHacks 演示影片 | `docs/whitepaper.md` |
| **Phase 4: 官方投遞** | 2026-10-26 ~ 10-30 | 提交至 DoraHacks 平台並開源 GitHub Repo | `DoraHacks Project Submission` |

---

## 🔗 雙向拓撲支撐節點
* 工作區導航：[[README|⚖️ BLI Legal Tech 2 專屬工作區]]
* DoraHacks 專屬分池：[[m.A50.02_DORAHACKS_L2|🏆 DoraHacks 專屬戰場 L2 MOC]]
* 15 大賽事審計報告：[[35-Areas/A50_Global_Competitions_Arsenal/00-MOC/15-DoraHacks_Ongoing_Competitions_Audit|📊 DoraHacks 15 大進行中賽事第三方審計報告]]
