from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    category = models.Category.objects.all()
    images = models.Images.objects.all()
    data = {'category': category, 'images': images}
    return render(request, 'home/home.html', data)

def category(request, id):

    category = models.Category.objects.all()
    select_cat = models.Category.objects.get(id = id)
    check_cat = models.Images.objects.filter(cat_foreign = id)

    data = {'images': check_cat}

    return render(request, 'home/home.html', data)