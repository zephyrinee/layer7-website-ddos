try:
    import socks
    import socket
    SOCKS_AVAILABLE = True
except ImportError:
    SOCKS_AVAILABLE = False

def create_socks_connection(proxy_host, proxy_port, proxy_type=None):
    if not SOCKS_AVAILABLE:
        return None
    if proxy_type is None:
        proxy_type = socks.SOCKS5
    s = socks.socksocket()
    s.set_proxy(proxy_type, proxy_host, proxy_port)
    return s

def set_default_proxy(proxy_host, proxy_port, proxy_type=None):
    if SOCKS_AVAILABLE:
        if proxy_type is None:
            proxy_type = socks.SOCKS5
        socks.set_default_proxy(proxy_type, proxy_host, proxy_port)
        socket.socket = socks.socksocket
        return True
    return False