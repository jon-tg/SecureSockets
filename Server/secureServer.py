import subprocess
import socket
import os
import ssl

serverKey = "server.key"
clientCert = "../Certs/client.crt"
serverCert = "../Certs/server.crt"
port = 8080

if (not os.path.exists(serverCert) or not os.path.exists(serverKey)):
        subprocess.run(["./serverKeyGen.sh"], check=True) # Generate server private key and certificate

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile=clientCert)
context.load_cert_chain(certfile=serverCert, keyfile=serverKey)
context.options |= ssl.OP_SINGLE_ECDH_USE
context.minimum_version = ssl.TLSVersion.TLSv1_3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	sock.bind(('', port))
	sock.listen(1)
	with context.wrap_socket(sock, server_side=True) as ssock:
		conn, addr = ssock.accept()
		clientIP, clientPort = addr
		message = conn.recv(1024).decode()
		print(clientIP + " says: " + message)
		conn.send(message.encode())
