# -*- coding: UTF-8
from interface import *
from arquivo import *

from time import sleep

arq = 'relatorio.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do Sistema... Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida")
    sleep(2)
        