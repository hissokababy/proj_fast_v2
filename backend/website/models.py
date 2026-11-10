
from django.db import models


class Teacher(models.Model):
    name_uz = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Имя (узбекский)"
    )
    name_ru = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Имя (русский)"
    )
    description_uz = models.TextField(blank=True, verbose_name="Описание (узбекский)")
    description_ru = models.TextField(blank=True, verbose_name="Описание (русский)")
    photo = models.ImageField(upload_to="teachers/", verbose_name="Фото")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        ordering = ["order"]
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.name_ru


class Certificate(models.Model):
    title_uz = models.CharField(max_length=150, blank=True, verbose_name="Название (узбекский)")
    title_ru = models.CharField(max_length=150, blank=True, verbose_name="Название (русский)")
    description_uz = models.TextField(blank=True, verbose_name="Описание (узбекский)")
    description_ru = models.TextField(blank=True, verbose_name="Описание (русский)")
    image = models.ImageField(upload_to="certificates/", verbose_name="Фото сертификата")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        ordering = ["order"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.title_ru or self.title_uz or f"Сертификат #{self.pk}"


class Event(models.Model):
    title_uz = models.CharField(
        blank=True,
        max_length=150,
        verbose_name="Название (узбекский)"
    )
    title_ru = models.CharField(max_length=150, blank=True, verbose_name="Название (русский)")
    description_uz = models.TextField(blank=True, verbose_name="Описание (узбекский)")
    description_ru = models.TextField(blank=True, verbose_name="Описание (русский)")
    image = models.ImageField(upload_to="events/", verbose_name="Фото мероприятия")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        ordering = ["order"]
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title_ru


class InteriorPhoto(models.Model):
    title_uz = models.CharField(max_length=150, blank=True, verbose_name="Название (узбекский)")
    title_ru = models.CharField(max_length=150, blank=True, verbose_name="Название (русский)")
    image = models.ImageField(upload_to="interiors/", verbose_name="Фото интерьера")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото интерьера"
        verbose_name_plural = "Фото интерьера"

    def __str__(self):
        return self.title_ru or self.title_uz or f"Фото интерьера #{self.pk}"


class Course(models.Model):
    title_uz = models.CharField(max_length=200, verbose_name="Название (узбекский)")
    title_ru = models.CharField(max_length=200, verbose_name="Название (русский)")
    description_uz = models.TextField(verbose_name="Описание (узбекский)")
    description_ru = models.TextField(verbose_name="Описание (русский)")
    image = models.ImageField(upload_to="courses/", verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    show_on_home = models.BooleanField(default=False, verbose_name="Показывать на главной")

    class Meta:
        ordering = ["order"]
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title_ru


class Application(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Новая"
        IN_PROGRESS = "in_progress", "В работе"
        COMPLETED = "completed", "Обработана"
        REJECTED = "rejected", "Отклонена"

    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Статус",
    )

    utm_source = models.CharField(max_length=255, blank=True, verbose_name="UTM Source")
    utm_medium = models.CharField(max_length=255, blank=True, verbose_name="UTM Medium")
    utm_campaign = models.CharField(max_length=255, blank=True, verbose_name="UTM Campaign")
    utm_term = models.CharField(max_length=255, blank=True, verbose_name="UTM Term")
    utm_content = models.CharField(max_length=255, blank=True, verbose_name="UTM Content")

    landing_page = models.URLField(max_length=1000, blank=True, verbose_name="Страница заявки")
    referrer = models.URLField(max_length=1000, blank=True, verbose_name="Источник перехода")
    language = models.CharField(max_length=5, blank=True, verbose_name="Язык сайта")

    telegram_notified_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата уведомления Telegram",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее обновление")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.full_name} — {self.phone}"


class OtherPhoto(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название (НЕ ИЗМЕНЯТЬ!!!)")
    key = models.SlugField(max_length=100, unique=True, verbose_name="Ключ (НЕ ИЗМЕНЯТЬ!!!)")
    image = models.FileField(upload_to="other/", verbose_name="Изображение")

    class Meta:
        verbose_name = "Другое фото"
        verbose_name_plural = "Другие фото"

    def __str__(self):
        return f"{self.title} ({self.key})"


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=150, default="FAST and EASY", verbose_name="Название сайта")
    logo = models.ImageField(upload_to="site/", blank=True, verbose_name="Логотип")
    favicon = models.ImageField(upload_to="site/", blank=True, verbose_name="Favicon")

    phone = models.CharField(max_length=30, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")

    address_uz = models.TextField(blank=True, verbose_name="Адрес (узбекский)")
    address_ru = models.TextField(blank=True, verbose_name="Адрес (русский)")

    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True, verbose_name="Широта")
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True, verbose_name="Долгота")

    working_hours_uz = models.TextField(blank=True, verbose_name="График работы (узбекский)")
    working_hours_ru = models.TextField(blank=True, verbose_name="График работы (русский)")

    instagram_url = models.URLField(blank=True, verbose_name="Instagram")
    telegram_url = models.URLField(blank=True, verbose_name="Telegram")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube")

    yandex_maps_api_key = models.CharField(max_length=255, blank=True, verbose_name="API-ключ Яндекс Карт")
    yandex_maps_map_id = models.CharField(max_length=255, blank=True, verbose_name="ID карты Яндекс")

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return self.site_name


class SEOSettings(models.Model):
    meta_title_uz = models.CharField(max_length=255, blank=True, verbose_name="Meta Title (узбекский)")
    meta_title_ru = models.CharField(max_length=255, blank=True, verbose_name="Meta Title (русский)")
    meta_description_uz = models.TextField(blank=True, verbose_name="Meta Description (узбекский)")
    meta_description_ru = models.TextField(blank=True, verbose_name="Meta Description (русский)")
    h1_uz = models.CharField(max_length=255, blank=True, verbose_name="H1 (узбекский)")
    h1_ru = models.CharField(max_length=255, blank=True, verbose_name="H1 (русский)")

    class Meta:
        verbose_name = "SEO-настройки"
        verbose_name_plural = "SEO-настройки"

    def __str__(self):
        return "SEO-настройки сайта"
