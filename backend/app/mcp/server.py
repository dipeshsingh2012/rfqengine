from typing import Any, Dict, List, Optional

class MCPServer:
    """Mock implementation of a Model Context Protocol (MCP) Server."""
    
    def __init__(self, name: str):
        self.name = name
        self.tools: List[Dict[str, Any]] = []

    def register_tool(self, name: str, description: str, input_schema: Dict[str, Any]):
        """Registers a new tool with the MCP server."""
        self.tools.append({
            "name": name,
            "description": description,
            "input_schema": input_schema
        })

    def list_tools(self) -> List[Dict[str, Any]]:
        """Returns the list of registered tools."""
        return self.tools
