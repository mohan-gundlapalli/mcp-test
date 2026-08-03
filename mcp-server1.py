from fastmcp import FastMCP

mcp = FastMCP("First MCP")

@mcp.tool
def add(first: int, second: int) -> int:
    return first + second

@mcp.tool
def greet(name: str) -> str:
    return f"Hello {name}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

