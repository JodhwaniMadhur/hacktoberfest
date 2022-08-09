from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import cgi

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        data = json.dumps({'hello': 'world', 'received': 'ok'})
        data = data.encode(encoding='UTF-8')
        self.wfile.write(data)
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype,_ = cgi.parse_header(self.headers.get('Content-type'))
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        message = (self.headers.get('Content-length'))
        print(message)
        length = json.loads(self.rfile.read(len(message)))
        
        # add a property to the object, just to mess with data
        length['received'] = 'ok'
        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(length))
        return json.dumps({'response':200,'data_recieved':1})
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        