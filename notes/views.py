from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from .models import Note
from .forms import NoteForm

# Create your views here.
def list(request):
    published = request.GET.get('published')
    if published:
        notes = Note.objects.filter(published=True).order_by('created_at')
    else:
        notes = Note.objects.all().order_by('created_at')
    
    paginator = Paginator(notes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'notes/list.html',{'notes':page_obj})

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = NoteForm()
    return render(request,'notes/create.html',{'form':form})