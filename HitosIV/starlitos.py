from starlette.applications import Starlette
from starlette.routing import Route, Router
from starlette.responses import JSONResponse

from HitosIV.core import HitosIV

""" Declara clase """
estos_hitos = HitosIV()

""" Define API """
async def hitos(request):
    """Devuelve todos los hitos"""
    return JSONResponse( estos_hitos.todos_hitos() )


rutas = Router( routes = [
    Route("/hitos", endpoint=hitos)
])
