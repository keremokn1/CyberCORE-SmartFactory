from django.db import models

class Robot(models.Model):
    DURUM_CHOICES = [
        ('calisiyor', 'Çalışıyor'),
        ('ariza', 'Arıza'),
        ('bakim', 'Bakımda'),
    ]

    isim = models.CharField(max_length=100) # Robotun adı (Örn: Robot-01)
    model = models.CharField(max_length=100) # Örn: Kaynak Robotu
    durum = models.CharField(max_length=20, choices=DURUM_CHOICES, default='calisiyor')
    ariza_notu = models.TextField(blank=True, null=True) # Arıza varsa sebebi buraya yazılacak
    son_bakim = models.DateTimeField(auto_now=True) # Otomatik tarih atar
    resim = models.ImageField(upload_to='robotlar/', blank=True, null=True)

    def __str__(self):
        return f"{self.isim} - {self.get_durum_display()}"
    
class ArizaKaydi(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name='kayitlar')
    eski_durum = models.CharField(max_length=20)
    yeni_durum = models.CharField(max_length=20)
    tarih = models.DateTimeField(auto_now_add=True)
    notlar = models.TextField(blank=True)

    def __str__(self):
        return f"{self.robot.isim} - {self.tarih.strftime('%d/%m %H:%M')}" 
     
class Mesaj(models.Model):
    isim = models.CharField(max_length=100)
    konu = models.CharField(max_length=200)
    icerik = models.TextField()
    okundu = models.BooleanField(default=False)
    tarih = models.DateTimeField(auto_now_add=True)      
    
    
    
    
    
    