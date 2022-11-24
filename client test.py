import socket

HOST = 'server ip'        
PORT = 42050              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
f = open('my.csv', 'rb')
print ("Sending Data ....")
l = f.read()
while True:      
    for line in l:
        s.send(line)    
    break
f.close()
print ("Sending Complete")
s.close()