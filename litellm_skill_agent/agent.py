import pathlib
import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset
from google.adk.models.lite_llm import LiteLlm

# 載入環境變數
load_dotenv()

# 嚴格從環境變數取得設定
API_BASE   = os.getenv("LITELLM_MODEL_API_BASE")
API_KEY    = os.getenv("LITELLM_MODEL_API_KEY")
MODEL_NAME = os.getenv("LITELLM_MODEL_MODEL_NAME")

# 驗證必要環境變數是否存在
missing_vars = [var for var, val in {
    "LITELLM_MODEL_API_BASE": API_BASE,
    "LITELLM_MODEL_API_KEY": API_KEY,
    "LITELLM_MODEL_MODEL_NAME": MODEL_NAME
}.items() if not val]

if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

# 初始化 LiteLlm 模型
litellm_model = LiteLlm(
    model=MODEL_NAME,
    api_base=API_BASE,
    api_key=API_KEY,
    extra_body={"skip_special_tokens": False}
)

# 載入 Skill
travel_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "travel-planner"
)

# 建立工具集
my_skill_toolset = skill_toolset.SkillToolset(
    skills=[travel_skill]
)

# 初始化 Agent
root_agent = Agent(
    model=litellm_model,
    name='travel_agent',
    description='A helpful assistant that can leverage specialized skills.',
    instruction=(
        "You are a helpful travel assistant that can leverage specialized skills. "
        "When a user asks for travel-related tasks, activate and use your 'travel-planner' skill."
    ),
    tools=[
        my_skill_toolset,
    ],
)
