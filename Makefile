# ADK 專案開發管理工具
.PHONY: help web create-agent list-apps install

# 預設運行的 Agent
APP ?= litellm_skill_agent

# 模型與 API 設定
export LITELLM_MODEL_API_BASE ?= 
export LITELLM_MODEL_API_KEY ?= 
export LITELLM_MODEL_MODEL_NAME ?= 

help:
	@echo "可用指令："
	@echo "  make web [APP=名稱]    - 啟動 ADK Web UI (預設: $(APP))"
	@echo "  make create-agent      - 建立新的 Agent 範本"
	@echo "  make list-apps         - 列出當前目錄所有 ADK 應用"
	@echo "  make install           - 安裝必要依賴"
	@echo ""
	@echo "環境變數範例："
	@echo "  make web LITELLM_MODEL_API_KEY=sk-... LITELLM_MODEL_API_BASE=... LITELLM_MODEL_MODEL_NAME=..."

web:
	@echo "啟動 Web UI 控制台: $(APP)..."
	adk web

create-agent:
	@echo "請輸入要建立的 Agent 資料夾名稱："
	@read name; adk create ./$$name

list-apps:
	@ls -d */ | grep -E "agent|skill"

install:
	pip install google-adk litellm python-dotenv
