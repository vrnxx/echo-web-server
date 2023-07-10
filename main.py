import socket

# Address Family INET, socket type STREAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Created the server socket. Recommended using port in range 1024 < XXXX
# to avoid conflicts with other applications
# like a Steam client, Discord ect
server.bind(('127.0.0.1', 2500))

# Set max incoming requests, if requests count will be greater 10 this requests will be dropped
server.listen(10)

# Check that the server is successful running
print('The server is running and waiting for a request')

# Ready to accept incoming request
client_socket, address = server.accept()

# Extract a data from request and decode data to utf-8
# Set a size of data to 1024 bytes
data = client_socket.recv(1024).decode('utf-8')

# Print the data from response in our server console
print(f'Request accepted, data: {data}')

# Create a response headers
HEADERS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

# Create a response to our client and encode it to utf-8
response_to_client = 'Request accepted. This message is a server response...'.encode('utf-8')

# Send a response to client
client_socket.send(HEADERS.encode('utf-8') + response_to_client)
