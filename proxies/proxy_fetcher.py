import requests

class ProxyFetcher:
    def __init__(self):
        self.proxies = []
        self.sources = [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt"
        ]

    def fetch(self, limit=50):
        for url in self.sources:
            try:
                resp = requests.get(url, timeout=10)
                lines = resp.text.split('\n')
                for line in lines[:limit]:
                    if '.' in line and ':' in line:
                        self.proxies.append(line.strip())
            except:
                pass
        return self.proxies