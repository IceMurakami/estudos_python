import os

print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


def mostrar_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurante')
    print('3 - Ativar Restaurante')
    print('4 - Sair')


mostrar_opcoes()
opcao_escolhida = input('Escolha uma opção: ')

def formulario():
    nome = input('Nome da Pizarria:\n ')
    cep = input('Cep da Pizzaria: \n ') 

def cadastro(nome, cep):
    nome_pizzaria = nome
    cep_pizzaria = cep

def finalizar_app():
    os.system('cls')
    print('Encerando Programa')


while opcao_escolhida != '4':
   
    if opcao_escolhida == '1':
        formulario()


    if opcao_escolhida == '2':
        print(3)

    if opcao_escolhida == '3':
        print(4)
        

    if opcao_escolhida == '4':
        finalizar_app()
        break
        
    mostrar_opcoes()
    opcao_escolhida = input('Escolha uma opção: ')   
   
    





    #    if opcao_escolhida == '1':
#        formulario()


