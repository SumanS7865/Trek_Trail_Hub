from django.shortcuts import render
from .models import TrekkingGear  # हाम्रो मोडल ल्याएको


def home(request):
    gears = TrekkingGear.objects.all()  # Database बाट सबै सामान तानेको
    return render(request, "home.html", {gears: gears})  # HTML मा पठाएको
