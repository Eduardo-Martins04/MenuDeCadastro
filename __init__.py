# -*- coding: UTF-8
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print("ERRO! Digite um numero inteiro válido")
        else:
            return n
        
        
def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())    
    

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc