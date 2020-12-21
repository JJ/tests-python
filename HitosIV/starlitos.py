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

async def unHito( request ):
    """ Crea un hito """
    file = request.path_params["file"]
    print("unHito ", estos_hitos.uno_por_clave( file ))
    if request.method == "PUT":
        return await construyeHito( file, request )
    elif request.method == "GET":
        print("unHito ", estos_hitos.uno_por_clave( file ))
        try:
            return JSONResponse(estos_hitos.uno_por_clave( file ))
        except:
            return JSONResponse( { "error": f"No existe {file}" }, status_code=404 )
    else:
        return JSONResponse( { "error": f"Método no implementado {request.method}" }, status_code=405 )

rutas = Router( routes = [
    Route("/hitos/{file}", endpoint=unHito, methods=["GET","PUT"]),
    Route("/hitos", endpoint=hitos, methods=["GET","POST"])
])
