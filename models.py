# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)


class Data(object):
    'Classe para formatação de datas'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
    'Classe Pessoa'

    def __init__(self, nome, peso_kg, altura_mt):
        self.nome = nome
        self.peso_kg = peso_kg
        self.altura_mt = altura_mt

    def imprime_imc(self):
        imc = self.peso_kg / (self.altura_mt * self.altura_mt)
        print 'IMC de %s: %s' % (self.nome, imc)