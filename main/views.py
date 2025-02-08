from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from main.models import Car, Brand, CarImage

from .forms import CarAddForm


# Create your views here.
def get_main_page(request):
    cars =Car.objects.all()
    brands=Brand.objects.all()
    context = {
        'cars': cars,
        'brands':brands,
    }
    return render(request,'main.html', context)


def car_detail(request,id):
    cars =Car.objects.get(id=id)
    picture = CarImage.objects.filter(car=id)
    context = {
        'car': cars,
        "picture": picture
    }
    return render(request,'car_detail.html', context)

def car_add(request):
    form = CarAddForm()
    # print(form.is_bound, '29')
    if request.method == "POST":
        form = CarAddForm(request.POST, request.FILES)
        # print(form.is_bound,"32")

    context = {
        "form": form
    }
    return render(request, 'car_add.html', context )  # Отображаем форму на странице upload_image.html




