# ADK Skill Agent 專案

本專案基於 Google ADK (Agent Development Kit) 框架，展示了如何建構具備專業技能 (Skill) 的 AI Agent。

## 🚀 專案結構

- `litellm_skill_agent/`: 使用 LiteLLM 整合模型並搭載 `travel-planner` 技能的主 Agent。
- `skill_agent/`: 使用 Gemini 模型並搭載 `travel-planner` 技能的 Agent。
- `skill_original_agent/`: 基本的 ADK Agent (未掛載 Skill)。

## 🛠️ 環境配置

請確保在對應的 Agent 資料夾中建立 `.env` 檔案，並配置以下變數：

### Google AI (Gemini)
```env
GOOGLE_API_KEY=YOUR_GEMINI_KEY
```

### LiteLLM
```env
LITELLM_MODEL_API_BASE=https://your-api-base-url.com/v1
LITELLM_MODEL_API_KEY=YOUR_API_KEY
LITELLM_MODEL_MODEL_NAME=openai/your-model-name
```

## 📖 快速上手

### 1. 安裝環境
```bash
make install
```

### 2. 啟動 Web UI
使用預設的 `litellm_skill_agent`:
```bash
make web
```

切換至其他 Agent (例如 `skill_agent`):
```bash
make web APP=skill_agent
```

### 3. 建立新 Agent
```bash
make create-agent
```

## 🧩 技能說明 (Skill)

### Travel Planner (`travel-planner`)
- **功能**: 提供 3-5 天行程規劃與行李準備建議。
- **組件**:
  - `SKILL.md`: 定義 Agent 的專業行為與工作流。
  - `assets/`: 行程 Markdown 範本。
  - `references/`: 通用行李準備指南。

## ⚠️ 常見問題 (FAQ)

- **環境變數**: 確保 `litellm_skill_agent` 中已配置所有 `LITELLM_MODEL_...` 相關變數，否則 Agent 會因為驗證失敗而無法啟動。
- **ValidationError**: Skill 的 `name` 在 `SKILL.md` 中必須使用 **kebab-case** (例如 `travel-planner`)。
