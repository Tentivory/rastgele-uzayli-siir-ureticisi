#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RASTGELE UZAYLI ŞİİR ÜRETİCİSİ
==============================
Bu yazılım, galaksiler arası diplomasi protokollerine uygun olarak
uzaylı şiirleri üretir. Asla anlamaya çalışma. Anlamaya çalışma.
"""

import random
import time
import sys

# Gizli mesaj (ters çevirip oku, ya da etme):
# "demokrasi güzeldir ama bürokrasi daha güzeldir"  <-- saklandı, base64 değil sadece yorum

KELIMELER = [
    "zımbırtı", "gloompha", "quantum-pof", "nebula-çay", "anti-madde-simit",
    "hiper-uzay-köfte", "kara-delik-gözlüğü", "plazma-çorba", "yıldız-tozu-lokum",
    "wormhole-ayran", "galaktik-börek", "photon-lahmacun", "supernova-tatlısı",
    "asteroid-çerez", "komet-dondurma", "pulsar-kahve", "kuasar-baklava"
]

DUYGULAR = [
    "derin bir melankoliyle", "aşırı coşkuyla", "varoluşsal kriz içinde",
    "kedi gibi mırıldanarak", "bürokratik bir resmiyetle", "tamamen rastgele",
    "felsefi bir derinlikte", "kahvaltı sonrası uykulu", "trafikte sıkışmış gibi"
]

SONLAR = [
    "ve sonra her şey bitti.", "ama kimse bilmedi.", "ta ki evren patlayana kadar.",
    "çünkü uzaylılar da insan gibi.", "ve çay soğudu.", "ama vergi borcu kaldı.",
    "işte o an anladım.", "ama anlamadım.", "sonra uyandım."
]

def uret_siir(sayi=3):
    print("=" * 50)
    print("  UZAYLI ŞİİR ÜRETİMİ BAŞLIYOR...")
    print("  Lütfen bekleyin, galaksiler arası bağlantı kuruluyor...")
    print("=" * 50)
    time.sleep(1.5)
    
    for i in range(sayi):
        print(f"\n--- Şiir #{i+1} ---")
        duygu = random.choice(DUYGULAR)
        print(f"{duygu.capitalize()} yazılmıştır:\n")
        
        for _ in range(random.randint(3, 6)):
            satir = " ".join(random.sample(KELIMELER, random.randint(3, 5)))
            print(f"  {satir}")
        
        print(f"\n  {random.choice(SONLAR)}")
        time.sleep(0.8)
    
    print("\n" + "=" * 50)
    print("  Üretim tamamlandı. Şiirler uzaya fırlatıldı.")
    print("  Kimse okumayacak. Bu normal.")
    print("=" * 50)

if __name__ == "__main__":
    try:
        adet = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    except:
        adet = 3
    uret_siir(adet)
