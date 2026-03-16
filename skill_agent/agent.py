import pathlib
from google.adk.agents.llm_agent import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset

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
    model='gemini-2.5-flash',
    name='travel_agent',
    description='A helpful assistant that can leverage specialized skills.',
    instruction=(
        "You are a helpful travel assistant that can leverage specialized skills."
        "When a user asks for travel-related tasks, activate and use your 'travel-planner' skill."
    ),
    tools=[
        my_skill_toolset,
    ],
)
