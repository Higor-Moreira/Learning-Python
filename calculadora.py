# codigo realiza as 4 operacoes basicas

# Menu inicial 
print("=-" * 10)
print(">>> CALCULADORA <<<")
print("0 - Sair \n"
        "1 - adicao \n"
        "2 - subtracao \n"
        "3 - multiplicacao \n"
        "4 - divisao")
print("=-" * 10)

# Recebe retorno do usuario 
operacao = input("Qual operação deseja fazer: ")

# Este bloco verifica se o valor digitado esta dentro do intervalo valido
while operacao not in '01234':

    print("ERRO! Por favor digite umas das seguintes opções :")
    print("0 - Sair \n"
        "1 - adicao \n"
        "2 - subtracao \n"
        "3 - multiplicacao \n"
        "4 - divisao")
    print("=-" * 10)

    operacao = input("Qual operação deseja fazer: ")

# Converte o valor digitado em int 
operacao = int(operacao)

while True:
    if operacao == 0:
        break
    elif operacao == 1:
        numero_1 = int(input("Digite o primeiro numero: "))
        numero_2 = int(input("Digite o segundo numero: "))
        resultado = numero_1 + numero_2
        print(f"A soma de {numero_1} + {numero_2} é = {resultado}")

print('saiu')