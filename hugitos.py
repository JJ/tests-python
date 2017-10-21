"""Hitos de IV servidos para usted"""

import hug

from HitosIV import HitosIV


estos_hitos = HitosIV()

@hug.get('/all')
def all():
    """Devuelve todos los hitos"""
    return { "hitos": estos_hitos.todos_hitos() }

