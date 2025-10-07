import socket
import subprocess
import sys
import ssl
import os

clientKey = "client.key"
clientCert = "../Certs/client.crt"
serverCert = "../Certs/server.crt"
port = 8080

if (not os.path.exists(clientKey) or not os.path.exists(clientCert)):
	subprocess.run(["./clientKeyGen.sh"], check=True) # Generate client private key and certificate

hostname = sys.argv[1]
context = ssl.SSLContext(ssl.PROTOCOL_TLS, cafile=serverCert)
context.load_cert_chain(certfile=clientCert, keyfile=clientKey)
context.load_verify_locations(cafile=serverCert)
context.verify_mode = ssl.CERT_REQUIRED
context.options |= ssl.OP_SINGLE_ECDH_USE
context.minimum_version = ssl.TLSVersion.TLSv1_3

with socket.create_connection((hostname, port)) as sock:
	with context.wrap_socket(sock, server_side=False, server_hostname=hostname) as ssock:
		print(ssock.version())
		message = input("Please enter your message: ")
		ssock.send(message.encode())
		receives = ssock.recv(1024).decode()
		print(receives)
