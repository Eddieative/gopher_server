import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9010)
sock.connect(addr)

try:
    message = 'testfile'
    sock.sendall(bytes(message.encode('utf-8')))

    r_text = ''

    while not r_text.endswith('.'):
        getData = sock.recv(1024)
        r_text += getData.decode('utf-8')

    print(r_text)

finally:
    print("closing socket")
    sock.close()
