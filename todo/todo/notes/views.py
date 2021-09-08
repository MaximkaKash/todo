from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Notes index view")


from django.shortcuts import render
from notes.forms import AddNoteForm


def index(request):
    notes = []
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            # Create new DB record
            pass
    else:
        form = AddNoteForm()
    return render(request, "note_list.html", {"notes": notes, "form": form})
