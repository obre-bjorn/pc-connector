import socket 

target_host = '127.0.0.1'
target_port = 9988

#Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host,target_port))

# send some data
client.send(b' ABCDEf')
response = client.recv(4096)

print(response.decode())
client.close()