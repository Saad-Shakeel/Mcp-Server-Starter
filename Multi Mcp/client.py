import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main(user_input: str):
    # Load environment variables
    load_dotenv()

    # Create configuration dictionary
    # Create MCPClient from configuration dictionary
    client = MCPClient.from_config_file("server_config.json")

    # Create LLM
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

    # Create agent with the client
    agent = MCPAgent(
        llm=llm,
        client=client, 
        max_steps=30)

    # Run the query
    result = await agent.run(
        user_input
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    user_input = "Give me the summary of paper 'attention is all you need' and saved it in summary.txt file"
    asyncio.run(main(user_input))