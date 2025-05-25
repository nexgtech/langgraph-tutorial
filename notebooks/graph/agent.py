from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display
from typing import Literal
import random


## Define state of the graph
class State(TypedDict):
    graph_state: str


## Define nodes (python funcitons). Each node operates on the state.
def node_1(state):
    print("-------Node1----------")
    return {"graph_state": state['graph_state']+" I am"}
    
def node_2(state):
    print("-------Node2----------")
    return {"graph_state": state['graph_state']+" happy!"}

def node_3(state):
    print("-------Node3----------")
    return {"graph_state": state['graph_state']+" sad!"}



def decide_mood(state) -> Literal["node_2", "node_3"]:
    
    # use state to decide on the next node to visit
    user_input = state["graph_state"]

    if random.random() < 0.5:

        # 50% of time, return Node2
        return "node_2"
    
    # 50% of time, return Node3
    return "node_3"


builder = StateGraph(State)

# add nodes
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# graph compile
graph = builder.compile()

# view
display(Image(graph.get_graph().draw_mermaid_png()))

graph.invoke({"graph_state": "Hi, this is Lance."})