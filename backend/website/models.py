from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    photo = models.ImageField(upload_to="teachers/", verbose_name="Фото")
    description = models.TextField(blank=True, verbose_name="Описание")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to="certificates/", verbose_name="Фото сертификата")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to="events/", verbose_name="Фото мероприятия")
    description = models.TextField(blank=True, verbose_name="Описание")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title


class InteriorPhoto(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to="interiors/", verbose_name="Фото интерьера")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото интерьера"
        verbose_name_plural = "Фото интерьера"

    def __str__(self):
        return self.title


class Application(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name="ФИО"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Номер телефона"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата заявки"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.full_name} — {self.phone}"