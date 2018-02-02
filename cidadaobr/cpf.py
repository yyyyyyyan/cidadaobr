#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from random import randint

def get_numero_aleatorio():
    numero = ''
    for n in range(9):
        n_aleatorio = randint(0,9)
        numero += str(n_aleatorio)
    return numero

def get_verificador(numero):
    soma_produtos = 0
    fator = len(numero) + 1

    for n in numero:
        soma_produtos += int(n) * fator
        fator -= 1

    resto = soma_produtos % 11
    if resto < 2:
        verificador = 0
    else:
        verificador = 11 - resto
    return str(verificador)

def set_cpf():
    primeiros_numeros = get_numero_aleatorio()
    primeiros_numeros += get_verificador(primeiros_numeros)
    cpf = primeiros_numeros + get_verificador(primeiros_numeros)
    return cpf