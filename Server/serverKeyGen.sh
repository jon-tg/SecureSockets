#!/bin/bash

openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out ../Certs/server.crt
