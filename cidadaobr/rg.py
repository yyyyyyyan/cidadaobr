#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from random import randint

def set_rg(estado):
    if estado.upper() != 'SP':
        return 'None'

    numeros = ''
    for n in range(8):
        numeros += str(randint(0, 9))

    soma_produtos = 0
    for i, n in enumerate(numeros):
        soma_produtos += int(n) * (i+2)

    if soma_produtos % 11 > 2:
        numeros += str(11 - (soma_produtos % 11))
    else:
        numeros += '0'

    return numeros