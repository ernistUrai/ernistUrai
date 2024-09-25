from django.db import models

class Phone(models.Model):
    PHONE_MAKE = (
        ("IPhone", "IPhone"),
        ("Samsung Galaxy", "Samsung Galaxy"),
        ("Google Pixel", "Google pixel"),
        ("Xiaomi ", "Xiaomi "),
    )
    
    
    
    title = models.CharField("Название смартфона", max_length=100, help_text="Максимум 100")
    description = models.TextField("Напишите описание")
    image = models.ImageField("Фотография смартфона", upload_to="")
    price = models.PositiveIntegerField("Цена")
    phone_make = models.CharField("Модель", max_length=100, choices=PHONE_MAKE)
    video = models.URLField("Видео")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title





class CommentPhone(models.Model):
    RATING = (
        ("*", "*"),
        ("**", "**"),
        ("***", "***"),
        ("****", "****"),
        ("*****", "*****"),
    )

    phone_choice_comment = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="comment")
    test = models.TextField()
    rate_starts = models.CharField(max_length=100, choices=RATING)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rate_starts