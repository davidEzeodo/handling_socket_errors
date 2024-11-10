import sys
import socket
import argparse


def main():
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action='store', dest='host', required=False, default='localhost')
    parser.add_argument('--port', action='store', dest='port', type=int, required=False, default=80)
    parser.add_argument('--file', action='store', dest='file', required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    try:
        soket.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

    try:
        msg = "GET %s HTTP/1.0\rn\n\r\n" % filename
        soket.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while 1:
        try:
            buf = soket.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf.decode('utf-8'))


if __name__ == '__main__':
    main()
