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
        self.user_agents = self.load_file(USER_AGENTS_FILE)
        self.setup_files()
        
    def setup_files(self):
        os.makedirs('data', exist_ok=True)
        if not os.path.exists(REFERRAL_FILE):
            open(REFERRAL_FILE, 'w').close()
            
    def load_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        return []
    
    def get_random_proxy(self):
        return random.choice(self.proxies) if self.proxies else None
    
    def generate_fake_data(self):
        """Generates placeholder data (NOT real cryptographic data)"""
        return {
            'wallet_address': self.fake.sha256(),
            'phrase_key': ' '.join(self.fake.words(nb=12)),
            'private_key': self.fake.sha256()
        }
    
    def save_referral(self, data):
        with open(REFERRAL_FILE, 'a') as f:
            f.write(f"[{time.ctime()}] New entry:\n")
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
            f.write("-" * 50 + "\n")
    
    def make_request(self, proxy=None):
        headers = {'User-Agent': random.choice(self.user_agents) or 'Mozilla/5.0'}
        
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        try:
            # PLACEHOLDER: Actual API interaction would go here
            response = requests.get(
                f"{BASE_URL}api-endpoint",  # Replace with real endpoint
                headers=headers,
                proxies=proxies,
                timeout=10
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
    
    def run(self):
        print("Starting demo mode...")
        while True:
            proxy = self.get_random_proxy()
            wallet_data = self.generate_fake_data()
            
            print(f"Attempting request with proxy: {proxy or 'No proxy'}")
            
            if self.make_request(proxy):
                self.save_referral(wallet_data)
                print("Demo entry saved")
            else:
                print("Request simulation failed")
            
            time.sleep(random.uniform(5, 15))

if __name__ == '__main__':
    bot = ReferralBot()
    bot.run()
