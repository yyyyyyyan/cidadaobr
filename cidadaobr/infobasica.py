#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from requests import get
from datetime import date
from random import choice as randchoice

def is_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 > 0 or ano % 400 == 0:
            return True
    return False

def set_nome():
    data = {'q':1, 'o':'plain'}
    r = get('http://www.wjr.eti.br/nameGenerator/index.php', data)
    return r.text

def set_data_nascimento_aleatoria():
    ano = randchoice(range(1950, 2000))
    mes = randchoice(range(1, 13))
    if mes == 2:
        if is_ano_bissexto(ano):
            dia = randchoice(range(1, 30))
        else:
            dia = randchoice(range(1, 29))
    elif (mes <= 7 and mes % 2 > 0) or (mes > 7 and mes % 2 == 0):
        dia = randchoice(range(1, 32))
    else:
        dia = randchoice(range(1, 31))
    return date(ano, mes, dia)

def set_data_nascimento(data):
    if not data:
        return set_data_nascimento_aleatoria()
        
    data_nascimento = data.split('/')
    try:
        data = date(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]))
    except ValueError:
        print('\n\nAlerta: Data inválida. Padrão deve ser AAAA/MM/DD. Gerando data aleatória...')
        data = set_data_nascimento_aleatoria()
    finally:
        return data

def set_idade(data_nascimento):
    hoje = date.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))