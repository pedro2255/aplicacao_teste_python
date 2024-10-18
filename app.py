
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

def exbir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')
    

def finalizar_app():
    os.system('cls')
    #os.system('clear') no mac
    print("Finalizando app\n")

def opcao_invalida():
    print("Opção invalida!\n")
    input("Digite uma tecla para voltar ao menu:")
    main()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        if opcao_escolhida == 1:
            print("Cadastrar restaurante")
        elif opcao_escolhida == 2:
            print("Listar restaurante")
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:    
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()            



def main():
    os.system('cls')
    exibir_nome_do_programa()
    exbir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()







    
    



