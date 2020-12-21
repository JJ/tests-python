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
    form = await request.form()
    data = {}
    for i in ['title','fecha']:
        data[i] = form[i]
    data['file'] = file
    print(data)
    estos_hitos.nuevo( file, form['title'], form['fecha'] )
    return JSONResponse( data, status_code=201 )


rutas = Router( routes = [
    Route("/hitos", endpoint=hitos, methods=["GET"]),
    Route("/hitos/{file}", endpoint=creaHito, methods=["PUT"] )
])
