from django.shortcuts import render
import threading



def index(request):
    print(threading.get_native_id())
    return render(request, "chatapp/index.html")

# Create your views here.
def room(request, room_name):
    return render(request, "chatapp/room.html", {"room_name": room_name})