import socket
import logging
from Gopher import Gopher

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9010)
sock.bind(addr)

sock.listen(1)
while True:
    connection, client_address = sock.accept()
    try:
        while True:
            gopher_protocol = Gopher()
            data = connection.recv(1024)
            if data:
                gopher_protocol.resolve_gquery(data.decode("utf-8"))
                getData = gopher_protocol.get_result_strings()
                connection.sendall(bytes(getData.encode("utf-8")))
            else:
                break

    finally:
        connection.close()
