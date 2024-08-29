"""
DIGITE A SENHA CORRETA
"""
senha_correta = "Jamerson"

while True:
    senha = input("Qual é o animal com o maior nivel de QI?: ")
    if senha == senha_correta:
        print("Na mosca!")
        break
    else:
        print("Errou animal")