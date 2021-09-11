from django.http import HttpResponse
from django.shortcuts import render
import json
from notes.forms import AddNoteForm
from notes.models import Note


def index(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
    else:
        form = AddNoteForm()
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes, "form": form})


# def data(request):
#     notes = [x.data() for x in Note.objects.all()]
#     return HttpResponse(json.dumps(notes))


def data(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
    else:
        form = AddNoteForm()
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes, "form": form})
