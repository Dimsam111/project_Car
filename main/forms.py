from django import forms  # Импортируем модуль forms из Django
from .models import Brand  # Импортируем нашу модель Image

class CarAddForm(forms.Form):  # Создаем класс ImageForm, который наследуется от forms.ModelForm
        brand = forms.ModelChoiceField(queryset=Brand.objects.all())
        model = forms.CharField(max_length=50)# Указываем, что форма основана на модели Image
        price = forms.DecimalField(max_digits=8, decimal_places=2)
        image = forms.ImageField()
        color = forms.CharField(max_length=100)
        description = forms.CharField(widget=forms.Textarea())
        annotation = forms.CharField(max_length=1000)



