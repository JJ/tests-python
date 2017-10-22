"""Hitos de IV servidos para usted"""

import hug

from HitosIV import HitosIV


estos_hitos = HitosIV()

@hug.get('/all')
def all():
    """Devuelve todos los hitos"""
    return { "hitos": estos_hitos.todos_hitos() }

@hug.get('/one/{id}')
def one( id: int ):
    """Devuelve un hito"""
    return { "hito": estos_hitos.uno( id ) }
