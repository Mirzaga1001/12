import time
import random
import sys

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
        count = int(input("Kaç SMS gönderilsin (simülasyon)?: "))
    except ValueError:
        print("[X] Geçerli bir sayı girilmedi!")
        sys.exit()

    for i in range(count):
        print(f"\n[+] {i+1}. SMS")
        send_fake_sms(phone, message)

if __name__ == "__main__":
    main()
