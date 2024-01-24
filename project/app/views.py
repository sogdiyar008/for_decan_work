from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponseNotFound
def index(request):
    tovars = Shop.objects.all()
    return render(request,'app/index.html', {'tovars': tovars})

def add(request):
    error = ''
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была не верной:_('
    form=ShopForm
    data={
        'form': form,
        'error':error,
    }
    return render(request, 'app/add.html', data)

def edit(request, id):
    try:
        tovar = Shop.objects.get(id=id)
        if request.method=="POST":
            tovar.name = request.POST.get("name")
            tovar.info = request.POST.get("info")
            tovar.img = request.POST.get("img")
            tovar.price = request.POST.get("price")
            tovar.save()
            return HttpResponseRedirect("..")
        else:
            form = ShopForm(request.POST, instance=tovar)
            return render(request, 'app/edit.html', {'form': form })
    except Shop.DoesNotExist:
        return HttpResponseNotFound('Не найдено')


def delete(request, id):
    try:
        child =Shop.objects.get(id=id)
        child.delete()
        return HttpResponseRedirect('..')
    except Shop.DoesNotExist:
        return HttpResponseNotFound('Человек не найден')