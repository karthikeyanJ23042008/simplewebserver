from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Device Information</title>
    </head>
    <body>
        <h2> KARTHIKEYAN J(26009634)</h2>
        <table border="1" cellspacing="5" cellpadding="15">
        <caption>Karthi Laptop Device Information</caption>

            <tr bgcolor="lime">
                <th>S.No.</th>
                <th>Device Name</th>
                <th>Device Info</th>
                <th>Details</th>
            </tr>

            <tr>
                <td>1</td>
                <td>Device Model</td>
                <td>TravelLite</td>
                <td>TL15-53M-G2</td>
            </tr>

            <tr>
                <td>2</td>
                <td>Product ID</td>
                <td>00342-42943-41971</td>
                <td>AAOEM</td>
            </tr>

            <tr>
                <td>3</td>
                <td>RAM</td>
                <td>Installed Memory</td>
                <td>16 GB</td>
            </tr>

            <tr>
                <td>4</td>
                <td>Graphics Card</td>
                <td>Intel Graphics</td>
                <td>128 MB</td>
            </tr>

            <tr>
                <td>5</td>
                <td>Storage</td>
                <td>Total Storage</td>
                <td>477 GB</td>
            </tr>

            <tr>
                <td>6</td>
                <td>Operating System</td>
                <td>Windows</td>
                <td>Windows 11 Home</td>
            </tr>

            <tr>
                <td>7</td>
                <td>System Type</td>
                <td>Operating System Type</td>
                <td>64-bit</td>
            </tr>

        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()