"""
URL configuration for fabrika_merkezi project.
"""
from django.contrib import admin
from django.urls import path
from uretim import views 
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ana_sayfa, name='ana_sayfa'), 
    
    
    path('rapor-indir/', views.pdf_rapor_olustur, name='pdf_rapor'),
    
   
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Paneli Özelleştirmeleri
admin.site.site_header = "Alpha Sanayi Kontrol Merkezi"
admin.site.site_title = "Alpha Sanayi Admin Paneli"
admin.site.index_title = "Fabrika Robot Takip Sistemi"