import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = 'localhost'
port = 5002

sheepValue = 0
currentSheep = 0
sheeptoUSD = 0
currentUSD = 0
USDtosheep = 0
get1 = True
get2 = True
get3 = True

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print "Server listening on {}:{}".format(host, port)
print ""

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print 'Got connection from', addr

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)

        if not data:
            break

        # Convert received data to integer
        received_integer = int(data)

        if received_integer == 1 and get1 == True:
            print "<SET SHEEP> Set Sheep Value started with:", received_integer
            print "\nNext integer entered will be value of sheep per USD (Ex: 10 sheep to 1 USD)"
            # Set the flag to indicate that the next incoming integer should be stored
            store_next_integer = 1
            get1 = False
            get2 = False
            get3 = False

        elif received_integer == 2 and get2 == True:
            print "<SHEEP TO USD> Sheep to USD started with:", received_integer
            print "\nNext integer entered will be how many sheep you want converted to USD"
            # Set the flag to indicate that the next incoming integer should be stored
            store_next_integer = 2
            get2 = False
            get1 = False
            get3 = False

        elif received_integer == 3 and get3 == True:
            print "<USD TO SHEEP> USD to sheep started with:", received_integer
            print "\nNext integer entered will be how many USD you want converted to sheep"
            # Set the flag to indicate that the next incoming integer should be stored
            store_next_integer = 3
            get3 = False
            get1 = False
            get2 = False

        elif store_next_integer == 1:
            # Store the next incoming integer
            sheepValue = received_integer
            print "\nSheep Value Set: ", sheepValue
            # Reset the flag to indicate that the server should go back to normal operation
            store_next_integer = None
            get1 = True
            get2 = True
            get3 = True

        elif store_next_integer == 2:
            # Store the next incoming integer
            currentSheep = received_integer
            print "\nSheep you want converted:", currentSheep
            print "With a value of ", sheepValue, " sheep per USD..."
            sheeptoUSD = currentSheep // sheepValue

            print "\nYour sheep are worth ", sheeptoUSD, " USD's"
            # Reset the flag to indicate that the server should go back to normal operation
            store_next_integer = None
            get1 = True
            get2 = True
            get3 = True

        elif store_next_integer == 3:
            # Store the next incoming integer
            currentUSD = received_integer
            print "\nUSD's you want converted:", currentUSD
            print "With a value of ", sheepValue, " sheep per USD..."
            USDtosheep = currentUSD * sheepValue

            print "\nYour USD's are worth ", USDtosheep, " sheep"
            # Reset the flag to indicate that the server should go back to normal operation
            store_next_integer = None
            get1 = True
            get2 = True
            get3 = True

        else:
            print "No Logic for integer recieved: ", received_integer
            # Implement your default logic here for other received integers
            # For demonstration, let's just print the received integer

        

        


        # Your logic here for what the server should do with the received integer
        # For demonstration, let's just print the received integer

        #print "Input Received: ", received_integer

    # Close the connection with the client
    client_socket.close()



