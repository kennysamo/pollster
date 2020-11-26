from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting, Room
from polls.models import Poll
# from polls.models import 


def welcome(request):
   # return HttpResponse("Welcome to SonySugar Web " + str(datetime.now()))
   # return render(request, "website/welcome.html", {"today": str(datetime.now())})
   return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all(),
                   "num_polls": Poll.objects.count(),
                   "today": str(datetime.now())})

def about(request):
    return HttpResponse("SonySugar is a world class manufacturer of sugar and its associated products.")