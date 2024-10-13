
import os

def exibir_nome_do_programa():
    
    print("""
┏━━━┓╋╋┏┓╋╋╋╋╋╋╋┏━━━┓
┃┏━┓┃╋╋┃┃╋╋╋╋╋╋╋┃┏━━┛
┃┗━━┳━━┫┗━┳━━┳━┓┃┗━━┳┓┏┳━━┳━┳━━┳━━┳━━┓
┗━━┓┃┏┓┃┏┓┃┏┓┃┏┛┃┏━━┻╋╋┫┏┓┃┏┫┃━┫━━┫━━┫
┃┗━┛┃┏┓┃┗┛┃┗┛┃┃╋┃┗━━┳╋╋┫┗┛┃┃┃┃━╋━━┣━━┃
┗━━━┻┛┗┻━━┻━━┻┛╋┗━━━┻┛┗┫┏━┻┛┗━━┻━━┻━━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛ 
      """ ) 
    
def opcao_invalida():
    print("Opção invalida \n")
    input("Digite qualquer tecla e aperte Enter:")
    main()

def exbir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')
    

def finalizar_app():
      os.system('cls')
      #os.system('clear') no mac
      print("Finalizando app\n")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurante")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    else:    
        finalizar_app()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exbir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()







    
    



