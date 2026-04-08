import random
import string
import os

class Randomizer:
    def __init__(self):
        self.ua_file = "payloads/user_agents.txt"
        self.ref_file = "payloads/referers.txt"
        self._cache_ua = self._load_file(self.ua_file)
        self._cache_ref = self._load_file(self.ref_file)

    def _load_file(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        return ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"]

    def get_random_ua(self):
        return random.choice(self._cache_ua)

    def get_random_referer(self):
        return random.choice(self._cache_ref)

    def get_random_ip(self):
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

    def random_string(self, length=10):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))

    def random_choice(self, list_obj):
        return random.choice(list_obj)

    def random_int(self, min_val, max_val):
        return random.randint(min_val, max_val)