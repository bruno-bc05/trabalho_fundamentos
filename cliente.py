import socket

def send_number(number, original_base, target_base):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"convert {original_base} {number} {target_base}"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"O número {number} na base {original_base} convertido para a base {target_base} é: {result}")

    client_socket.close()

def soma(num1, num2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"math {num1} {num2} +"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A soma de {num1} com {num2} é: {result}")

    client_socket.close()

def subtracao(num1, num2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"math {num1} {num2} -"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A subtração de {num1} com {num2} é: {result}")

    client_socket.close()

def multiplicacao(num1, num2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"math {num1} {num2} *"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A multiplicação de {num1} com {num2} é: {result}")

    client_socket.close()

def divisao(num1, num2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"math {num1} {num2} /"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A divisão de {num1} com {num2} é: {result}")

    client_socket.close()

def IEE754(num1):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"ieee754 {num1}"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A representação (float) de {num1} no padrão IEEE754 é: {result}")

    client_socket.close()

def utf(palavra):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"utf {palavra}"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A representação (float) de '{palavra}' no padrão UTF-8 é: {result}")

    client_socket.close()

def simp_exp(expressao):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = f"simp {expressao}"
    client_socket.send(data.encode())

    result = client_socket.recv(1024).decode()
    print(f"A simplificação da expressão '{expressao}' é: {result}")

    client_socket.close()

if __name__ == "__main__":
    while True:
        opcao = int(input("Digite o número da questão (1 a 6) ou 0 para sair: "))
        if opcao == 0:
            break
        elif opcao == 1:
            original_base = int(input("Digite a base original (2, 8, 10, 16): "))
            number = input("Digite o número que deseja converter: ")
            target_base = int(input("Digite a base de destino (2, 8, 10, 16): "))
            send_number(number, original_base, target_base)
        elif opcao == 2:
            op = input('Dê a operação que deseja realizar (+, -, *): ')
            if op in ('+', '-', '*'):
                num1 = input("Número 1 (em binário): ")
                num2 = input("Número 2 (em binário): ")
                if op == '+':
                    soma(num1, num2)
                elif op == '-':
                    subtracao(num1, num2)
                elif op == '*':
                    multiplicacao(num1, num2)
            else:
                print("Operação inválida.")
        elif opcao == 3:
            num1 = input("Número 1 (em binário): ")
            num2 = input("Número 2 (em binário): ")
            divisao(num1, num2)
        elif opcao == 4:
            num1 = input("Número (decimal): ")
            IEE754(num1)
        elif opcao == 5:
            palavra = input("Forneça a palavra a ser codificada em UTF-8: ")
            utf(palavra)
        elif opcao == 6:
            expressao = input("Forneça a expressão a ser simplificada: ")
            simp_exp(expressao)
        else:
            print("Número inválido")
