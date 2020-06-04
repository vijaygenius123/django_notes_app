from django.shortcuts import render


from .forms import NoteForm

# Create your views here.
def list(request):
    return render(request,'notes/list.html')

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'notes/list.html')
    form = NoteForm()
    return render(request,'notes/create.html',{'form':form})