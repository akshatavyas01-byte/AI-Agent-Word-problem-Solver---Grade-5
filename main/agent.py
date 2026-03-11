from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("api_key")

model=HuggingFaceEndpoint(
    model="zai-org/GLM-5:novita",
    huggingfacehub_api_token=api_key,
    temperature=0.1,
    top_k=1,
    top_p= 0.9
)


Chatmodel=ChatHuggingFace(llm=model)

@tool
def Addition(x:int, y:int)-> int:
    """Add the two integer values."""
    z=x+y
    return z

@tool
def Subtraction(x:int, y:int)-> int:
    """Subtract the smaller integer from the bigger interger."""
    if(x>y):
        z=x-y
    else:
        z=y-x
    return z

@tool
def Multiplication(x:int, y:int)-> int:
    """Multiply the two integer values."""
    z=x*y
    return z

@tool
def Division(x:int, y:int)-> int:
    """Divide the bigger integer by the smaller integer."""
    if(x>y):
        z=x%y
    else:
        z=y%x
    return z

prompt=SystemMessage(
    content=
    """Think in step by step process to solve the math problems.
    Tools provided:Addition,Subtraction,Multiplication and Division."
    Tools accept only integer inputs.""")

agent=create_agent(
    model=Chatmodel,
    tools=[Addition,Subtraction,Multiplication,Division],
    system_prompt=prompt
)

# response=agent.invoke({'messages':[
# HumanMessage(content="A cricket team scored 456 and 249 runs. How many in total?")
# ]})

# print(response["messages"][-1].content)