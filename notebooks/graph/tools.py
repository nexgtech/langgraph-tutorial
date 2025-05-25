from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, START, END
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Fetch the API key
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0, 
)

# Define tool
def multiply(a: int, b: int) -> int:
    """
    Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# Bind tools
llm_with_tools = llm.bind_tools([multiply])

from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

# Define node
def tool_calling_node(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

builder = StateGraph(MessagesState)

builder.add_node("tool_calling_llm", tool_calling_node)
builder.add_node("tools", ToolNode([multiply]))

builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    tools_condition
)
builder.add_edge("tools", END)

graph = builder.compile()

graph.invoke({"messages": [HumanMessage(content="Multiply 3 and 5")]})
