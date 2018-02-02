#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from random import randint

def set_numero(ddd, fixo=True):
    if fixo:
        tipo = ' '
    else:
        tipo = ' 9'
    numero = '+55 {0}{1}'.format(ddd, tipo)
    numero += str(randint(1,9))
    for n in range(7):
        numero += str(randint(0,9))
    return numero