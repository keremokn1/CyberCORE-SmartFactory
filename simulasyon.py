import os
import django
import time
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fabrika_merkezi.settings')
django.setup()

from uretim.models import Robot

print("--- Alpha Sanayi Canli Simulasyon Basladi ---")

durumlar = ['calisiyor', 'ariza', 'bakim']

try:
    while True:
        # Rastgele bir robot seç
        robotlar = Robot.objects.all()
        secilen_robot = random.choice(robotlar)
        yeni_durum = random.choice(durumlar)
        
        if secilen_robot.durum != yeni_durum:
            secilen_robot.durum = yeni_durum
            secilen_robot.ariza_notu = "Simulasyon tetiklendi." if yeni_durum == 'ariza' else ""
            secilen_robot.save() # Bu işlem otomatik olarak signal'i tetikler ve PDF raporuna gecer!
            print(f"Guncelleme: {secilen_robot.isim} su an {yeni_durum} modunda.")
        
        time.sleep(5) # Her 5 saniyede bir fabrikayi salla
except KeyboardInterrupt:
    print("Simulasyon durduruldu.")