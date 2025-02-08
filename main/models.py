from django.db import models


# Create your models here.

class Brand (models.Model):
    title =models.CharField(max_length=50)

    def __str__(self):
        return self.title

class CarImage(models.Model):
    picture = models.ImageField(upload_to="car")
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    def __str__(self):
        return self.car.model



class Car (models.Model):
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='car')
    color = models.CharField(max_length=100)
    description = models.TextField()
    annotation = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.brand} {self.model}'

# from django.db import models  # Импортируем модуль models из Django

# class Image(models.Model):  # Создаем класс Image, который наследуется от models.Model
#     title = models.CharField(max_length=100)  # Поле для названия изображения (строка длиной до 100 символов)
#     image = models.ImageField(upload_to='images/')  # Поле для загрузки изображения, файлы будут сохраняться в папку 'images/'
#     description = models.TextField(blank=True, null=True)  # Поле для описания, можно оставить пустым
#     uploaded_at = models.DateTimeField(auto_now_add=True)  # Поле для времени загрузки, автоматически устанавливается текущее время
#
#     def __str__(self):  # Метод, который возвращает строковое представление объекта
#         return self.title  # Возвращает название изображения





