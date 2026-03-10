from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Robot, ArizaKaydi

@receiver(pre_save, sender=Robot)
def durum_degisikligi_kaydet(sender, instance, **kwargs):
    if instance.id: # Eğer robot zaten varsa (yeni oluşturulmuyorsa)
        eski_robot = Robot.objects.get(id=instance.id)
        if eski_robot.durum != instance.durum:
            # Durum değişmiş! Kaydı oluştur:
            ArizaKaydi.objects.create(
                robot=instance,
                eski_durum=eski_robot.get_durum_display(),
                yeni_durum=instance.get_durum_display(),
                notlar=instance.ariza_notu or "Durum güncellendi."
            )