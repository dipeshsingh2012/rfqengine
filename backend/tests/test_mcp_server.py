import pytest
from app.mcp.server import MCPServer

def test_mcp_server_registration():
    server = MCPServer(name="TestServer")
    
    tool_name = "get_weather"
    tool_desc = "Get current weather"
    tool_schema = {"type": "object", "properties": {"location": {"type": "string"}}}
    
    server.register_tool(tool_name, tool_desc, tool_schema)
    
    tools = server.list_tools()
    assert len(tools) == 1
    assert tools[0]["name"] == tool_name
    assert tools[0]["description"] == tool_desc
    assert tools[0]["input_schema"] == tool_schema

def test_mcp_server_empty_tools():
    server = MCPServer(name="EmptyServer")
    assert server.list_tools() == []
