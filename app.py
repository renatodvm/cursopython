# -*- coding: UTF-8 -*-
import re

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Digite o nome a remover:'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome gostaria de alterar?'
    nome = raw_input()
    if (nome in nomes):
        print 'Digite o novo nome:'
        novo_nome = raw_input()
        nomes[nomes.index(nome)] = novo_nome
    else:
        print 'Nome não encontrado'

def pesquisar(nomes):
    print 'Digite um nome para procurar:'
    nome = raw_input()
    if (nome in nomes):
        print 'Nome está na lista'
    else:
        print 'Nome não encontrado'

def pesquisar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concat = ' '.join(nomes)
    busca = re.findall(regex, nomes_concat)
    print busca

def menu():
    nomes = []
    escolha = ''
    while (escolha != 0):
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 6 para procurar regex e 0 para terminar'
        escolha = raw_input()

        if (escolha == '1'):
            cadastrar(nomes)

        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

        if (escolha == '4'):
            alterar(nomes)

        if (escolha == '5'):
            pesquisar(nomes)

        if (escolha == '6'):
            pesquisar_regex(nomes)

menu()