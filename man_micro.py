import socket
import random

def mancala_computer():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_address = ('localhost', 8075)
    server_socket.bind(server_address)
    print("Server running and listening for incoming connections on 8075...")

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
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    # Process data (convert to lowercase)
                    data = data.decode()
                    print("data received: ", data)
                    if data == 'same':    # computer will choose from its own side
                        random_number = random.randint(7,12)
                        print("num: ", random_number)
                        client_socket.sendall(str(random_number).encode())
                    elif data == 'other':                #computer side empty so will chose from player's side
                        random_number = random.randint(1, 6)
                        print("num: ", random_number)
                        client_socket.sendall(str(random_number).encode())

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
    mancala_computer()