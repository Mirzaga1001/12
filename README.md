# 📱 SMS Bomber (Simülasyon) - +994 Destekli

Bu proje, yalnızca **eğitim amaçlı** hazırlanmış sahte bir SMS bomber simülasyonudur. Gerçek SMS gönderimi yapmaz. Sadece terminalde mesaj gönderiyormuş gibi davranır.

> ⚠️ Bu araç gerçek SMS göndermez! Hiçbir servisle bağlantı kurmaz. Yalnızca Python öğrenimi ve simülasyon içindir.

## 🧾 Özellikler

- Yalnızca **+994** (Azerbaycan) ülke kodunu kabul eder.
- Gerçekçi mesaj gönderim gecikmesi simülasyonu.
- Kullanıcıdan mesaj içeriği ve gönderim sayısı alır.
- Renkli çıktı desteği (opsiyonel).

## 🚀 Kurulum (Termux için)

```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt
python sms_bomber.py
```

## 📝 Kullanım

Program çalıştırıldığında:

1. +994 ile başlayan 13 haneli bir numara girmeniz istenir.
2. Göndermek istediğiniz mesaj içeriğini yazarsınız.
3. Kaç adet sahte SMS göndermek istediğinizi girersiniz.

### Örnek:

```
Telefon numarası: +994502223344
Mesaj içeriği: Salam qaqa
Kaç SMS gönderilsin (simülasyon)?: 5
```

## ⚠️ Uyarı

- Bu script **gerçek SMS gönderimi yapmaz**.
- Gerçek servisler üzerinde denemeyin, API veya hizmet kurallarını ihlal etmeyin.
- Kötüye kullanım **yasadışıdır ve etik dışıdır.**

## 📂 Dosyalar

- `sms_bomber.py` - Ana Python simülasyon scripti
- `requirements.txt` - Gerekli modül listesi

---

**Yasal Uyarı:** Bu araç yalnızca kişisel eğitim/test ortamlarında kullanılmalıdır. Her türlü kötüye kullanım kullanıcının kendi sorumluluğundadır.
