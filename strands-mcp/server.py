from fastmcp import FastMCP

mcp = FastMCP("Strands_MPC_Server")

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

if __name__ == "__main__":
    mcp.run()