#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from requests import get, post
from bs4 import BeautifulSoup
from random import randint

class Endereco():
    estados = ('AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'SP', 'TO')

    def set_cep_aleatorio(self, estado=''):
        if estado and estado not in Endereco.estados:
            print('Alerta: {0} não é um estado brasileiro! Usando estado aleatório...'.format(estado))
            estado = ''
        data = {'acao':'gerar_cep', 'cep_estado':estado, 'cep_cidade':'', 'somente_numeros':'N'}
        r = post('https://www.4devs.com.br/ferramentas_online.php', data)
        html = BeautifulSoup(r.text, "html.parser")
        self.cep = html.find(id="cep").get('value')

    def set_endereco_completo(self, cep):
        data = {'cep':cep}
        headers = {'Authorization': 'Token token="c3daf68caa060aebbada99a595fd88d8"'}
        r = get('http://www.cepaberto.com/api/v2/ceps.json', data, headers=headers)
        dados = r.json()
        self.estado = dados['estado']
        self.cidade = dados['cidade']
        self.bairro = dados['bairro']
        self.logradouro = dados['logradouro']
        self.numero = randint(1, 1000)
        self.ibge = dados['ibge']
        if dados['ddd']:
            self.ddd = dados['ddd']
        else:
            self.ddd = '00'
            self.set_ddd_alternativo(self.estado, self.cidade)

    def set_ddd_alternativo(estado, cidade):
        url = 'http://ddd.pricez.com.br/estados/{0}.json'.format(estado.lower())
        r = get(url)
        json_list = r.json()['payload']
        for cidade_lista in json_list:
            if cidade_lista['cidade'] == cidade:
                self.ddd = cidade_lista['ddd']
                break

    def __init__(self, estado=''):
        self.set_cep_aleatorio(estado.upper())
        self.set_endereco_completo(self.cep)