import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fabrika_merkezi.settings')
django.setup()

from uretim.models import Robot

modeller = ['A-100', 'B-200', 'X-Interceptor', 'Alpha-Core', 'Titan-V8']
durumlar = ['calisiyor', 'ariza', 'bakim']

for i in range(1, 21):
    Robot.objects.create(
        isim=f"Robot-Alpha-{i:02d}",
        model=random.choice(modeller),
        durum=random.choice(durumlar),
        ariza_notu="Sistem kontrolü yapıldı." if i % 5 == 0 else ""
    )

print("20 Yeni Robot Basariyla Fabrikaya Eklendi!")