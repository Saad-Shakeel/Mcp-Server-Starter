from langchain_community.retrievers import ArxivRetriever
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("research-mcp")

@mcp.tool()
def document_retriver(user_input: str) -> str:
    """
    Retrieve and return academic documents from the ArXiv database based on a user query.

    This tool queries the ArXiv API to fetch up to two relevant documents related to
    the provided search string. Each retrieved document includes its unique Entry ID
    (if available) and full content, separated by a delimiter for readability.

    Args:
        user_input (str): Search query or keywords for retrieving documents.

    Returns:
        str: A formatted string containing the Entry ID and full content of
             each retrieved document, separated by '---'.

    Example:
        >>> document_retriver("quantum computing")
        'ID: 1234.56789\n\nDocument content here...\n\n---\n\nID: 9876.54321\n\nDocument content here...'
    """
    retriever = ArxivRetriever(
        load_max_docs=2,
        get_ful_documents=True,  # assuming this is a valid parameter
    )
    docs = retriever.invoke(user_input)

    results = []
    for doc in docs:
        entry_id = doc.metadata.get("Entry ID", "No ID found")
        content = doc.page_content
        results.append(f"ID: {entry_id}\n\n{content}")

    return "\n\n---\n\n".join(results)


if __name__ == "__main__":
    mcp.run(transport="stdio")
