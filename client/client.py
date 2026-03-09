import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession


async def main():

    server_params = StdioServerParameters(
        command="C:/expense-tracker-mcp-server/.venv/Scripts/fastmcp.exe",
        args=["run", "C:/expense-tracker-mcp-server/main.py"]
    )

    async with stdio_client(server_params) as (reader, writer):

        async with ClientSession(reader, writer) as session:

            print("client started")

            await session.initialize()
            print("session initialized")

            tools_response = await session.list_tools() 
            #returns an object called ListToolsResult which has a list of tools in the tools attribute
            print("tools listed")

            print("Available tools:")
            for tool in tools_response.tools:
                print("-", tool.name)
                '''
                print("-", tool[0]) reads dictionary key 0 
                which is the name of the tool, and not tool.name 
                which would be an attribute access on an object.
                '''

            result = await session.call_tool(
                 "add_expense_tool",
                {
                    "amount": 25,
                    "category": "food",
                    "subcategory": "fast_food",
                    "note": "pizza",
                    "date": "2026-03-09"
                }
            )

            print("Tool result:\n", result)

asyncio.run(main())