import sys
import socket

size = 1024

def sendMessage(smtpServer, port, fromAddress, toAddress, message):
    IP = smtpServer
    PORT = int(port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))  # Open socket on port
    print(s.recv(size).decode())  # Display response

    # Send HELO command
    s.send(b'HELO ' + fromAddress.split('@')[1].encode() + b'\n')
    print(s.recv(size).decode())

    # Send MAIL FROM: command
    s.send(b'MAIL FROM:<' + fromAddress.encode() + b'>\n')
    print(s.recv(size).decode())

    # Send RCPT TO: command
    s.send(b'RCPT TO:<' + toAddress.encode() + b'>\n')
    print(s.recv(size).decode())

    # Send DATA command
    s.send(b"DATA\n")
    print(s.recv(size).decode())

    # Send email content
    s.send(message.encode() + b'\n')

    # Send end of data
    s.send(b'\r\n.\r\n')
    print(s.recv(size).decode())  # Display response

    # Send QUIT command
    s.send(b'QUIT\n')
    print(s.recv(size).decode())  # Display response

    s.close()

def main(args):
    smtpServer = args[1]
    port = args[2]
    fromAddress = args[3]
    toAddress = args[4]
    message = args[5]
    sendMessage(smtpServer, port, fromAddress, toAddress, message)

if __name__ == "__main__":
    main(sys.argv)
