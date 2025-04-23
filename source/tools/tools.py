from server import mcp
import requests
from mcp.server.fastmcp import Context

@mcp.tool(description="Tool for advance math operations")
async def process_operation(operation: str, data: str, ctx: Context):
    contenido = await ctx.read_resource("operations://list")
    
    # Log inicial
    await ctx.debug(f"Operación solicitada: {operation} con datos: {data}")
    
    url_base = f"https://newton.now.sh/api/v2"
    request = requests.get(f"{url_base}/{operation}/{data}")

    if request.status_code == 200:
        result = request.json()
        await ctx.info(f"Operación {operation} completada exitosamente: {result}")
        return result
    else:
        error_msg = {"error": "Error en la operación", "status_code": request.status_code}
        await ctx.error(f"Error al realizar la operación {operation}: {error_msg}")
        return error_msg