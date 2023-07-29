from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

import dotenv

from lib import ltspice, LTSpiceInput

dotenv.load_dotenv()

tools = [
    Tool.from_function(
        func=ltspice,
        name="LTSpice",
        description="useful for when you need to run an LTSpice simulation, provide a netlist directly to this function",
        args_schema=LTSpiceInput
    )
]

agent = initialize_agent(
    tools,
    ChatOpenAI(temperature=0, model="gpt-4",verbose=True),
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
)

# Load test.txt
with open("test.txt","r") as f:
    input = f.read()

prompt = f"Can you evaluate the output of the below netlist LTSpice circuit and analyze the output? \n ```\n{input}\n```"
print(prompt)
agent.run(prompt)