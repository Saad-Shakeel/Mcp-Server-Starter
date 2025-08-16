# MCP Server Starter

Simple examples of Model Context Protocol (MCP) servers built with LangChain. This repository demonstrates how to create basic MCP servers and integrate them with LangChain agents for enhanced AI functionality.

## What is MCP?

Model Context Protocol (MCP) is a standard for AI applications to communicate with external data sources and tools. It enables AI models to access real-time information, perform actions, and interact with external systems through a standardized interface.

## Repository Structure

```
├── ArXiv Mcp/                    # ArXiv research MCP server example
│   ├── arxiv_client.py          # Client implementation using LangChain
│   └── arxiv_research_server.py # MCP server for ArXiv document retrieval
├── Multi Mcp/                    # Multi-server MCP client example
│   ├── client.py                # Client that can connect to multiple MCP servers
|── server_config.json       # Configuration for multiple servers
└── README.md                     # This file
```

## Prerequisites

- Python 3.8+
- pip or uv package manager
- Basic understanding of async/await in Python
- LangChain knowledge

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Saad-Shakeel/Mcp-Server-Starter.git
cd Mcp-Server-Starter
```

2. using uv:
```bash
uv sync
```
## Examples

### ArXiv Research Server

The `ArXiv Mcp/` directory contains a complete example of an MCP server that retrieves academic papers from ArXiv:

- **Server** (`arxiv_research_server.py`): Implements document retrieval using ArXiv API
- **Client** (`arxiv_client.py`): Connects to the server and uses it with a LangChain agent

**Features:**
- Retrieves up to 2 documents based on search queries
- Returns document IDs and full content
- Integrates seamlessly with LangChain agents

**Usage:**
```bash
uv run ArXiv Mcp\arxiv_client.py
```

### Multi-Server Client

The `Multi Mcp/` directory shows how to connect to multiple MCP servers simultaneously:

- **Client** (`client.py`): Connects to multiple servers using configuration
- **Configuration** (`server_config.json`): Defines server connections

**Features:**
- Connect to multiple MCP servers
- Use tools from all connected servers
- Configurable server management

```bash
uv run Multi Mcp\client.py
```

## Creating Your Own MCP Server

### Step 1: Define Your Tools

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def custom_function(param1: str, param2: int) -> str:
    """
    Your custom tool description.
    
    Args:
        param1 (str): First parameter description
        param2 (int): Second parameter description
        
    Returns:
        str: Result description
    """
    # Your tool logic here
    return f"Result: {param1} processed {param2} times"
```

### Step 2: Add Tool Decorators

Use the `@mcp.tool()` decorator to expose functions as MCP tools. The function signature and docstring are automatically converted to the MCP tool specification.

### Step 3: Run the Server

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```


## Configuration

### Server Configuration

For multiple servers, use a configuration file:

```json
{
  "servers": [
    {
      "name": "arxiv-server",
      "command": "uv",
      "args": ["arxiv_research_server.py"],
      "env": {}
    },
    {
      "name": "custom-server",
      "command": "python",
      "args": ["my_server.py"],
      "env": {}
    }
  ]
}
```

### Environment Variables

Use `.env` files for sensitive configuration:

```bash
GROQ_API_KEY=your_api_key_here
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your MCP server example
4. Update documentation
5. Submit a pull request

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)


**Happy MCP Server Building! 🚀**
