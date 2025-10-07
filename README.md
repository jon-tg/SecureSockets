Establishes a TLS 1.3 encrypted socket connection between a client and server. Both sides use mutual authentication with certificates — the server verifies the client, and the client verifies the server. The server echoes whatever message the client sends.

Usage:

First, generate keys and certificates by running ./serverKeyGen.sh and ./clientKeyGen.sh.

Run server.py to start the secure echo server (port 8080 by default).

Run client.py <hostname> (e.g., localhost or 127.0.0.1).

Type a message and the server will send it back encrypted over TLS.

If the required .key or .crt files don’t exist, the scripts automatically call their respective key generation scripts.
