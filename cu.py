import requests
import os
import time
from datetime import datetime

# Danh sách nguồn proxy
PROXY_SOURCES = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/proxies.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt"
]

# Hàm tải proxy từ URL
def fetch_proxies_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        proxies = response.text.splitlines()
        print(f"[+] Fetched {len(proxies)} proxies from {url}")
        return proxies
    except Exception as e:
        print(f"[-] Failed to fetch from {url}: {e}")
        return []

# Hàm gửi file qua Telegram với caption
def send_file_to_telegram(bot_token, chat_id, file_path, file_type, proxy_count):
    try:
        caption = f"Proxy Type: {file_type}\nTotal Proxies: {proxy_count}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nOwner: @ventoxdeptrai"
        with open(file_path, 'rb') as f:
            response = requests.post(
                f'https://api.telegram.org/bot{bot_token}/sendDocument',
                data={'chat_id': chat_id, 'caption': caption},
                files={'document': f}
            )
        if response.status_code == 200:
            print(f"[+] {file_type} file sent to Telegram successfully.")
        else:
            print(f"[-] Failed to send {file_type} file to Telegram: {response.text}")
    except Exception as e:
        print(f"[-] Error sending {file_type} file: {e}")

# Lấy tất cả proxy từ các nguồn và phân loại
http_proxies = []
https_proxies = []
socks4_proxies = []
socks5_proxies = []

for source in PROXY_SOURCES:
    proxies = fetch_proxies_from_url(source)
    for proxy in proxies:
        if "http" in source:
            http_proxies.append(proxy)
        elif "https" in source:
            https_proxies.append(proxy)
        elif "socks4" in source:
            socks4_proxies.append(proxy)
        elif "socks5" in source:
            socks5_proxies.append(proxy)

# Lưu vào các file riêng biệt
os.makedirs("output", exist_ok=True)

http_file_path = "output/http_proxies.txt"
with open(http_file_path, "w") as f:
    f.write("\n".join(http_proxies))

https_file_path = "output/https_proxies.txt"
with open(https_file_path, "w") as f:
    f.write("\n".join(https_proxies))

socks4_file_path = "output/socks4_proxies.txt"
with open(socks4_file_path, "w") as f:
    f.write("\n".join(socks4_proxies))

socks5_file_path = "output/socks5_proxies.txt"
with open(socks5_file_path, "w") as f:
    f.write("\n".join(socks5_proxies))

print(f"[+] Saved proxies to files.")

# Cập nhật thông tin Telegram Bot và Chat ID
BOT_TOKEN = '8185929921:AAHnaIAgjDV1L0lZNyEx255uAcLP4IdMp-A' # Thay bằng Bot Token của bạn
CHAT_ID = '-1002390825493'      # Thay bằng Chat ID của nhóm

# Gửi các file qua Telegram
send_file_to_telegram(BOT_TOKEN, CHAT_ID, http_file_path, "HTTP", len(http_proxies))
send_file_to_telegram(BOT_TOKEN, CHAT_ID, https_file_path, "HTTPS", len(https_proxies))
send_file_to_telegram(BOT_TOKEN, CHAT_ID, socks4_file_path, "SOCKS4", len(socks4_proxies))
send_file_to_telegram(BOT_TOKEN, CHAT_ID, socks5_file_path, "SOCKS5", len(socks5_proxies))