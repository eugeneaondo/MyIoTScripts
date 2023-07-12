import socket

# Define the request parameters
host = 'app.dtuip.com'
port = 1883
endpoint = '/api/device/getProtocolLabel'
headers = {
    'Host': 'app.dtuip.com',
    'Content-Type': 'application/json',
    'tlinkAppId': '6f678f69******283d6e7c6faf',
    'Authorization': 'Bearer 3f7908b4-b******a62dfafc'
}

# Create a socket object and establish a TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# Construct the request message
request = f"GET {endpoint} HTTP/1.1\r\n"
for header, value in headers.items():
    request += f"{header}: {value}\r\n"
request += "\r\n"

# Send the request
sock.sendall(request.encode())

# Receive and print the response
response = sock.recv(4096).decode()
print(response)

# Close the socket
sock.close()