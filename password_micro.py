import socket
import random
import string



def random_password():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_address = ('localhost', 8050)
    server_socket.bind(server_address)
    print("Server running and listening for incoming connections on 8050...")

    # Listen for incoming connections
    server_socket.listen(1)

    try:
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print("Connected to main program:", client_address)

            try:
                while True:
                    # Receive data from main program
                    length = client_socket.recv(1024)

                    if not length:
                        break

                    length = length.decode()
                    x = int(length)
                    print("data received: ", x)



                    letters = string.ascii_letters
                    password = ''.join(random.choice(letters) for _ in range(x))
                    print("suggested password: ", password)

                    client_socket.sendall(password.encode())

            finally:
                # Clean up the connection
                client_socket.close()
                print("Connection with main program closed")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed")

if __name__ == "__main__":
    random_password()