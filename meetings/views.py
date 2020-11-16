from django.shortcuts import render

from .models import Meeting

def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})