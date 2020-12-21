from starlette.applications import Starlette
from starlette.routing import Route, Router
from starlette.responses import JSONResponse

from HitosIV.core import HitosIV

""" Declara clase """
estos_hitos = HitosIV()

""" Define API """
async def hitos(request):
    """Devuelve todos los hitos o crea uno dependiendo del método"""
    if request.method == "GET":
        return JSONResponse( estos_hitos.todos_hitos() )
    elif request.method == "POST":
        file = str(int( estos_hitos.cuantos() ) + 1)
        return await construyeHito( file, request )

async def construyeHito( file, request ):
    form = await request.form()
    data = {}
    for i in ['title','fecha']:
        data[i] = form[i]
    data['file'] = file
    estos_hitos.nuevo( file, form['title'], form['fecha'] )
    return JSONResponse( data, status_code=201, headers={ 'Location': f"/hitos/{file}" })

async def creaHito( request ):
    """ Crea un hito """
    file = request.path_params["file"]
    return await construyeHito( file, request )

rutas = Router( routes = [
    Route("/hitos/{file}", endpoint=creaHito, methods=["PUT"]),
    Route("/hitos", endpoint=hitos, methods=["GET","POST"])
])
