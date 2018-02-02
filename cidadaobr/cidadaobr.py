#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from infobasica import set_nome, set_data_nascimento, set_idade
from cpf import set_cpf
from endereco import Endereco
from telefone import set_numero
from rg import set_rg

class CidadaoBrasileiro():
    def __init__(self, nome='', data_nascimento='', estado=''):
        self.nome = nome if nome else set_nome()
        self.data_nascimento = set_data_nascimento(data_nascimento)
        self.idade = set_idade(self.data_nascimento)
        self.cpf = set_cpf()
        self.endereco = Endereco(estado)
        self.telefone_fixo = set_numero(self.endereco.ddd)
        self.celular = set_numero(self.endereco.ddd, False)
        self.rg = set_rg(self.endereco.estado)

    def __repr__(self):
        dados = "Nome: {0}".format(self.nome)
        dados += "\nData de Nascimento: {0}".format(self.data_nascimento)
        dados += "\nIdade: {0}".format(self.idade)
        dados += "\nCPF: {0}".format(self.cpf)
        dados += "\nRG: {0}".format(self.rg)
        dados += "\nEndereço:"
        dados += "\n\tBrasil - {0} - {1}".format(self.endereco.estado, self.endereco.cidade)
        dados += "\n\t{0}\n\t{1}, {2}".format(self.endereco.bairro, self.endereco.logradouro, self.endereco.numero)
        dados += "\n\tIBGE: {0}".format(self.endereco.ibge)
        dados += "\nTelefone Fixo: {0}".format(self.telefone_fixo)
        dados += "\nTelefone Celular: {0}".format(self.celular)
        return dados

    def __getitem__(self, index):
        json = self.json()
        return json[index]

    def json(self):
        nascimento = str(self.data_nascimento.day) + '/' + str(self.data_nascimento.month) + '/' + str(self.data_nascimento.year)
        json = {'nome':self.nome, 'nascimento':nascimento, 'idade':self.idade, 'cpf':self.cpf,
                'pais':'Brasil', 'estado':self.endereco.estado, 'cidade':self.endereco.cidade, 'rg':self.rg,
                'bairro':self.endereco.bairro, 'logradouro':self.endereco.logradouro, 'endereco_numero':self.endereco.numero,
                'endereco_ibge':self.endereco.ibge, 'fixo':self.telefone_fixo, 'celular':self.celular}
        return json

