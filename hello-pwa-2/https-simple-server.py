import http.server, ssl, socketserver

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("cert.pem")
ip = '192.168.0.181'
server_address = (ip, 8080)

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(server_address, handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()