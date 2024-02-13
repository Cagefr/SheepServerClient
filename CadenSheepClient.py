import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = 'localhost'
port = 5002


# Connect to server
client_socket.connect((host, port))

while True:
    # Get integer input from user
    integer_input = raw_input("Enter an integer (1-3 = sheep logic) to send to server (or 'exit' to quit): ")

    if integer_input.lower() == 'exit':
        break

    try:
        # Send integer data to server
        client_socket.sendall(integer_input)
    except:
        print "Failed to send data to server"

# Close the connection
client_socket.close()






