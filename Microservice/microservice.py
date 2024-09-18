import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
server_socket.bind(server_address)
server_socket.listen(5)
try:
    while True:
        connection, client_address = server_socket.accept()
        try:
            received_val = connection.recv(10)
            print(f'value received: {received_val}')
            if received_val:
                kelvin = float(received_val.decode())
                celsius = kelvin - 273.15
                connection.sendall(str(celsius).encode())
                print(f'value converted and passed: {celsius}')
                connection.close()
        finally:
            connection.close()
except KeyboardInterrupt:
    print("Server Shutting Down.")
finally:
    server_socket.close()
