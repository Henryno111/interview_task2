import http.server
import socketserver

PORT = 8000

class BasicHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""<!DOCTYPE html>
<html>
<head>
<title>python web page</title>
<style>
body {
  font-size: 15px;
  font-family: cursive;
  background-color: grey;
}
h1 {
  text-align: center;
  margin-top: 50px;
}
p {
  text-align: center;
  margin-top: 20px;
}
table, th, td {
 border: 1px solid black;
}
</style>
</head>
<body>
<h1>Election results table Delta state/h1>
<p>Page of election result in delta</p>
<table style:"width= 100%">
<tr>
<th>Political party</th>
<th>Total votes</th>
</tr>
<tr>
<td>PDP</td>
<td>1075</td>
</tr>
<tr>
<td>DPP</td>
<td>68</td>
</tr>
<tr>
<td>ACN</td>
<td>617</td>
</tr>
<tr>
<td>PPA</td>
<td>831</td>
</tr>
<tr>
<td>CDC</td>
<td>253</td>
</tr>
<tr>
<td>JP</td>
<td>721</td>
</tr>
<tr>
<td>ANPP</td>
<td>798</td>
</tr>
<tr>
<td>LABO</td>
<td>774</td>
</tr>
<tr>
<td>CPP</td>
<td>428</td>
</tr>
</table>
</body>
</html>""")
        else:
            self.send_error(404, 'Not Found')

with socketserver.TCPServer(('', PORT), BasicHTTPRequestHandler) as httpd:
    print(f'Serving on port {PORT}')
    httpd.serve_forever()
