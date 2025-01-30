import requests
from faker import Faker
import random
import time
import os

# Configuration
PROXY_FILE = 'proxies.txt'
REFERRAL_FILE = 'referrals.txt'
USER_AGENTS_FILE = 'user_agents.txt'
BASE_URL = 'https://dashboard.layeredge.io/'

class ReferralBot:
    def __init__(self):
        self.fake = Faker()
        self.proxies = self.load_file(PROXY_FILE)
        self.user_agents = self.load_file(USER_AGENTS_FILE) or self.default_user_agents()
        self.setup_files()
        
    def default_user_agents(self):
        """Provide default user agents if file is missing"""
        return [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'
        ]
        
    def setup_files(self):
        os.makedirs('data', exist_ok=True)
        if not os.path.exists(USER_AGENTS_FILE):
            with open(USER_AGENTS_FILE, 'w') as f:
                f.write("\n".join(self.default_user_agents()))
        if not os.path.exists(REFERRAL_FILE):
            open(REFERRAL_FILE, 'w').close()
            
    def load_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        return []
    
    # Rest of the class remains the same until make_request
    
    def make_request(self, proxy=None):
        # Fixed user agent selection
        headers = {
            'User-Agent': random.choice(self.user_agents) if self.user_agents else 'Mozilla/5.0'
        }
        
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        try:
            response = requests.get(
                f"{BASE_URL}",
                headers=headers,
                proxies=proxies,
                timeout=10
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

# Rest of the code remains unchanged
