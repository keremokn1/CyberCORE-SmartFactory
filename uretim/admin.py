from django.contrib import admin
from .models import Robot

@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ('isim', 'model', 'durum', 'son_bakim') # Listede görünecek sütunlar
    list_filter = ('durum',) # Sağ tarafa durum filtresi ekler
    search_fields = ('isim', 'model') # Arama çubuğu ekler