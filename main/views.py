from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from main.models import Car, Brand, CarImage

from .forms import CarAddForm


# Create your views here.
def get_main_page(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    context = {
        'cars': cars,
        'brands': brands,
    }
    return render(request, 'main.html', context)


def car_detail(request, id):
    cars = Car.objects.get(id=id)
    picture = CarImage.objects.filter(car=id)
    context = {
        'car': cars,
        "picture": picture
    }
    return render(request, 'car_detail.html', context)


def car_add(request):
    form = CarAddForm()
    # print(form.is_bound, '29')
    if request.method == "POST":
        form = CarAddForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            new_car = Car(brand=form.cleaned_data.get('brand'),
                          model=form.cleaned_data.get('model'),
                          price=form.cleaned_data.get('price'),
                          image=form.cleaned_data.get('image'),
                          color=form.cleaned_data.get('color'),
                          description=form.cleaned_data.get('description'),
                          annotation=form.cleaned_data.get('annotation',))
            new_car.save()
            additional_img = CarImage(picture=form.cleaned_data.get('additional_img'),
                                      car_id=new_car.id)
            additional_img.save()

        # print(form.is_bound,"32")

    context = {
        "form": form
    }
    return render(request, 'car_add.html', context)  # Отображаем форму на странице upload_image.html
