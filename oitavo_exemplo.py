"""
ESCOLHENDO A OPÇÃO
"""

while True:
    print("\nMenu:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '4':
        print("Saindo...")
        break
    elif escolha == '1':
        print("Você escolheu a Opção 1!")
    elif escolha == '2':
        print("Você escolheu a Opção 2!")
    elif escolha == '3':
        print("Você escolheu a Opção 3!")
    else:
        print("Opção inválida! Tente novamente.")