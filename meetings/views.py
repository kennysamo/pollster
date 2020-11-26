from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting, Room

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def room_list(request):
    # room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == 'POST':
        # form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("home")            
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})