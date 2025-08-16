from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

server_params = StdioServerParameters(
    command="uv",
    args=["run", "ArXiv Mcp/arxiv_research_server.py"],  # Adjust the script name as needed
    env=None,  # Optional environment variables
)

async def main(user_input: str):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await load_mcp_tools(session)
            
            agent = create_react_agent(
                model=llm,
                tools=tools
                
            )
            agent_response = await agent.ainvoke(
                {"messages": [
                    {"role": "user", "content": user_input}
                ]})
            
            print(agent_response['messages'][-1].content)

if __name__ == "__main__":
    # user_input = input("User:: ")
    asyncio.run(main("Attention is all you need"))  