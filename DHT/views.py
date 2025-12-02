# views.py
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from .models import Dht11



def dashboard(request):
    return render(request, "dashboard.html")



def latest_json(request):
    last = Dht11.objects.order_by('-dt').values('temp', 'hum', 'dt').first()
    if not last:
        return JsonResponse({"detail": "no data"}, status=404)
    return JsonResponse({
        "temperature": last["temp"],
        "humidity":    last["hum"],
        "timestamp":   last["dt"].isoformat()
    })



# ============================
# 🚨 View to send alert message
# ============================
def send_alert(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=400)

    temperature = request.POST.get("temperature")
    humidity = request.POST.get("humidity")
    recipient_email = request.POST.get("email")  # where email is sent

    if not (temperature and humidity and recipient_email):
        return JsonResponse({"error": "Missing fields"}, status=400)

    # The message text
    alert_text = f"IoT Alert:\nTemperature: {temperature}°C\nHumidity: {humidity}%"

    # ----- SEND EMAIL -----
    try:
        send_mail(
            subject="IoT Sensor Alert",
            message=alert_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_email],   # <= WHERE EMAIL IS SENT
            fail_silently=False,
        )
    except Exception as e:
        print("Email sending error:", e)

    # ----- SEND TELEGRAM -----
    try:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(url, data={
            "chat_id": settings.TELEGRAM_CHAT_ID,   # <= WHERE TELEGRAM IS SENT
            "text": alert_text
        })
    except Exception as e:
        print("Telegram sending error:", e)

    return JsonResponse({"status": "Alert sent successfully!"})


def graph_temp(request):
    return render(request, "graph_temp.html")


def graph_hum(request):
    return render(request, "graph_hum.html")


def api_data(request):
    # Récupérer les 50 dernières lectures
    readings = Dht11.objects.order_by('-dt')[:50]
    # Inverser pour avoir l'ordre chronologique
    readings = reversed(readings)

    data = []
    for reading in readings:
        data.append({
            "temp": reading.temp,
            "hum": reading.hum,
            "dt": reading.dt.isoformat()
        })

    return JsonResponse({"data": data})