from django.contrib.auth.models import AdvUser
from django.db import models

class CustomUser(AdvUser):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(unique=True, verbose_name="Email")
    agreement = models.BooleanField(default=False, verbose_name="Согласие на обработку персональных данных")

    def __str__(self):
        return self.username

class Application(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'Принято в работу'),
        ('completed', 'Выполнено'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=50, verbose_name="Категория")
    photo = models.ImageField(upload_to='applications/', verbose_name="Фото помещения")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Временная метка")

    def __str__(self):
        return self.title


