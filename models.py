# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s, Curtidas %s' % (self.nome, self.telefone, self.empresa, self.__curtidas)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        perfis = []
        arquivo = open(nome_arquivo, 'r')
        for linha in arquivo:
            valores = linha.split(',')
            perfil = classe(*valores)
            perfis.append(perfil)
        arquivo.close()
        return perfis

class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários VIPs'

    def __init__(self, nome, telefone, empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0

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