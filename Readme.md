# Pybical

## INTRODUCTION

Pybical is a logical framework which is easy-to-learn and has transparent and in-built code. It will work on the basis of request and response. It has it's own server which gives more transparency to developer for working. After some version, we will be working on quantam computing web application.

- [X] HTTP Server (pending)
- [ ] HTTPS Server (pending)
- [X] Socket Server
- [ ] Quantam Computing

## HTTP Server

HTTP Server is a main web server. This will support the some of the feature

1. Routing
2. Virtual Path
3. CSRF Protection
4. Session
5. Request
6. Response
7. Logging
8. Error Handling
9. URL Generating
10. Programming Logic
11. System Controls (SSH)
12. Environmental variable [Maybe]

This command will lunch the server and run on PORT 80 and URL `http://localhost`

```python
 python main.py
```

## Socket Server

Socket server is full-duplex communication of server and clients. Client can communicate to server in real-time. It's specially made for chats app. The host of the socket is `127.0.0.1` and it will run in port `1289` by default.

This command will be lunch the server.

```python
python socket_server.py
```

## Socket Client

Socket Client is way to communicate with server with other clients. It will run only when the socket server is listening. It has by default connection with our socket server.

This command will help to commnicate the other client of the server

```python
python server_client.py
```

## To-do

### 1. Configuration File

Configuration file will be in YAML. `pybical.yaml` will be the whole system configuration and version of the package (Requirements).`web.pybical.yaml` will be the web configuration.
It helps to enable/disable feature of the system. `data.pybical.yaml` will be database connector.

### 2 Routing.json

`Routing.json` helps to route the request of URI. It will help you to redirect and render the request. It will be by default off.

### 3 Virtual.path.json

`Virtual.path.json` is te logical path to access the file which is pointed to from outside of the Pybical application folder. It will be by default off.

## Other Programming Language

All programming language has its special and unique feature. For now, Python will be taken as priority. We will be taking other programming language like `C`, `C++`, `PHP`, `Java`, `Rust`, and `R`.

### Why PHP is being use?

PHP is server-side scripting powerful language. It will give more secure and powerful service. Application can easily be loaded which are based on PHP and connected to database. It’s mainly used due to its faster rate of loading over slow internet speed than another programming language.  

### Why R is being use?

R is a programming language for statistical computing. It helps to solve big data. It will be helpful for data trafficking because it is full stack application.

### What about library related to given other programming language?

Library using developers will be discouraged. All the library are made from its own language. So, It just help to show your emotions not talent. If you have your own library, then you may be consider if it is suitable with application's performance. We hate to be depending to other's third party library.

### What about Quantam Computing in web?

Quantam Computer are more powerful then world best super computer. It can solve biggest problem in millisecond which binary best supercomputer take it millennia. Quantam Computing will help to solve the small problem in zeptosecond.
