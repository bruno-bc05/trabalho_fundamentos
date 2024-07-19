import socket
from ieee754 import single  # código para padrão ieee754 https://github.com/canbula/ieee754
from sympy import symbols, to_cnf

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Servidor aguardando conexões na porta 12345...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Conexão estabelecida com {client_address}")

            data = client_socket.recv(1024).decode()
            received_data = data.split(maxsplit=1)
            prefix = received_data[0]

            if prefix == "convert" and len(received_data) == 2:
                original_base, original_number, target_base = map(int, received_data[1].split())
                original_number = int(original_number, original_base)
                converted_number = convert_base(original_number, target_base)
                client_socket.send(converted_number.encode())

            elif prefix == "math" and len(received_data) == 2:
                num1, num2, operation = received_data[1].split()
                num1 = int(num1, 2)
                num2 = int(num2, 2)
                result_bin = perform_math(num1, num2, operation)
                client_socket.send(result_bin.encode())

            elif prefix == "ieee754" and len(received_data) == 2:
                num1 = float(received_data[1])
                result = single(num1)
                client_socket.send(str(result).encode())

            elif prefix == "utf" and len(received_data) == 2:
                palavra = received_data[1]
                result = ' '.join(f'{ord(char):02x}' for char in palavra)
                client_socket.send(result.encode())

            elif prefix == "simp" and len(received_data) == 2:
                exp = received_data[1]
                a, b, c, d, e = symbols('a, b, c, d, e')
                result = to_cnf(eval(exp), True)
                client_socket.send(str(result).encode())

            else:
                client_socket.send("Dados inválidos. Formato incorreto.".encode())
        except Exception as e:
            client_socket.send(f"Ocorreu um erro: {e}".encode())
        finally:
            client_socket.close()
            print(f"Conexão com {client_address} encerrada")

def convert_base(number, target_base):
    if target_base == 10:
        return str(number)
    elif target_base == 2:
        return bin(number)[2:]
    elif target_base == 8:
        return oct(number)[2:]
    elif target_base == 16:
        return hex(number)[2:]
    else:
        return "Base inválida"

def perform_math(num1, num2, operation):
    if operation == '+':
        return bin(num1 + num2)[2:]
    elif operation == '-':
        return bin(num1 - num2)[2:]
    elif operation == '*':
        return bin(num1 * num2)[2:]
    elif operation == '/':
        if num2 != 0:
            return bin(num1 // num2)[2:]
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

if __name__ == "__main__":
    start_server()
