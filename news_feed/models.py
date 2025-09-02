from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    publication_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    body = RichTextField(verbose_name="Тело новости")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Главное изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-publication_date']