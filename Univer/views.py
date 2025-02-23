from django.shortcuts import render, get_object_or_404
from .models import Kompaniya, Avtomabil


def index(request):
    kompaniya = Kompaniya.objects.all()
    avtomabil = Avtomabil.objects.all()

    return render(request, 'news/index.html', {'Kompaniya': kompaniya, 'avtomabil': avtomabil})


def komp_avto(request, kompaniya_id):
    kompaniya = get_object_or_404(Kompaniya, pk=kompaniya_id)  # Tanlangan kompaniya
    avtomabil = Avtomabil.objects.filter(kompaniya=kompaniya)  # Shu kompaniyaga tegishli avtomabillar
    barcha_kompaniyalar = Kompaniya.objects.all()  # 🔥 Kompaniyalar ro‘yxatini olish

    context = {
        "kompaniya": kompaniya,  # Tanlangan kompaniya
        "avtomabil": avtomabil,  # Shu kompaniyaga tegishli avtomabillar
        "kompaniyalar": barcha_kompaniyalar,  # 🔥 Barcha kompaniyalar
        "tanlangan_kompaniya_id": kompaniya_id  # ✅ Tanlangan kompaniya ID si
    }

    return render(request, 'news/index.html', context)

def avtomabil_detail(request, avtomabil_id):
    avtomabil = get_object_or_404(Avtomabil, id=avtomabil_id)

    context = {
        "avtomabil": avtomabil
    }
    return render(request, 'news/avtomabil_detail.html', context)

def home(request):
    kompaniyalar = Kompaniya.objects.all()  # 🔥 Barcha kompaniyalar

    context = {
        "kompaniyalar": kompaniyalar  # ✅ Kompaniyalar ro‘yxatini template ga yuborish
    }
    return render(request, 'news/index.html', context)
