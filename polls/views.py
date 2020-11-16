from django.shortcuts import render

from .models import Poll

def poll_detail(request, id):
    poll = Poll.objects.get(pk=id)
    return render(request, "polls/detail.html", {"poll": poll})
