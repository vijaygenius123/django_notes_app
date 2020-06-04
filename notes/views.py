from django.shortcuts import render


from .forms import NoteForm

# Create your views here.
def list(request):
    return render(request,'notes/list.html')

def create(request):
     return render(request,'notes/create.html')