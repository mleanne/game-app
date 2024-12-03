import socket

def lowercase_service():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)
    print("Server running and listening for incoming connections on 8000...")

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

                    print("Received: ", data.decode())

                    # Process data (convert to lowercase)
                    processed_data = data.decode().lower()

                    # Send processed data back to main program
                    client_socket.sendall(processed_data.encode())
                    print("Sent: ", processed_data)

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
    lowercase_service()
