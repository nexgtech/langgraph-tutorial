# LangGraph Studio
Run the LangGraph application locally.

## Install the LangGraph CLI
```bash
pip install --upgrade "langgraph-cli[inmem]"
```

## Create a LangGraph app

Create a new app from the new-langgraph-project-python template 
```bash
langgraph new path/to/your/app --template new-langgraph-project-python
```

## Install dependencies
In the root of your new LangGraph app, install the dependencies in edit mode 
```bash
cd path/to/your/app
pip install -e .
```
## Create a .env file
You will then want to create a .env file with the relevant environment variables:

```bash
cp .env.example .env
```

## Launch LangGraph Server
Start the LangGraph API server locally

```bash
langgraph dev
```

The langgraph dev command starts LangGraph Server in an in-memory mode. This mode is suitable for development and testing purposes.


## Test application in LangGraph Studio
you can connect to LangGraph API server to visualize, interact with, and debug your application locally. Test your graph in LangGraph Studio by visiting the URL 

```bash
https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

When you invoke a graph, LangGraph Studio will automatically create a new thread for the session. You can manage multiple threads by switching between them using the dropdown menu located in the top-left corner of the right-hand pane. 