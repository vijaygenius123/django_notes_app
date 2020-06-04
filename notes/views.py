from django.shortcuts import render, redirect


from .models import Note
from .forms import NoteForm

# Create your views here.
def list(request):
    notes = Note.objects.all()

    return render(request,'notes/list.html',{'notes':notes})

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = NoteForm()
    return render(request,'notes/create.html',{'form':form})