import socket
from ieee754 import single  # código para padrão ieee754 https://github.com/canbula/ieee754
from sympy import symbols, simplify_logic

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
            received_data = data.split()
            prefix = received_data[0]

            if prefix == "convert" and len(received_data) == 4:
                original_base = int(received_data[1])
                original_number = received_data[2]
                target_base = int(received_data[3])
                number_in_base_10 = int(original_number, original_base)
                converted_number = convert_base(number_in_base_10, target_base)
                client_socket.send(converted_number.encode())

            elif prefix == "math" and len(received_data) == 4:
                num1 = int(received_data[1], 2)
                num2 = int(received_data[2], 2)
                operation = received_data[3]
                max_bits = max(len(received_data[1]), len(received_data[2]))
                result_bin = perform_math(num1, num2, operation, max_bits)
                client_socket.send(result_bin.encode())

            elif prefix == "ieee754" and len(received_data) == 2:
                num1 = float(received_data[1])
                result = single(num1)
                client_socket.send(str(result).encode())

            elif prefix == "utf" and len(received_data) == 2:
                palavra = received_data[1]
                result = ' '.join(f'{ord(char):02x}' for char in palavra)
                client_socket.send(result.encode())

            elif prefix == "simp":
                exp = ' '.join(received_data[1:])
                a, b, c, d, e = symbols('a b c d e')
                try:
                    result = simplify_logic(exp, form='cnf')
                    client_socket.send(str(result).encode())
                except Exception as e:
                    client_socket.send(f"Ocorreu um erro na simplificação: {e}".encode())

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

def perform_math(num1, num2, operation, max_bits):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 // num2
        else:
            return "Erro: Divisão por zero".zfill(max_bits)
    else:
        return "Operação inválida".zfill(max_bits)
    
    return format(result, f'0{max_bits}b')

if __name__ == "__main__":
    start_server()
