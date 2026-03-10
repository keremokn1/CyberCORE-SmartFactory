from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Robot, Mesaj, ArizaKaydi
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas # pip install reportlab yapmadıysan terminalde yapmalısın

@login_required
def ana_sayfa(request):
    # Form gönderildiyse (Mesaj Sistemi)
    if request.method == "POST":
        isim = request.POST.get('isim')
        konu = request.POST.get('konu')
        icerik = request.POST.get('icerik')
        
        Mesaj.objects.create(isim=isim, konu=konu, icerik=icerik)
        return redirect('ana_sayfa')
     
    # Robotları ve İstatistikleri Çek
    robotlar = Robot.objects.all()
    toplam = robotlar.count()
    calisan = robotlar.filter(durum='calisiyor').count()
    arizali = robotlar.filter(durum='ariza').count()
    bakimda = robotlar.filter(durum='bakim').count()
    toplam_mesaj = Mesaj.objects.count()
    context = {
        'robotlar': robotlar,
        'toplam': toplam,
        'calisan': calisan,
        'arizali': arizali,
        'bakimda': bakimda,
        'mesaj_sayisi': toplam_mesaj,
    }
    return render(request, 'uretim/index.html', context)

@login_required
def pdf_rapor_olustur(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Alpha_Sanayi_Rapor.pdf"'
    
    p = canvas.Canvas(response)
    
    # Başlık
    p.setFont("Helvetica-Bold", 16)
    # Türkçe karakter sorunu için 'ı' yerine 'i' veya 'I' kullanabiliriz 
    # (Veya font kaydedebiliriz ama en hızlısı karakteri düzeltmek)
    p.drawString(100, 800, "Alpha Sanayi - Uretim Hatti Durum Raporu")
    
    p.setFont("Helvetica", 12)
    y = 750
    kayitlar = ArizaKaydi.objects.all().order_by('-tarih')[:25]
    
    if not kayitlar.exists():
        p.drawString(100, y, "Henuz bir durum degisikligi kaydi bulunmamaktadir.")
    else:
        p.drawString(100, y, "Son Durum Degisiklikleri:")
        y -= 30
        for kayit in kayitlar:
            tarih_str = kayit.tarih.strftime('%d/%m/%Y %H:%M')
            # Türkçe karakterleri manuel temizleyerek garantiye alalım
            satir = f"{tarih_str} - {kayit.robot.isim}: {kayit.eski_durum} -> {kayit.yeni_durum}"
            p.drawString(100, y, satir)
            y -= 20
            if y < 50:
                p.showPage()
                y = 800
                
    p.save()
    return response