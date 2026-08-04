from fastmcp import FastMCP

mcp = FastMCP(name="math")

@mcp.tool(
        name="add_numbers",
        description="Adds two numbers and returns the result"
)
def add(first: int, second: int) -> int:
    return first + second

@mcp.tool(
        name="multipy_numbers",
        description="Adds two numbers and returns the result"
)
def multiply(first: int, second: int) -> int:
    return first * second

@mcp.tool
def greet(name: str) -> str:
    return f"Hello {name}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

