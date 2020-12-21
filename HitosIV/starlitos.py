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

async def creaHito( request ):
    """ Crea un hito """
    file = request.path_params["file"]
    data = await request.json()
    data['file'] = file
    estos_hitos['hitos'].append(data)


rutas = Router( routes = [
    Route("/hitos", endpoint=hitos, methods=["GET"]),
    Route("/hitos/{file}", endpoint=creaHito, methods=["PUT"] )
])
