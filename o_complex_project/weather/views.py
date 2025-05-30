from django.shortcuts import render
from.models import Town
from django.utils import timezone
from .weather_service import get_weather
import datetime
from .ai_service import generate_fact


def home(request):
    context = {}
    context["towns"] = Town.objects.all()
    if request.method == "POST":
        form_town = str(request.POST["town"]).capitalize()
        database_town = Town.objects.filter(title=form_town).first()
        if database_town is None:
            weather = get_weather(form_town)
            if weather != "Ошибка на стороне сервера. Извините...":
                database_town = Town(
                    title=form_town,
                    weather=get_weather(form_town),
                    scan_time=timezone.now(),
                    fact=generate_fact(form_town))
            else:
                return render(request, "weather/home.html", context)
        elif timezone.now() - database_town.scan_time > datetime.timedelta(minutes=20):
            database_town.weather = get_weather(database_town.title)
            database_town.fact = generate_fact(database_town.title)
            database_town.scan_time = timezone.now()
            
        database_town.cnt += 1
        database_town.save()
        context["current_town"] = database_town
            
    return render(request, "weather/home.html", context)