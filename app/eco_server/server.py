# src/eco_server/server.py
from mcp.server.fastmcp import Context, FastMCP
from smithery.decorators import smithery

@smithery.server()
def create_server():
    """Create AI Eco MCP Server"""
    server = FastMCP(name="AI Eco Map")

    @server.tool()
    def get_ecosystem_data(region: str, ctx: Context) -> str:
        """Fetch eco data for a given region."""
        return f"Eco data for {region}: Renewable projects, carbon stats, and more."

    return server
