import socket
import tqdm
import os
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6969
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
while True:
  client_socket, address = s.accept() 
  print(f"[+] {address} is connected.")
  #receive file
  received = client_socket.recv(BUFFER_SIZE).decode()
  filename, filesize, kode = received.split(SEPARATOR)
  filename = os.path.basename(filename)
  filesize = int(filesize)
  filename = "Data Base.csv"
  progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
  if kode=="upload":
    with open(filename, "ab") as f:
      while True:
          bytes_read = client_socket.recv(BUFFER_SIZE)
          if not bytes_read:    
              break
          f.write(bytes_read)
          progress.update(len(bytes_read))
  elif kode=="update":
    with open(filename, "wb") as f:
      while True:
          bytes_read = client_socket.recv(BUFFER_SIZE)
          if not bytes_read:    
              break
          f.write(bytes_read)
          progress.update(len(bytes_read))
  #send file
  elif kode == "download":
    with open(filename, "rb") as f:
      while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
          break
        client_socket.sendall(bytes_read)
        progress.update(len(bytes_read))
  client_socket.close()
s.close()