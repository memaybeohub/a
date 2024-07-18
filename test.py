from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Xin chào! Host của bạn đang hoạt động!</h1></body></html>")

HOST_NAME = ""  # Địa chỉ IP hoặc tên miền của host (để trống nếu chạy trên localhost)
PORT = 8000  # Cổng mà bạn muốn máy chủ lắng nghe

if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, PORT), SimpleHTTPRequestHandler)
    print(f"Máy chủ đang chạy tại http://{HOST_NAME}:{PORT}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Máy chủ đã dừng.")
