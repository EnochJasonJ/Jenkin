from django.shortcuts import render , redirect , get_object_or_404
from .models import User
from .forms import UserForms

# Create your views here.
def view_list(request):
    people = User.objects.all()
    return render(request , 'index.html' , {'people': people})
def view_individual(request , pk):
    person = get_object_or_404(User , pk = pk)
    return render(request , 'individual.html' , {'person': person})

def create_view(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_list')
    else:
        form = UserForms()
    return render(request, 'create_view.html' , {'form':form})

def update_view(request , pk):
    person = get_object_or_404(User , pk = pk)
    if request.method == 'POST':
        form = UserForms(request.POST , instance=person)
        if form.is_valid():
            form.save()
            return redirect('view_list')
    else:
        form = UserForms(instance=person)
    return render(request, 'create_view.html' , {'form':form})
def delete_view(request , pk):
    person = get_object_or_404(User , pk = pk)
    if request.method == 'POST':
        person.delete()
        return redirect('view_list')
    
    return render(request , 'delete.html' , {'person': person})