import requests
import os

# Danh sách các nguồn proxy
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

# Lấy tất cả proxy từ các nguồn
all_proxies = []
for source in PROXY_SOURCES:
    all_proxies.extend(fetch_proxies_from_url(source))

# Loại bỏ các proxy trùng lặp
all_proxies = list(set(all_proxies))

# Lưu vào file
os.makedirs("output", exist_ok=True)
file_path = "output/proxy_list.txt"
with open(file_path, "w") as f:
    f.write("\n".join(all_proxies))

print(f"[+] Saved {len(all_proxies)} proxies to {file_path}")

# Gửi file proxy tới Telegram group (tùy chọn)
def send_file_to_telegram(bot_token, chat_id, file_path):
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(
                f'https://api.telegram.org/bot{bot_token}/sendDocument',
                data={'chat_id': chat_id},
                files={'document': f}
            )
        if response.status_code == 200:
            print("[+] File sent to Telegram group successfully.")
        else:
            print(f"[-] Failed to send file to Telegram: {response.text}")
    except Exception as e:
        print(f"[-] Error sending file: {e}")

# Nếu cần gửi file qua Telegram
BOT_TOKEN = '8185929921:AAHnaIAgjDV1L0lZNyEx255uAcLP4IdMp-A' # Thay bằng Bot Token của bạn
CHAT_ID = '-1002390825493'      # Thay bằng Chat ID của nhóm
send_file_to_telegram(BOT_TOKEN, CHAT_ID, file_path)
