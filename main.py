import requests
import random
import string

PROXY_HOST = ""
PROXY_PORT = ""
PROXY_USER = ""
PROXY_PASS = ""

def get_new_proxy():
    session_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    proxy_url = f"http://{PROXY_USER}-session-{session_id}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
    return {"http": proxy_url, "https": proxy_url}

def generate_and_download(text, voice="alloy"):
    url = "https://ttsmp3.com/makemp3_ai.php"
    
    payload = {
        "msg": text,
        "lang": voice,
        "source": "ttsmp3",
        "speed": "1.00"
    }
    
    headers = {
        "Referer": "https://ttsmp3.com/ai",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        proxies = get_new_proxy()
        print(f"Request එක යවනවා අලුත් IP එකකින්...")
        
        response = requests.post(url, data=payload, headers=headers, proxies=proxies, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success") == 1:
                audio_url = data.get("URL")
                print(f"Audio URL එක ලැබුණා: {audio_url}")
                
                print("Download")
                r = requests.get(audio_url)
                
                filename = f"audio_{voice}_{random.randint(1000,9999)}.mp3"
                with open(filename, "wb") as f:
                    f.write(r.content)
                print(f"done! File එක: {filename}")
            else:
                print("Site එකෙන් error එකක් ආවා:", data.get("error"))
        else:
            print(f"Request එක අසාර්ථකයි: {response.status_code}")

    except Exception as e:
        print(f"අවුලක් වුණා: {e}")

generate_and_download("hehe", "fable")
