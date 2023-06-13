from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

llm = ChatOpenAI(temperature=0.0)
tools = load_tools(
    ["arxiv"], 
)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

test_str = "What's the paper 1605.08386 about?"

test_str1 = "Give me all the papers about generative AI or gpt or nlp in the last week please."
test_str2 = "Give me all the papers in the computer science category from today"
agent_chain.run(test_str2)

