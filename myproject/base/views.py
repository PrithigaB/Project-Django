from django.shortcuts import render,redirect
from .models import * 


# HOME PAGE
def home(request):
    data = Taskmodel.objects.all()
    return render(request, 'home.html', {'data': data})


# ADD TASK
def add(request):
    if request.method == 'POST':
        Taskmodel.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
        return redirect('home')
    return render(request, 'add.html')


# UPDATE TASK
def update(request, pk):
    data = Taskmodel.objects.get(id=pk)
    if request.method == 'POST':
        data.title = request.POST['title']
        data.desc = request.POST['desc']
        data.save()
        return redirect('home')
    return render(request, 'update.html', {'data': data})


# DELETE FROM HOME → MOVE TO TRASH
def delete(request, pk):
    data = Taskmodel.objects.get(id=pk)
    Trashmodel.objects.create(
        title=data.title, 
        desc=data.desc)
    data.delete()
    return redirect('home')


# COMPLETE FROM HOME → MOVE TO COMPLETE
def complete_(request, pk):
    data = Taskmodel.objects.get(id=pk)
    Completemodel.objects.create(
        title=data.title, 
        desc=data.desc
        )
    data.delete()
    return redirect('home')


# COMPLETE PAGE
def complete(request):
    data = Completemodel.objects.all()
    return render(request, 'complete.html', {'data': data})


# RESTORE FROM COMPLETE → HOME
def crestore(request, pk):
    data = Completemodel.objects.get(id=pk)
    Taskmodel.objects.create(
        title=data.title, 
        desc=data.desc
        )
    data.delete()
    return redirect('complete')


# DELETE FROM COMPLETE → TRASH
def cdelete(request, pk):
    data = Completemodel.objects.get(id=pk)
    Trashmodel.objects.create(
        title=data.title, 
        desc=data.desc
        )
    data.delete()
    return redirect('complete')


# RESTORE ALL FROM COMPLETE → HOME
def crestore_all(request):
    data = Completemodel.objects.all()
    for i in data:
        Taskmodel.objects.create(
            title=i.title, 
            desc=i.desc
            )
        i.delete()
    return redirect('complete')



# TRASH PAGE
def trash(request):
    data = Trashmodel.objects.all()
    return render(request, 'trash.html', {'data': data})


# RESTORE FROM TRASH → HOME
def trestore(request, pk):
    data = Trashmodel.objects.get(id=pk)
    Taskmodel.objects.create(
        title=data.title, 
        desc=data.desc
        )
    data.delete()
    return redirect('trash')


# DELETE PERMANENTLY FROM TRASH
def tdelete(request, pk):
    Trashmodel.objects.get(id=pk).delete()
    return redirect('trash')


# DELETE ALL FROM HOME → TRASH
def delete_all(request):
    data = Taskmodel.objects.all()
    for i in data:
        Trashmodel.objects.create(
            title=i.title, 
            desc=i.desc
            )
        i.delete()
    return redirect('home')


# RESTORE ALL FROM COMPLETE → HOME
def complete_deleteall(request):
    data = Completemodel.objects.all()
    for i in data:
        Taskmodel.objects.create(
            title=i.title, 
            desc=i.desc
            )
        i.delete()
    return redirect('complete')


# RESTORE ALL FROM COMPLETE → HOME
# COMPLETE ALL FROM HOME → COMPLETE PAGE
def complete_all(request):
    data = Taskmodel.objects.all()
    for i in data:
        Completemodel.objects.create(
            title=i.title, 
            desc=i.desc
            )
        i.delete()
    return redirect('complete')


# ABOUT PAGE
def about(request):
    return render(request, 'about.html')